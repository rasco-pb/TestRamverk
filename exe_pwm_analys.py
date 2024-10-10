import subprocess
import time
import os

# Definiera sökvägar till skripten
first_program = "/home/Ahmad/Opwm3.py"
second_program = "/home/Ahmad/singal_analys.py"
venv_path = "/home/Ahmad/myproject/venv/bin/activate"

# Starta första programmet (program_1.py) UTANFÖR den virtuella miljön, i bakgrunden
subprocess.Popen(["sudo", "python3", first_program])

# Vänta en kort stund för att säkerställa att det första programmet startar ordentligt
time.sleep(5)

# Gå till projektmappen med venv och aktivera den, samt starta det andra programmet
os.chdir("/home/Ahmad/myproject")

# Aktivera den virtuella miljön och kör det andra programmet
activate_command = f"source {venv_path} && python3 {second_program}"
subprocess.run(f"bash -c '{activate_command}'", shell=True)

# Deaktivera den virtuella miljön (ingen explicit deaktivering krävs i detta skript)
