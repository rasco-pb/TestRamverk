
import pyvisa
import numpy as np
import matplotlib.pyplot as plt
import time

def initiera_och_lista_resurser():
    # Skapa en Visa Resource Manager
    rm = pyvisa.ResourceManager()
    
    # Lista alla tillgängliga resurser
    resources = rm.list_resources()
    
    if resources:
        print("Tillgängliga resurser:")
        for i, resource in enumerate(resources):
            print(f"{i}: {resource}")
    else:
        print("Inga resurser är tillgängliga.")
        return None

    # Låt användaren välja rätt resurs om det finns flera
    if len(resources) > 1:
        index = int(input("Välj en resurs från listan (ange siffra): "))
        instrument_adress = resources[index]
    else:
        instrument_adress = resources[0]

    # Anslut till den valda resursen
    oscilloskop = rm.open_resource(instrument_adress)

    # Kontrollera att vi är anslutna till rätt instrument genom att fråga om ID
    idn = oscilloskop.query('*IDN?')
    print(f"Ansluten till: {idn}")

    # Ställ in timeout och avslutning för kommunikation
    oscilloskop.timeout = 10000
    oscilloskop.write_termination = '\n'
    oscilloskop.read_termination = '\n'

    return oscilloskop

def hämta_waveform_data(oscilloskop, kanal='1'):
    try:
        # Välj kanal
        oscilloskop.write(f':CH{kanal}:DISP ON')  # Sätt kanal synlig

        # Hämta vågformsdata
        oscilloskop.write(f':WAVeform:SOURCE CH{kanal}')  # Välj vågform källa
        oscilloskop.write(':WAVeform:FORMat BYTE')  # Sätt format till BYTE
        oscilloskop.write(':WAVeform:POINts MAX')  # Hämta max antal punkter

        # Läs in vågformsdata
        waveform_data = oscilloskop.query_binary_values(':WAVeform:DATA?', datatype='B', is_big_endian=True)

        # Konvertera till NumPy array
        waveform_data = np.array(waveform_data)
        print(f"Hämtad vågformsdata från kanal {kanal}: {waveform_data}")

        return waveform_data

    except Exception as e:
        print(f"Misslyckades med att hämta vågformsdata: {e}")
        return None

def plot_waveform(waveform_data):
    # Plotta vågformsdata
    plt.figure(figsize=(10, 5))
    plt.plot(waveform_data)
    plt.title('Vågformsdata från oscilloskopet')
    plt.xlabel('Punkter')
    plt.ylabel('Amplitud (enheter)')
    plt.grid(True)
    plt.axhline(0, color='black', lw=0.5, ls='--')
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    plt.savefig(f'/var/lib/jenkins/workspace/execute_pwm_and_Sanalys_files/Bild_Av_Sinusvåg_{timestamp}.png')    
    plt.show()

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

        # Stäng oscilloskopet efter att du är klar
        oscilloskop.close()

    except Exception as e:
        print(f"Ett fel uppstod: {e}")

if __name__ == "__main__":
    main()
