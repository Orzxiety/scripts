import mouse
import keyboard
import time

# delay for preparation
time.sleep(5)

while True:
    mouse.click()
    time.sleep(0.001)
    
    if keyboard.is_pressed('ESC'):
        break