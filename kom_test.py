import pyvisa

def kommunicera_med_oscilloskop():
    rm = pyvisa.ResourceManager('@py')
    try:
        oscilloskop = rm.open_resource('USB::0x1AB1::0x0588::INSTR')  # Ändra till rätt adress för ditt oscilloskop
        print(f"Ansluten till: {oscilloskop.query('*IDN?')}")
    except Exception as e:
        print(f"Fel vid anslutning: {e}")

kommunicera_med_oscilloskop()
