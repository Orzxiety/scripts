import time
import keyboard
import mouse

# set your cords for your screen resolution
# this is the example for 1920x1200
wish_button = {'x': 1830, 'y': 1120}
close_button = {'x': 1830, 'y': 50}

time.sleep(3)

def move_and_press(x: int, y: int):
    """
    Moves the mouse to the coordinates (x; y) and click on left mouse quickly.
    """

    mouse.move(x, y)
    time.sleep(0.05)

    mouse.press(mouse.LEFT)
    time.sleep(0.05)
    mouse.release(mouse.LEFT)

# press and hold ESC to stop the loop
while not keyboard.is_pressed('ESC'):
    # move and click on wish button
    move_and_press(wish_button['x'], wish_button['y'])
    time.sleep(0.25)

    # move to close button
    mouse.move(close_button['x'], close_button['y'])
    time.sleep(0.05)

    # skip animation
    for _ in range(5):
        mouse.press()
        time.sleep(0.05)
        mouse.release()

    # wait for the result of wish
    time.sleep(1.5)

    # close the result
    for _ in range(5):
        mouse.press()
        time.sleep(0.05)
        mouse.release()

    time.sleep(0.5)