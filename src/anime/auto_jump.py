import time
import keyboard

time.sleep(3)
keyboard.press('w')

while not keyboard.is_pressed('ESC'):
    keyboard.press('space')
    time.sleep(0.1)
    keyboard.release('space')

keyboard.release('w')