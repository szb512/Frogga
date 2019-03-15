import turtle, random, math
screen = turtle.Screen()
screen.bgcolor("gray")
screen.delay(0)

sprite = turtle.Turtle()
sprite.penup()
sprite.speed(10)
sprite.ht()
player = sprite.clone()
player.shape("turtle")
player.color("green")
player.seth(90)
player.goto(0,-180)
player.st()

cars = []
for i in range(10):
    car = sprite.clone()
    car.shape('square')
    if i % 2:
        car.seth(0)
    else:
        car.seth(180)

    car.goto(random.randint(-200,200),-120+i*30)
    car.st()
    cars.append(car)
def update():
    player.fd(10)
    if(player.ycor() < 200):
        for car in cars:
            car.fd(10)
            if car.distance(player) < 20:
                break
            elif(car.xcor() < -200 or car.xcor() > 200):
                car.left(180)
        else:
            screen.ontimer(update, 50)

update()
def up():
    player.seth(90)

def down():
    player.seth(270)

def left():
    player.seth(180)

def right():
    player.seth(0)

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()
