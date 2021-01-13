"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

this program is a breakout game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    """
    This program is a break out game. The player has to control the paddle by moving the mouse to
    breakout all bricks on canvas with only three chances. If the ball falls out of the canvas, the player will
    loose one chance.
    """
    num_lives = NUM_LIVES
    graphics = BreakoutGraphics()
    while num_lives > 0 and graphics.brick_n < (graphics.brick_cols*graphics.brick_rows):
        pause(FRAME_RATE)
        graphics.ball.move(graphics.dx, graphics.dy)
        if graphics.ball.y > graphics.window.height-graphics.ball.height:
            # ball move out of the canvas
            graphics.reset_ball()
            graphics.dx = 0
            graphics.dy = 0
            num_lives -= 1
        elif graphics.check_for_collision():
            graphics.dx = -graphics.dx
            graphics.dy = -graphics.dy
        else:
            if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width-graphics.ball.width:
                graphics.dx = -graphics.dx
            if graphics.ball.y <= 0:
                graphics.dy = -graphics.dy
    pass









if __name__ == '__main__':
    main()
