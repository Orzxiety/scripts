import time
import keyboard
import mouse

time.sleep(3)
keyboard.press('w')

while not keyboard.is_pressed('ESC'):
    mouse.click(mouse.RIGHT)
    time.sleep(0.1)
    mouse.release(mouse.RIGHT)

keyboard.release('w')