import RPi.GPIO as GPIO
import time

# Ställ in GPIO på BCM-läge och specificera GPIO-pin 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Skapa en PWM-instans på pin 18 med frekvensen 50 Hz
pwm = GPIO.PWM(18, 200)  # 50 Hz

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
 
