from turtle import Turtle, Screen
import time
import random

# Initializing variables
points = 0
best_points = 0
title = "Python SnakeGame"
body_parts = []

# Screen settings
screen = Screen()
screen.bgcolor("green")
screen.title(title)
screen.setup(width=600, height=600)
screen.tracer(False)
screen.register_shape("apple.gif")
screen.listen()

# Object creating
head = Turtle("square")
score_sign = Turtle()
apple = Turtle("apple.gif")

# International object template
def set_object(object, color, x, y):
    object.penup()
    object.color(color)
    object.goto(x, y)

# Head settings
set_object(head, "yellow", 0, 0)
head.shapesize(1)
head.direction = "stop"

# Score sign settings
set_object(score_sign, "white", 0, 265)
score_sign.hideturtle()
score_sign.write(f"Points: {points}  Highest: {best_points}", align="center", font=("Calibri", 18))

# Apple settings
set_object(apple, "red", random.randint(-280, 280), random.randint(-280, 280))

# ========== COLLISION CHECKING FUNCTIONS ==========
def check_apple(points):
    if head.distance(apple) < 25:
        points += 1
        screen.title(f"Python SnakeGame | Points: {points}")
        apple.goto(random.randint(-280, 280), random.randint(-280, 280))

        # Body parts creating
        new_body_part = Turtle("square")
        new_body_part.color("blue")
        new_body_part.penup()
        body_parts.append(new_body_part)
    return points

def check_border(points):
    if head.xcor() > 275 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -275:   # <--------- Right and bottom border were little odd dont know why
        points = 0
        screen.title(f"Python SnakeGame | Points: {points}")
        time.sleep(2)
        head.direction = "stop"
        head.goto(0, 0)

        # Body parts clearance
        for one_body_part in body_parts:
                one_body_part.goto(0, 2000)
        body_parts.clear()
    return points

def check_self(points):
    for one_body_part in body_parts:
        if head.distance(one_body_part) < 5:          
            points = 0
            screen.title(f"Python SnakeGame | Points: {points}")          
            time.sleep(2)
            head.direction = "stop"
            head.goto(0, 0)
                    
            # Body parts clearance
            for one_body_part in body_parts:
                    one_body_part.goto(0, 2000)
            body_parts.clear()
    return points

# ========== MOVE FUNCTIONS ==========
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 5)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 5)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 5)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 5)

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

    # ======== COLISIONS HANDLING ========
    points = check_self(points)
    points = check_border(points)
    points = check_apple(points)

    # Check best score
    if points > best_points:
        best_points = points

    score_sign.write(f"Points: {points}  Highest: {best_points}", align="center", font=("Calibri", 18))

    # ===== BODY PARTS MOVING =====
    if len(body_parts) > 0:
        body_parts[0].goto(head.xcor(), head.ycor())

    for i in range(len(body_parts) - 1, 0, -1):
        x = body_parts[i - 1].xcor()
        y = body_parts[i - 1].ycor()
        body_parts[i].goto(x, y)

    move()
    time.sleep(0.012)
