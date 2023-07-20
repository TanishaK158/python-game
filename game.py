import turtle

# Functions
def move_paddle_left():
    x = paddle.xcor()
    if x > -350:
        x -= 40
    paddle.setx(x)

def move_paddle_right():
    x = paddle.xcor()
    if x < 350:
        x += 40
    paddle.setx(x)

def exit_game():
    screen.bye()

# Function for button click
def button_click(x, y):
    if -180 < x < 180 and -170 < y < -130:
        exit_game()

if __name__ == '__main__':
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Brick Breaker")
    screen.bgcolor("bisque")
    screen.setup(width=800, height=600)
    screen.tracer(0)

    # Paddle
    paddle = turtle.Turtle()
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=1, stretch_len=5)
    paddle.penup()
    paddle.goto(0, -250)

    # Ball
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball_radius = 10  # Radius of the ball
    ball.dx = 8  # Increase the speed in the x direction
    ball.dy = -8  # Increase the speed in the y direction

    # Bricks
    bricks = []
    brick_colors = ["PaleVioletRed4", "LightCoral", "LightPink3", "salmon"]
    

    for i in range(4):
        for j in range(-5, 6):
            brick = turtle.Turtle()
            brick.shape("square")
            brick.color(brick_colors[i])
            brick.shapesize(stretch_wid=1, stretch_len=2)
            brick.penup()
            brick.goto(j * 70, 200 - i * 30)
            bricks.append(brick)

    brick_count = len(bricks)
    print(len(bricks))
    # Score
    score = 0

    # Scoreboard
    scoreboard = turtle.Turtle()
    scoreboard.color("dark blue")
    scoreboard.penup()
    scoreboard.hideturtle()
    scoreboard.goto(0, 260)
    scoreboard.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Keyboard bindings
    screen.listen()
    screen.onkeypress(move_paddle_left, "Left")
    screen.onkeypress(move_paddle_right, "Right")
    screen.onkeypress(exit_game, "q")

    # Game loop
    while True:
        screen.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Check for collision with walls
        if ball.xcor() > 390 or ball.xcor() < -390:
            ball.dx *= -1
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.dy *= -1

        # Check for collision with paddle
        if (ball.ycor() < -240 and ball.ycor() > -250) and (ball.xcor() < paddle.xcor() + 50 and ball.xcor() > paddle.xcor() - 50):
            ball.dy *= -1

        # Check for collision with bricks
        for brick in bricks:
            if brick.distance(ball) < 40:
                brick.goto(2000, 2000)  # Move the brick off the screen
                score += 1
                scoreboard.clear()
                scoreboard.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
                brick_count -= 1
                ball.dy *= -1

        #check score
        n = 0
        for brick in bricks:
            if(brick.xcor() == 2000 and brick.ycor() == 2000):
                n += 1

        score = n
        brick_count = len(bricks) - n


        # Check for game over
        if brick_count == 0:
            scoreboard.goto(0, 0)
            scoreboard.write("You Won", align="center", font=("Courier", 24, "normal"))
            break

        # Check for ball touching the ground
        # if ball.ycor() < -290:
        #     scoreboard.goto(0, 0)
        #     scoreboard.write("Game Over", align="center", font=("Courier", 24, "normal"))
        #     break

    # Exit button
    exit_button = turtle.Turtle()
    exit_button.shape("square")
    exit_button.color("red")
    exit_button.shapesize(stretch_wid=2, stretch_len=6)
    exit_button.penup()
    exit_button.goto(0, -150)
    exit_button.write("Exit", align="center", font=("Courier", 24, "normal"))

    # Register button click event
    screen.onclick(button_click)

    turtle.mainloop()
