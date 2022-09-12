import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @chas")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

food2 = turtle.Turtle()
food2.speed(0)
food2.shape("circle")
food2.color("black")
food2.penup()
food2.goto(random.randint(-290, 290),random.randint(-290, 290))

food3 = turtle.Turtle()
food3.speed(0)
food3.shape("circle")
food3.color("purple")
food3.penup()
food3.goto(random.randint(-290, 290),random.randint(-290, 290))

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)


def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
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

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")



# Main game loop
while True:
    wn.update()
    if  head.distance(food) < 20:

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        food.goto(random.randint(-290, 290),random.randint(-290, 290))
        
    if  head.distance(food2) < 20:
        length = len(segments)
        
        for idx in range(length):
            if (idx >= length/2):
                a = segments.pop()
                a.color("green")

        food2.goto(random.randint(-290, 290),random.randint(-290, 290))
        
    if  head.distance(food3) < 20:
        
        length = len(segments)
        for idx in range(length):
            a = segments.pop()
            a.color("green")
        food3.goto(random.randint(-290, 290),random.randint(-290, 290))
    
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    
    if len(segments) >0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
        
    score = len(segments) * 10
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 20, "normal"))

    
    move()
        
    time.sleep(delay)

wn.mainloop()