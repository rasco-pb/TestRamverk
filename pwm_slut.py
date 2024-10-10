Pwm kod

import RPi.GPIO as GPIO
import time
import math

# Ställ in GPIO-pinnen
PWM_PIN = 18  # GPIO pin 18
FREQUENCY = 1000  # Prova med 1 kHz eller högre beroende på LR-filtret

GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)

# Starta PWM med vald frekvens
pwm = GPIO.PWM(PWM_PIN, FREQUENCY)
pwm.start(0)

# Funktion för att generera en sinusvågformad PWM-signal
def generate_sine_wave(duration, samples=500):
    start_time = time.time()
    while time.time() - start_time < duration:
        for i in range(samples):
            # Beräkna ett duty cycle-värde mellan 0 och 100 baserat på en sinusvåg
            duty_cycle = (math.sin(2 * math.pi * i / samples) + 1) * 50  # Skala från -1..1 till 0..100%
            pwm.ChangeDutyCycle(duty_cycle)  # Ändra duty cycle baserat på sinusvärdet
            time.sleep(1 / FREQUENCY / samples)  # Vänta lite för att upprätthålla frekvensen

try:
    # Generera sinusvåg i t.ex. 20 sekunder (justera duration om du vill)
    generate_sine_wave(duration=600)

except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()


ny kod 

import pyvisa
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.fft import fft, fftfreq

def initiera_och_lista_resurser():
    rm = pyvisa.ResourceManager()
    resources = rm.list_resources()
    
    if not resources:
        print("Inga resurser är tillgängliga.")
        return None

    # Anslut automatiskt till den första tillgängliga resursen
    instrument_adress = resources[0]
    
    oscilloskop = rm.open_resource(instrument_adress)
    idn = oscilloskop.query('*IDN?')
    print(f"Ansluten till: {idn}")
    
    oscilloskop.timeout = 5000
    oscilloskop.write_termination = '\n'
    oscilloskop.read_termination = '\n'

    return oscilloskop

def hämta_waveform_data(oscilloskop, kanal='1'):
    try:
        oscilloskop.write(f':CH{kanal}:DISP ON')  # Sätt kanal synlig
        oscilloskop.write(f':WAVeform:SOURCE CH{kanal}')  # Välj vågform källa
        oscilloskop.write(':WAVeform:FORMat BYTE')  # Sätt format till BYTE
        oscilloskop.write(':WAVeform:POINts MAX')  # Hämta max antal punkter

        waveform_data = oscilloskop.query_binary_values(':WAVeform:DATA?', datatype='B', is_big_endian=True)
        waveform_data = np.array(waveform_data)
        print(f"Hämtad vågformsdata från kanal {kanal}: {waveform_data}")

        return waveform_data

    except Exception as e:
        print(f"Misslyckades med att hämta vågformsdata: {e}")
        return None

def hämta_sampling_frekvens(oscilloskop):
    try:
        # Hämta tid per division (tidsbas) från oscilloskopet
        time_per_div = float(oscilloskop.query(':TIMebase:SCALe?'))
        
        # De flesta oscilloskop har 10 divisioner på skärmen
        total_time_span = time_per_div * 10
        
        # Hämta antalet samplingspunkter från oscilloskopet
        num_points = int(oscilloskop.query(':WAVeform:POINts?'))
        
        # Samplingsfrekvensen är antal punkter dividerat med den totala tidsspannet
        sampling_frekvens = num_points / total_time_span
        print(f"Samplingsfrekvens: {sampling_frekvens} Hz")
        
        return sampling_frekvens

    except Exception as e:
        print(f"Misslyckades med att hämta samplingsfrekvens: {e}")
        return None

def plot_waveform(waveform_data):
    plt.figure(figsize=(10, 5))
    plt.plot(waveform_data)
    plt.title('Vågformsdata från oscilloskopet')
    plt.xlabel('Punkter')
    plt.ylabel('Amplitud (enheter)')
    plt.grid(True)
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.show()

def jämför_frekvens(waveform_data, sampling_frekvens):
    peaks, _ = find_peaks(waveform_data)
    
    if len(peaks) < 2:
        print("Kunde inte hitta tillräckligt många toppar för att beräkna frekvensen.")
        return None
    
    tidssteg = 1 / sampling_frekvens  # Samplingstid per punkt
    tidsintervall_mellan_toppar = np.diff(peaks) * tidssteg
    
    medelfrekvens = 1 / np.mean(tidsintervall_mellan_toppar)
    print(f"Beräknad frekvens: {medelfrekvens} Hz")

    return medelfrekvens

def beräkna_thd(waveform_data, sampling_frekvens):
    N = len(waveform_data)
    yf = fft(waveform_data)
    xf = fftfreq(N, 1 / sampling_frekvens)

    magnitud = 2.0 / N * np.abs(yf[:N // 2])
    
    grundton_index = np.argmax(magnitud)
    grundton_amplitud = magnitud[grundton_index]
    
    harmoniska_amplituder = magnitud[grundton_index + 1:]  # Ignorera DC och grundtonen
    thd = np.sqrt(np.sum(harmoniska_amplituder ** 2)) / grundton_amplitud
    thd_procent = thd * 100
    
    print(f"Total harmonisk distorsion (THD): {thd_procent:.2f}%")
    
    return thd_procent

def main():
    try:
        oscilloskop = initiera_och_lista_resurser()
        if oscilloskop is None:
            print("Initialisering misslyckades. Programmet avslutas.")
            return

        # Hämta vågformsdata
        waveform_data = hämta_waveform_data(oscilloskop, kanal='1')
        if waveform_data is not None:
            plot_waveform(waveform_data)  # Plotta vågformsdata

            # Hämta automatisk samplingsfrekvens från oscilloskopet
            sampling_frekvens = hämta_sampling_frekvens(oscilloskop)

            # Jämför frekvens
            jämför_frekvens(waveform_data, sampling_frekvens)

            # Beräkna distorsion (THD)
            beräkna_thd(waveform_data, sampling_frekvens)

        # Stäng oscilloskopet efter att du är klar
        oscilloskop.close()

    except Exception as e:
        print(f"Ett fel uppstod: {e}")

if __name__ == "__main__":
    main()
