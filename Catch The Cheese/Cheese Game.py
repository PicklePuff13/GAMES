import pgzrun, random

WIDTH=700
HEIGHT=700

Mouse=Actor("mouse.png")
Cheese=Actor("cheese.png")

Mouse.pos=(525,650)

def draw():
    screen.blit("kitchen floor.jpg", (0,0))
    Mouse.draw()
    Cheese.draw()

def update():
    pass

pgzrun.go()

