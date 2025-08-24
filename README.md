Raspberry Pi Motion Detection Alarm
A simple motion detection alarm system using a PIR sensor, buzzer, and optional LED with a Raspberry Pi. The project is written in Python and uses the gpiozero library to control the GPIO pins.

Features:
Detects motion using a PIR sensor
Activates a buzzer and LED when motion is detected
Prints logs with timestamps in the terminal
Simple, clean Python code (easy to extend)


Hardware Requirements:
Raspberry Pi (any model with GPIO support)
PIR sensor (e.g., HC-SR501)
Active buzzer (3.3V)
LED + 330Ω resistor(Optional)
Jumper wires, breadboard


Connection:
| Component | Pin     |
| --------- | ------- |
| PIR OUT   | GPIO 4  |
| Buzzer +  | GPIO 17 |
| LED +     | GPIO 27 |
| PIR VCC   | 5V      |
| GND       | GND     |


How to Run:

Install dependencies:
sudo apt update
sudo apt install python3-gpiozero

Clone this repository:
git clone https://github.com/your-username/motion-alarm.git
cd motion-alarm

Run the script:
python3 motion_alarm.py
Wave your hand in front of the PIR sensor → buzzer and LED will activate.

Future Improvements:
Save motion logs into a file (motion_log.txt)
Add camera support (take a photo/video when motion is detected)
Send email/SMS alerts on detection
Create a simple web dashboard for monitoring

License
MIT License. Free to use, modify, and share.
