import pgzrun, random

WIDTH=700
HEIGHT=700

def draw():
    screen.fill("black")
    width=WIDTH
    height=HEIGHT-200
    for i in range(40):
        blue=random.randint(0,255)
        red=random.randint(0,255)
        green=random.randint(0,255)
        box=Rect((0,0), (width, height))
        box.center=(350,350)
        screen.draw.rect(box, (red,green,blue))
        width-=10
        height+=10

def update():
    pass

pgzrun.go()
