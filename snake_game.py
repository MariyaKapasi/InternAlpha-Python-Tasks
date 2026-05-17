import turtle
import random
import time

delay = 0.1
score = 0

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)

head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

def move():

    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

head.direction = "stop"

wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

while True:

    wn.update()

    if head.distance(food) < 20:

        x = random.randint(-250,250)
        y = random.randint(-250,250)

        food.goto(x,y)

        score += 10

        print("Score:", score)

    move()

    time.sleep(delay)

wn.mainloop()
