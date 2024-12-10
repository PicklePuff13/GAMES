import random, pgzrun, time

WIDTH=1000
HEIGHT=700

#variables
Stars= []
Lines= []
Next_Star= 0
Total_Stars=8
Start_Time= 0
Middle_Time= 0
End_Time= 0

def starmaker():
    for i in range(8):
        Star=Actor("star.png")
        Star.pos=random.randint(650,50),random.randint(650,50)
        Stars.apend(Star)
    Start_Time=time.time()

def draw():
    screen.blit("galaxy bg.jpg",(0,0))
    for a in Stars:
        a.draw()

def update():
    pass

starmaker()

pgzrun.go()
