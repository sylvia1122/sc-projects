"""
File: my_drawing.py
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GLine
from campy.graphics.gcolor import GColor
from campy.graphics.gwindow import GWindow
import random


# Global Variable
w = GWindow(width=1200, height=800, title='sunset')


def main():
    """
    this program draws the scene of sunset
    to show how i wish to have a holiday
   """
    sky()
    ocean()
    sun()
    wave()
    sun_shadow()
    human()
    birds()

def birds():
    """
    this program draws 3 to 5 birds in the sky by random
    """
    n = random.randint(3, 5)
    for i in range(n):
        x = random.randint(0, w.width)
        y = random.randint(0, 300)
        size = random.randint(10, 30)
        l_wing = GLine(x, y, x-size, y-size/2)
        r_wing = GLine(x, y, x+size, y-size/2)
        w.add(l_wing)
        w.add(r_wing)

def wave():
    """
    this program draws waves on the surface of the ocean by random
    """
    for i in range(20):
        x = random.randint(0, w.width)
        y = random.randint(321, w.height)
        line = GLine(x, y, x+120, y)
        line.color = 'lightslategrey'
        w.add(line)

def human():
    """
    this program draws a person who imagines that he was on the vacation
    """
    head = GOval(120, 120)
    head.filled = True
    head.fill_color = GColor(38, 38, 38)
    head.color = GColor(38, 38, 38)
    w.add(head, 600-120/2, 520)

    body = GOval(150, 240)
    body.filled = True
    body.fill_color = GColor(38, 38, 38)
    body.color = GColor(38, 38, 38)
    w.add(body, 600 - 150 / 2, 640)

def sun_shadow():
    """
    this program draws the reflection of the sun
    """
    x = 603-360/4
    y = 323
    line_r = 190
    line_g = 130
    line_b = 0
    for i in range(20):
        line = GLine(x, y, x+360/2-6*(i+1), y)
        line.color = GColor(line_r, line_g, line_b)
        w.add(line)
        x += 3
        y += 3
        line_r -= 6
        line_g -= 3
        line_b += 3

def sun():
    """
    this program draws a sun
    """
    sun = GArc(180, 360, 0, 180)
    sun.filled = True
    sun.fill_color = GColor(255, 190, 0)
    sun.color = GColor(225, 190, 0)
    w.add(sun, 600-360/4, 319-360/4)

def sky():
    """
    this program draws the sky by gradient
    """
    x = 0
    y = 0
    sky_r = 185
    sky_g = 60
    sky_b = 20
    for i in range(40):
        rect = GRect(1200, 8)
        rect.filled = True
        rect.fill_color = GColor(sky_r, sky_g, sky_b)
        rect.color = GColor(sky_r, sky_g, sky_b)
        w.add(rect, x, y)
        y += 8
        sky_r += 1
        sky_g += 2
        if sky_b == 0:
            sky_b = 0
        else:
            sky_b -= 1

def ocean():
    """
    this program draws the ocean by gradient
    """
    x = 0
    y = 320
    ocean_r = 0
    ocean_g = 100
    ocean_b = 160
    for i in range(60):
        rect = GRect(1200, 8)
        rect.filled = True
        rect.fill_color = GColor(ocean_r, ocean_g, ocean_b)
        rect.color = GColor(ocean_r, ocean_g, ocean_b)
        w.add(rect, x, y)
        y += 8
        ocean_g -= 1
        ocean_b -= 1











if __name__ == '__main__':
    main()
