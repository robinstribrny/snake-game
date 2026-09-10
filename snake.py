from turtle import Turtle, Screen
import turtle
import time
import random

# Initializing variables
points = 0
best_points = 0
title = "Python SnakeGame by Robin Stříbrný"

# Screen settings
screen = Screen()
screen.bgcolor("green")
screen.title(title)
screen.setup(width=600, height=600)
screen.tracer(False)
screen.register_shape("apple.gif")
screen.listen()

# Head settings
head = Turtle("square")
head.color("yellow")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Score sign settings
score_sign = Turtle()
score_sign.color("white")
score_sign.hideturtle()
score_sign.penup()
score_sign.goto(0, 265)
score_sign.write(f"Points: {points}  Highest: {best_points}", align="center", font=("Calibri", 18))

# Apple settings
apple = Turtle("apple.gif")
apple.shapesize(100)
apple.color("red")
apple.penup()
apple.goto(random.randint(-280, 280), random.randint(-280, 250))

# Body settings
body_parts = []

# ========== MOVE FUNCTIONS ==========
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 15)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 15)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 15)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 15)

def move_up():
    if head.direction == "down":
        return
    else:
        head.direction = "up"
def move_down():
    if head.direction == "up":
        return
    else:
        head.direction = "down"
def move_left():
    if head.direction == "right":
        return
    else:
        head.direction = "left"
def move_right():
    if head.direction == "left":
        return
    else:
        head.direction = "right"

# Key binding
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

# ================== MAIN GAME CYCLE ==================
while True:

    screen.update()
    score_sign.clear()
    if points > best_points:
        best_points = points
    score_sign.write(f"Points: {points}  Highest: {best_points}", align="center", font=("Calibri", 18))

    # ======== COLISIONS HANDLING ========
    if head.distance(apple) < 20:
        points += 1
        title = f"Python SnakeGame by Robin Stříbrný | Points: {points}     :)"
        screen.title(title)
        apple.goto(random.randint(-280, 280), random.randint(-280, 250))

        # "new_body_part" object creating and setting
        new_body_part = Turtle("square")
        new_body_part.color("blue")
        new_body_part.penup()
        body_parts.append(new_body_part)

    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        title = f"Python SnakeGame by Robin Stříbrný | Oopsie     :("
        points = 0
        screen.title(title)
        time.sleep(2)
        title = f"Python SnakeGame by Robin Stříbrný"
        screen.title(title)
        head.direction = "stop"
        head.goto(0, 0)
        
        # Body parts clearance
        for one_body_part in body_parts:
            one_body_part.goto(0, 2000)
        body_parts.clear()

    for one_body_part in body_parts:
        if head.distance(one_body_part) < 10:
            if points > best_points:
                best_points = points
            title = f"Python SnakeGame by Robin Stříbrný | Oopsie     :("
            points = 0
            screen.title(title)
            time.sleep(2)
            title = f"Python SnakeGame by Robin Stříbrný"
            screen.title(title)
            head.direction = "stop"
            head.goto(0, 0)
                    
            # Body parts clearance
            for one_body_part in body_parts:
                    one_body_part.goto(0, 2000)
            body_parts.clear()

    # ===== BODY PARTS STACKING =====
    for i in range(len(body_parts) - 1, 0, -1):
        x = body_parts[i - 1].xcor()
        y = body_parts[i - 1].ycor()
        body_parts[i].goto(x, y)

    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x, y)

    move()
    time.sleep(0.1)

screen.exitonclick()