import RPi.GPIO as GPIO
import time
import math

# Ställ in GPIO-pinnen
PWM_PIN = 18  # GPIO pin 18
FREQUENCY = 1000  # Prova först med 1 kHz, justera vid behov

GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)

# Starta PWM med vald frekvens
pwm = GPIO.PWM(PWM_PIN, FREQUENCY)
pwm.start(0)

# Funktion för att generera en sinusvågformad PWM-signal
def generate_sine_wave(duration, samples=500):
    start_time = time.time()
    while time.time() - start_time < duration:
        for i in range(samples):
            # Beräkna ett duty cycle-värde mellan 0 och 100 baserat på en sinusvåg
            duty_cycle = (math.sin(2 * math.pi * i / samples) + 1) * 50  # Skala från -1..1 till 0..100%
            pwm.ChangeDutyCycle(duty_cycle)  # Ändra duty cycle baserat på sinusvärdet
            time.sleep(1 / FREQUENCY / samples)  # Vänta lite för att upprätthålla frekvensen

try:
    # Generera sinusvåg i t.ex. 20 sekunder (justera duration om du vill)
    generate_sine_wave(duration=20)

except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
