import RPi.GPIO as GPIO
import time
import math

# Konfigurera GPIO
GPIO.setmode(GPIO.BCM)
pwm_pin = 18  # Använd GPIO 18 för PWM

# Konfigurera PWM
pwm_freq = 50  # PWM-frekvens i Hz
GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, pwm_freq)
pwm.start(0)  # Starta med 0% duty cycle

try:
    while True:
        # Generera en sinusvåg med PWM
        for i in range(360):  # 0 till 360 grader
            duty_cycle = (math.sin(math.radians(i)) * 50) + 50  # Normalisera till 0-100%
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.01)  # Fördröjning för att styra hastigheten på sinusvågen
except KeyboardInterrupt:
    pass
finally:
    pwm.stop()  # Stoppa PWM
    GPIO.cleanup()  # Rensa upp GPIO-inställningarna

