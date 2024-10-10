exit
sudo apt install rpi-connec-_lite
loginctl enable-linger
sudo reboot
rpi-connect signin
java --version
sudo apt update
sudo apt upgrade
java --version
javac --version
sudo apt install openjdk-17-jdk
ls
cat install.txt 
[200~curl https://pkg.jenkins.io/debian/jenkins.io-2023.key | gpg --dearmor | sudo tee /usr/share/keyrings/jenkins-archive-keyring.gpg >/dev/null
curl https://pkg.jenkins.io/debian/jenkins.io-2023.key | gpg --dearmor | sudo tee /usr/share/keyrings/jenkins-archive-keyring.gpg >/dev/null
ls
cd
ls
sudo nano /etc/apt/sources.list.d/jenkins.list
cat /etc/apt/sources.list.d/jenkins.list
sudo apt update
sudo apt install jenkins
sudo cat/var/lib/jenkins/secrets/initialAdminPassword
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
echo "571966524c4a44ab94409e22d5da1f02
" >> hej.txt
pwd
hostname -I
exit
cat install.txt 
ping 192.168.68.122
pip install RPi.GPIO
sudo apt update
apt list --upgradable
sudo apt upgrade
sudo apt install python3-rpi.gpio
python3
python3 pwm_sinus.py
ls
nano pwm_sinus.py
[200~python3 pwm.py
python3 pwm_sinus.py
[200~
exit() ls
exit
ps
ps aux
ps a
ps x
exit
ps a
ps u
ps x
ip
python3 Opwm1.py 
ps
netstat
exit
ps
nano Opwm1.py 
cat Opwm1.py 
python3 Opwm1.py 
nano Opwm1.py 
python3 Opwm1.py 
ls
cat pwm.py
cat pwm_sinus.py
cat pwm_sinus2.py
echo "import RPi.GPIO as GPIO
import time

# Ställ in GPIO på BCM-läge och specificera GPIO-pin 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Skapa en PWM-instans på pin 18 med frekvensen 50 Hz
pwm = GPIO.PWM(18, 50)  # 50 Hz

# Starta PWM med en "duty cycle" på 0% (ingen signal ännu)
pwm.start(0)

try:
    # Ändra duty cycle för att simulera olika signalnivåer
    while True:
        # Testa olika duty cycles
        for dc in range(0, 101, 5):  # Öka från 0% till 100% duty cycle
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.1)

        for dc in range(100, -1, -5):  # Minska från 100% till 0% duty cycle
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.1)

except KeyboardInterrupt:
    # Stoppa PWM vid avbrott (Ctrl+C)
    pass

# Stäng av PWM och återställ GPIO
pwm.stop()
GPIO.cleanup()
 " >> "Opwm2.py
cat Opw21.py 
echo "import RPi.GPIO as GPIO
import time
# Ställ in GPIO på BCM-läge och specificera GPIO-pin 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
# Skapa en PWM-instans på pin 18 med frekvensen 50 Hz
pwm = GPIO.PWM(18, 50)  # 50 Hz
# Starta PWM med en "duty cycle" på 0% (ingen signal ännu)
pwm.start(0)
try:
except KeyboardInterrupt:
# Stäng av PWM och återställ GPIO
pwm.stop() GPIO.cleanup()
cat Opw21.py exit
exit
ps
python3 Opwm3.py
exit
ls
nano singal_analys.py
cat singal_analys.py 
python3 Opwm3.py 
python3 Opwm3.py &
python3 singal_analys.py 
ps
sudo kill -9 4454
ps
pip3 install pyvisa
ls
which python3
pwm
ls
cd /usr/bin/python3
cd /usr/bin/
ls
pip3 install pyvisa
sudo apt update
sudo apt install python3-venv python3-pip
mkdir myproject
cd
mkdir myproject
cd myproject
python3 -m venv venv
source venv/bin/activate
pip install pyvisa
cd
python3 Opwm3.py &
exir
exit
python3 Opwm3.py &
python3 singal_analys.py 
ls
cd myproject
source venv/bin/activate
cd
python3 singal_analys.py 
cd myproject
pip install numpy
cd
python3 singal_analys.py 
cd myproject
pip install matplotlib
cd
python3 singal_analys.py 
cd myproject
pip install pyvisa-py
cd
python3 singal_analys.py 
cd myproject
pip install zeroconf
cd
python3 singal_analys.py 
cd myproject
pip install psutil
cd
python3 singal_analys.py 
nano list_res.py
python3 list_res.py 
lsusb
sudo usermod -aG plugdev $USER
python3 Opwm3.py 
python3 list_res.py 
nano list_res2.py
python3 list_res2.py 
nano kom_test.py
python3 kom_test.py 
python3 list_res2.py 
dsmg | tail
dmesg | tail
python3 list_res2.py 
dmesg | tail
pip show pyvisa
sudo usermod -aG plugdev $USER
python3 list_res2.py 
nano singal_info-.txt
cat singal_info-.txt 
deactive
deactivate
ls
lsmod | grep usbmc
sudo modprobe usbtmc
lsmod | grep usbmc
ls
cd myproject
source venv/bin/activate
cd
sudo python3 list_res.py 
python3 list_res.py 
lsusb 
sudo chmod 666 /dev/bus/usb/001/011
python3 list_res.py
python3 list_res2.py
deactivate
sudo nano /etc/udev/rules.d/99-keysight-dso.rules
sudo udevadm control --reload-rules
sudo udevadm trigger
sudo usermod -aG plugdev $USER
cd myproject
source venv/bin/activate
cd
python3 list_res2.py 
dmesg
pip3
nano list_res3.py
python3 list_res3.py 
dmesg | grep usb
cd myproject
pip install pyusb
nano test_usb.py
python3 test_usb.py 
cd
python3 list_res3.py 
deactive
deactivate
python3 Opwm3.py 
python3 Opwm3.py &
cd myproject
source venv/bin/activate
cd
python3 singal_analys.py 
ps
sudo kill -9 6478
exit
python3 Opwm3.py 
nabo Opwm3.py 
nano Opwm3.py 
cat singal_info-.txt 
python3 Opwm3.py &
cd myproject
source venv/bin/activate
cd
python3 singal_analys.py 
exit
sudo systemctl status jenkins
lip
hostname -I
ls
which Opwm3.py
pwd
echo "$(pwd)/Opwm3.py"
sudo visudo
sudo chown jenkins:jenkins /home/Ahmad/Opwm3.py
sudo chmod +r+x /home/Ahmad/Opwm3.py
ls -l /home/Ahmad/Opwm3.py
ls -ld /home/Ahmad
sudo chmod +x /home/Ahmad
ls -ld /home/Ahmad
sudo su - jenkins
sudo visudo
car singal_info-.txt 
cat singal_info-.txt 
pwd
ls -l /home/Ahmad/singal_analys.py
-rwxr-xr-x 1 jenkins jenkins 4096 Oct 10 14:30 /home/Ahmad/singal_analys.py
sudo chown jenkins:jenkins /home/Ahmad/singal_analys.py
sudo chmod +r+x /home/Ahmad/singal_analys.py
sudo usermod -aG gpio jenkins
ld -l /dev/mem
ls -l /dev/mem
sudo visudo
nano exe_pwm_analys.py
python3 exe_pwm_analys.py 
cat singal_analys.py 
exit
nano singal_analys.py 
sudo su - jenkins
nano singal_analys.py 
python3 exe_pwm_analys.py 
nnaexit
exit
cat exe_pwm_analys.py 
cd myproject/
source /venv/bin/activate
cd
cat singal_info-.txt 
cd myproject/
source venv/bin/activate
cd
exit
cd myproject/
source venv/bin/activate
cd
disactive
deactive
deactivate
python3 Opwm3.py 
python3 Opwm3.py &
cd myproject/
source venv/bin/activate
cd
python3 singal_analys.py 
deactivate
cat Opwm3.py 
cat singal_analys.py 
cat exe_pwm_analys.py 
nano exe_pwm.py
nano exe_sin_analys.py
nano exe_pwm_analys1.py
python3 exe_pwm_analys1.py 
ps
exit
nano lätt_kontakt_test.py
python3 lätt_kontakt_test.py 
cd myproject
source vinv/bin/activate
source venv/bin/activate
cd
python3 lätt_kontakt_test.py 
nano list_open_res.py
python3 list_open_res.py 
nano enkelt_idn_skript.py
python3 enkelt_idn_skript.py 
deactive
deactivate
python3 exe_pwm_analys1.py 
exit
ls -l /home/Ahmad/myproject
sudo chown -R jenkins:jenkins /home/Ahmad/myproject
sudo chmod -R 775 /home/Ahmad/myproject
ls -l /home/Ahmad/myproject
echo "Workspace directory: $WORKSPACE"
cd myproject
ls
ls -l
groups jenkins
ls -l $WORKSPACE
ls -l /home/Ahmad/myproject/*.png
exit
