import pgzrun, random

HEIGHT=750
WIDTH=850

Rabbit=Actor("bunny.png",pos=(100,600))
Bear=Actor("bear.png",pos=(100,450))
Fox=Actor("fox.png",pos=(100,300))
Tiger=Actor("tiger.png",pos=(100,150))
Animals=[Rabbit,Bear,Fox,Tiger]

def draw():
    screen.blit("junglebackdrop.jpg",(0,0))
    for i in Animals:
        i.draw()
    screen.draw.line((830,0),(830,750),"white")

def update():
    pass

pgzrun.go()