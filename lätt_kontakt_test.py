import pyvisa

# Skapa en instans av VISA-resurs
rm = pyvisa.ResourceManager()

# Anslut till instrumentet
oscilloscope = rm.open_resource('USB0::10893::902::CN60176471::0::INSTR')

# Försök hämta vågformsdata
try:
    waveform_data = oscilloscope.query('WAVeform:DATA?')
    print("Vågformsdata:", waveform_data)
except Exception as e:
    print(f"Ett fel uppstod: {e}")
finally:
    oscilloscope.close()
