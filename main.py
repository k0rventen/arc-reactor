# Libs import
from touchio import TouchIn
import neopixel
import board
import time
import random

# I/O objects
ring = neopixel.NeoPixel(board.D0, 24, brightness=1, auto_write=False)
touch = TouchIn(board.A0)

# Variables
is_lit = True
r, g, b = 0, 0, 0
delta = 0

# Init
for i in range(0, 200, 2):
    ran = random.randint(0, 20)
    blue_value = int((i+ran)*1.2)
    ring.fill((i+ran, i+ran, blue_value if blue_value < 255 else 255))
    ring.show()
    time.sleep(.02-(i/10000))
r, g, b = i+ran, i+ran, blue_value if blue_value < 255 else 255


# Loopy
while True:

    # Breathing effect
    if is_lit:

        if delta == 80:
            step = -1
        elif delta == 0:
            step = 1
        delta += step

        ring.fill((r-delta, g-delta, b - delta))
        ring.show()
        time.sleep(.01)

    # Toggle the reactor with animation when the copper coil is touched
    if touch.value:

        # Toggle off
        if is_lit:
            ring.fill((200, 200, 240))
            ring.show()
            for i in range(200, 0, -4):
                ran = random.randint(0, 40)
                b = int((i+ran)*1.2)
                ring.fill((i+ran, i+ran, b if b < 255 else 255))
                ring.show()
                time.sleep(.02-(i/10000))
            is_lit = False
            ring.fill((0, 0, 0))
            ring.show()

        # Toggle On
        else:
            for i in range(0, 200, 2):
                ran = random.randint(0, 40)
                blue_value = int((i+ran)*1.2)
                ring.fill(
                    (i+ran, i+ran, blue_value if blue_value < 255 else 255))
                ring.show()
                time.sleep(.02-(i/10000))
            is_lit = True
            r, g, b = i+ran, i+ran, blue_value if blue_value < 255 else 255