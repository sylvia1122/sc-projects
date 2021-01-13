"""
File: draw_line.py
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Constant controls the size of the oval
OVALSIZE = 10

# Global Variable
window = GWindow(width=800, height=800, title='draw line')
n = 0
x1 = 0
y1 = 0

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(sketch)


def sketch(mouse):
    """
    This program determines if it is the first time user click on the canvas.
    It will draw a circle at the place where user clicks for the first time,
    and will draw a line from the position of the first click to the one of second click.
    When user click at the second time, the previous circle will disappear.
    """
    global n, x1, y1
    if n == 0:
        oval = GOval(OVALSIZE, OVALSIZE)
        n += 1
        window.add(oval, mouse.x-OVALSIZE/2, mouse.y-OVALSIZE/2)
        x1 = mouse.x
        y1 = mouse.y
    else:
        # look for the circle which appears according to the first click and remove it
        object = window.get_object_at(x1, y1)
        window.remove(object)
        line = GLine(x1, y1, mouse.x, mouse.y)
        window.add(line)
        n = 0






if __name__ == "__main__":
    main()
