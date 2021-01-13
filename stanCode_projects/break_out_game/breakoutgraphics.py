"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).
BRICK_N = 0            # Number of the vanished bricks.

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 brick_n = BRICK_N, title='Breakout'):
        """
        this program can create a canvas, a paddle, a ball, and bricks.
        """
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_n = brick_n
        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (self.window.width-self.paddle.width)/2,
                        self.window.height-self.paddle.height-paddle_offset)

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius, ball_radius)
        self.ball.filled = True
        self.window.add(self.ball, (self.window.width-ball_radius)/2, (self.window.height-ball_radius)/2)

        # Default initial velocity for the ball.
        self.dx = 0
        self.dy = 0

        # Initialize our mouse listeners.
        onmousemoved(self.move_paddle)
        onmouseclicked(self.determine)

        # Draw bricks. And the color of bricks will change depending on the rows of bricks.
        brick_x = 0
        brick_y = brick_offset
        color_order = ['red', 'orange', 'yellow', 'green', 'blue']
        color_n = brick_rows//5   # 5 for 5 colors
        color = 0
        n_rows = brick_rows
        while n_rows > 0:
            if color_n > 0:
                color_n -= 1
            else:
                color_n = brick_rows//5-1
                if color < 4:
                    color += 1
                else:
                    color = 0
            for i in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = color_order[color]
                self.brick.color = color_order[color]
                self.window.add(self.brick, brick_x, brick_y)
                brick_x += (brick_width+brick_spacing)
            brick_y += (brick_height+brick_spacing)
            brick_x = 0
            n_rows -= 1
        pass

    def move_paddle(self, mouse):
        """
        This program can move the paddle by tracking the route of the mouse.
        Paddle won't move out of the canvas.
        """
        if self.paddle.width/2 <= mouse.x <= self.window.width-(self.paddle.width/2):
            self.paddle.x = mouse.x-(self.paddle.width/2)
        elif mouse.x < self.paddle.width/2:
            self.paddle.x = 0
        elif mouse.x > self.window.width-(self.paddle.width/2):
            self.paddle.x = self.window.width-self.paddle.width

    def set_ball_v(self):
        """
        This program set a new speed of the ball by random.
        """
        self.dy = INITIAL_Y_SPEED
        self.dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.dx = -self.dx

    def reset_ball(self):
        """
        This program reset the ball in the middle of the window.
        """
        self.ball.x = (self.window.width-self.ball.width)/2
        self.ball.y = (self.window.height-self.ball.height)/2

    def determine(self, mouse):
        """
        This program can determine if the ball is moving now.
        Mouse click won't work if the ball is moving.
        """
        if self.ball.x == (self.window.width-self.ball.width)/2 \
                and self.ball.y == (self.window.height-self.ball.height)/2:
            self.set_ball_v()
        else:
            pass

    def check_for_collision(self):
        """
        This program can determine what kind of object the ball hits.
        If the ball hits a brick, the brick will be vanished.
        If the ball hits the paddle, the speed and direction of the ball will be changed.
        """
        obj_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        obj_2 = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
        obj_3 = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height)
        obj_4 = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height)
          # start from 0
        while True:
            if obj_1 is not None:
                obj_x = obj_1.x
                obj_y = obj_1.y
                break
            elif obj_2 is not None:
                obj_x = obj_2.x
                obj_y = obj_2.y
                break
            elif obj_3 is not None:
                obj_x = obj_3.x
                obj_y = obj_3.y
                break
            elif obj_4 is not None:
                obj_x = obj_4.x
                obj_y = obj_4.y
                break
            else:
                return False
        maybe_brick = self.window.get_object_at(obj_x, obj_y)
        if maybe_brick is not self.paddle:
            self.window.remove(maybe_brick)
            self.brick_n += 1
        elif maybe_brick is self.paddle:
            self.set_ball_v()
        return True






