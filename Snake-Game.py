import turtle
import random
import time
#Screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("#6B6B6B")
window.setup(width=600, height=600)
window.tracer(0)
#Snake head
head = turtle.Turtle()
head.shape("square")
head.color("#0B470A")
head.penup()
head.goto(0,0)
#Snake body and score
body = []
score = 0
txt = turtle.Turtle()
txt.penup()
txt.hideturtle()
txt.color("Black")
txt.goto(-280,280)
#Grid
grid = turtle.Turtle()
grid.speed(0)
grid.color("#595959")
for x in range(-310, 311,20):
    grid.penup()
    grid.goto(x, 300)
    grid.pendown()
    grid.goto(x,-300)
for y in range(-310, 311, 20):
    grid.penup()
    grid.goto(300,y)
    grid.pendown()
    grid.goto(-300,y)
#Apple
apple = turtle.Turtle()
apple.shape("circle")
apple.color("#FB232A")
apple.penup()
def place_apple():
    apple_x = random.randrange(-280, 280, 20)
    apple_y = random.randrange(-280, 280, 20)
    apple.goto(apple_x,apple_y)
#Snake commands
key_pressed = False
def move():
    head.forward(20)
def move_up():
    global key_pressed
    if key_pressed == False:
        if head.heading() != 270:
            head.setheading(90)
            key_pressed = True
def move_down():
    global key_pressed
    if key_pressed == False:
        if head.heading() != 90:
            head.setheading(270)
            key_pressed = True
def move_right():
    global key_pressed
    if key_pressed == False:
        if head.heading() != 180:
           head.setheading(0)
           key_pressed = True
def move_left():
    global key_pressed
    if key_pressed == False:
        if head.heading() != 0:
            head.setheading(180)
            key_pressed = True
window.listen()
window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
continue_game = True
place_apple()
while continue_game:
    window.update()
    if head.distance(apple) < 19:
        score += 1
        place_apple()
        new_body = turtle.Turtle()
        new_body.shape("square")
        new_body.color("#0D4B0C")
        new_body.penup()
        new_body.goto(1000,1000)
        body.append(new_body)
        txt.clear()
        txt.write(f"Score: {score} ", align="left", font=("Arial", 12, "bold"))
    for i in range(len(body) -1, 0, -1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x,y)
    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x,y)
    time.sleep(0.1)
    key_pressed = False
    move()
    if head.xcor() > 295  or head.xcor() < -295 or head.ycor() > 295 or head.ycor() < -295:
        continue_game = False
        text = turtle.Turtle()
        text.color("red")
        text.penup()
        text.hideturtle()
        text.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
        window.exitonclick()
    for new_body in body[1:]:
        if head.distance(new_body) < 20:
            continue_game = False
            text = turtle.Turtle()
            text.color("red")
            text.penup()
            text.hideturtle()
            text.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
            window.exitonclick()
window.mainloop()
