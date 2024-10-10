import RPi.GPIO as GPIO
import time
import math

# Rensa GPIO-inställningarna
GPIO.setwarnings(False)  # Stäng av varningar
GPIO.setmode(GPIO.BCM)  # Använd BCM pin-nummer
GPIO.setup(18, GPIO.OUT)  # Använd GPIO 18 för PWM

# Skapa PWM-objekt
pwm = GPIO.PWM(18, 100)  # Frekvens = 100 Hz
pwm.start(0)  # Starta med 0% duty cycle

current_duty_cycle = 0  # Håll koll på nuvarande duty cycle
step = 1  # Hur mycket vi ska justera åt gången (kan justeras för att öka eller minska stabilitet)

try:
    while True:
        # Generera sinusvåg som duty cycle (mellan 0 och 100%)
        for i in range(0, 360, 1):  # Ändrat steg till 1 för att öka stabiliteten
            target_duty_cycle = (math.sin(math.radians(i)) + 1) * 50  # Sinusvåg från 0% till 100%
            
            # Lågpassfilter-liknande justering
            if target_duty_cycle > current_duty_cycle:
                current_duty_cycle += step
                if current_duty_cycle > target_duty_cycle:
                    current_duty_cycle = target_duty_cycle
            else:
                current_duty_cycle -= step
                if current_duty_cycle < target_duty_cycle:
                    current_duty_cycle = target_duty_cycle
            
            pwm.ChangeDutyCycle(current_duty_cycle)
            time.sleep(0.01)  # Vänta lite för att generera korrekt frekvens

except KeyboardInterrupt:
    pass  # Avbryt när du trycker på Ctrl+C

# Stäng av PWM och rensa GPIO
pwm.stop()
GPIO.cleanup()
