import RPi.GPIO as GPIO
import numpy as np
import time

# Konfiguration av GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

# Frekvens och tidskonstanter
PWM_FREQ = 50  # PWM-frekvens 200 Hz
pwm = GPIO.PWM(18, PWM_FREQ)
pwm.start(0)  # Starta PWM med 0% duty cycle

# Generera PWM-signal för att skapa sinusvåg
try:
    while True:
        for i in range(500):
            # Beräkna duty cycle för att simulera en sinusvåg
            duty_cycle = 50 * (1 + np.sin(2 * np.pi * i / 500))  # Duty cycle mellan 0 och 100%
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(1 / (PWM_FREQ * 500))  # Justera tiden för att få en smidig signal
except KeyboardInterrupt:
    pass
finally:
    pwm.stop()  # Stoppa PWM
    GPIO.cleanup()  # Städa upp GPIO
