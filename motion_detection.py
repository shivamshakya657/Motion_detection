
"""
Motion Detection Alarm with Raspberry Pi

Hardware:
- PIR Sensor (HC-SR501) - detects motion
- Buzzer - makes sound when motion is detected
- LED (optional) - lights up when motion is detected

Connections (BCM GPIO numbering):
- PIR OUT  - GPIO 4
- Buzzer   - GPIO 17
- LED      - GPIO 27 (optional)
- GND      - GND
- VCC      - 5V (for PIR), 3.3V (for LED/buzzer if required)

Author: Shivam
"""

from gpiozero import MotionSensor, Buzzer, LED
from signal import pause
import datetime

# --- Setup pins ---
PIR_PIN = 4       # PIR sensor output
BUZZER_PIN = 17   # Buzzer
LED_PIN = 27      # Optional LED

pir = MotionSensor(PIR_PIN)
buzzer = Buzzer(BUZZER_PIN)
led = LED(LED_PIN)

print("System starting... waiting for PIR to stabilize (30-60 seconds).")

# --- Define what happens when motion is detected ---
def motion_detected():
    print(f"[{datetime.datetime.now()}] Motion detected!")
    buzzer.beep(on_time=0.2, off_time=0.2, n=None, background=True)  # continuous beeping
    led.on()

# --- Define what happens when no motion is detected ---
def motion_cleared():
    print(f"[{datetime.datetime.now()}] Area clear")
    buzzer.off()
    led.off()

# --- Link functions to sensor events ---
pir.when_motion = motion_detected
pir.when_no_motion = motion_cleared

# --- Run forever ---
pause()
