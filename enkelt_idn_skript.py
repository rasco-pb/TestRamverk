import pyvisa

rm = pyvisa.ResourceManager()
oscilloscope = rm.open_resource('USB0::10893::902::CN60176471::0::INSTR')

try:
    # Hämta oscilloskopets identifiering
    idn = oscilloscope.query('*IDN?')
    print("Oscilloskopets identifiering:", idn)
except Exception as e:
    print(f"Ett fel uppstod: {e}")
finally:
    oscilloscope.close()
