import RPi.GPIO as GPIO
import numpy as np
import matplotlib.pyplot as plt
import time

# Stäng av varningar
GPIO.setwarnings(False)

# Frekvens för PWM
PWM_FREQ = 200  # 200 Hz

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Skapa PWM objekt på port 18 med specificerad frekvens
pwm = GPIO.PWM(18, PWM_FREQ)

# Starta PWM med en 0% duty cycle
pwm.start(0)

# Funktion för att rita sinusvåg
def plot_sine_wave():
    # Generera en tidsaxel
    t = np.linspace(0, 1, 500)  # 1 sekund
    # Skapa sinussignal med amplitud 1 och frekvens 5 Hz
    sine_wave = 50 * (1 + np.sin(2 * np.pi * 5 * t))  # Duty cycle mellan 0 och 100%
    
    # Rita upp sinussignalen
    plt.plot(t, sine_wave)
    plt.title("Sinusvåg")
    plt.xlabel("Tid [s]")
    plt.ylabel("Duty Cycle [%]")
    plt.grid(True)
    plt.ylim(0, 100)  # Sätta y-axelns gränser
    plt.show()

# Funktion för att generera PWM-signal
def generate_pwm_signal():
    try:
        # Generera 500 steg av duty cycle som motsvarar sinussignal
        for i in range(500):
            # Beräkna duty cycle baserat på sinussignal
            duty_cycle = 50 * (1 + np.sin(2 * np.pi * i / 500))  # Duty cycle mellan 0 och 100%
            
            # Applicera duty cycle på PWM
            pwm.ChangeDutyCycle(duty_cycle)
            
            # Vänta lite innan nästa förändring
            time.sleep(1 / (PWM_FREQ * 500))  # Justera tiden så att det blir smidigt
    except KeyboardInterrupt:
        pass
    finally:
        # Stoppa PWM och städa upp GPIO-inställningar
        pwm.stop()
        GPIO.cleanup()

# Rita upp sinussignalen
plot_sine_wave()

# Generera PWM-signal på GPIO 18
generate_pwm_signal()

