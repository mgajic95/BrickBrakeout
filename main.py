import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Create paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Create ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Create bricks
bricks = []

for i in range(-200, 200, 50):
    for j in range(150, 250, 25):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color(random.choice(["red", "orange", "yellow", "green", "blue"]))
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.penup()
        brick.goto(i, j)
        bricks.append(brick)

# Function to move paddle left
def move_left():
    x = paddle.xcor()
    if x > -250:
        x -= 20
    paddle.setx(x)

# Function to move paddle right
def move_right():
    x = paddle.xcor()
    if x < 250:
        x += 20
    paddle.setx(x)

# Keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Main game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for collision with walls
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    # Check for collision with paddle
    if (ball.ycor() < -240 and ball.ycor() > -250) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.dy *= -1

    # Check for collision with bricks
    for brick in bricks:
        if (brick.ycor() - 12.5 < ball.ycor() < brick.ycor() + 12.5) and (brick.xcor() - 25 < ball.xcor() < brick.xcor() + 25):
            brick.goto(1000, 1000)  # Move brick off-screen
            bricks.remove(brick)
            ball.dy *= -1

    # Game over
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1
        for brick in bricks:
            brick.goto(1000, 1000)  # Move bricks off-screen
            bricks.remove(brick)

    # Check for win
    if not bricks:
        ball.goto(0, 0)
        ball.dx = 0
        ball.dy = 0
        paddle.goto(0, -250)
        break

    time.sleep(0.01)

screen.mainloop()
