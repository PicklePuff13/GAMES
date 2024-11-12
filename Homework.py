from turtle import Screen
import pgzrun, random

WIDTH=700
HEIGHT=700

def draw():
    screen.fill("black")
    radius=350
    for i in range(40):
        blue=random.randint(0,255)
        red=random.randint(0,255)
        green=random.randint(0,255)
        screen.draw.circle((red,green,blue), (350,350), radius)
        radius-=10
       # screen.draw.circle

def update():
    pass

pgzrun.go()
