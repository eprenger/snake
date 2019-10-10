import turtle
import time
import random

# delay
delay = 0.1

# score
score = 0
high_score = 0

# screen setup
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)  # turns off screen updates

# snakehead
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 150)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center",
          font=("Courier", 24, "normal"))

# functions


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


# keyboard
win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_right, "d")
win.onkey(go_left, "a")

# main game loop
while True:
    win.update()

    # check for border collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # hiding segments
        for segment in segments:
            segment.goto(1000, 1000)

        # clear segments list
        del segments[:]

        # reset score
        score = 0

        # reset delay
        delay = 0.1

        pen.clear()
        pen.write("Score : {}  High Score: {}".format(score, high_score),
                  align="center", font=("Courier", 24, "normal"))

    # checking for collision with food
    if head.distance(food) < 20:
        # food moves to random place
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # shorten the delay
        delay -= 0.001

        # setting score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score : {}  High Score: {}".format(score, high_score),
                  align="center", font=("Courier", 24, "normal"))

    # add segments
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)

    # move end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # move segment 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # check for body collisions
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hiding segments
            for segment in segments:
                segment.goto(1000, 1000)

            # clear segments list
            del segments[:]

            # reset score
            score = 0

            # reset delay
            delay = 0.1

    time.sleep(delay)

win.mainloop()
