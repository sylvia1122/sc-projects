"""
File: bouncing_ball.py
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
n = 3
ball = GOval(SIZE, SIZE)
gravity = GRAVITY



def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, START_X, START_Y)
    onmouseclicked(determine)

def determine(mouse):
    """
    This program checks if the ball is falling.
    Nothing will happen with mouse clicks while the ball is falling.
    """
    if ball.x == START_X:
        animation()
    else:
        pass

def animation():
    """
    The ball start falling after the mouse click.
    """
    global ball, gravity, n
    if n > 0:
    # the ball hasn't fallen over three times
        while ball.x < 800:
            # the ball is still on the canvas
            if gravity > 0:
                # when the ball is falling down
                if ball.y < 500-SIZE:
                # ball hasn't hit the floor
                    ball.move(VX, gravity)
                    pause(DELAY)
                    gravity += GRAVITY
                else:
                    # ball hits the floor
                    gravity = -gravity * REDUCE
            else:
                # when the ball is bouncing up
                ball.move(VX, gravity)
                pause(DELAY)
                gravity += GRAVITY
        # the ball falls out of the canvas
        n -= 1
        window.add(ball, START_X, START_Y)
    else:
        pass







def ball_fall():
    global ball, gravity













if __name__ == "__main__":
    main()
