import pgzrun, random

HEIGHT=750
import pgzrun, random

HEIGHT=750
WIDTH=850

Rabbit=Actor("bunny.png",pos=(100,600))
Bear=Actor("bear.png",pos=(100,450))
Fox=Actor("fox.png",pos=(100,300))
Tiger=Actor("tiger.png",pos=(100,150))
Animals=[Rabbit,Bear,Fox,Tiger]
AnimalsS=[]

#random speed for all animals
for a in Animals:
    speed=random.randint(2,7)
    AnimalsS.append (speed)

winner=None
gameover=False

def draw():
    screen.blit("junglebackdrop.jpg",(0,0))
    for i in Animals:
        i.draw()
    screen.draw.line((830,0),(830,750),"white")
    if gameover and winner:
        screen.draw.text("winner is "+str(winner),center=(425,30),fontsize=40,color="white")

def update():
    pass
    global winner, gameover
    if gameover:
        return
    for i in range(len(Animals)):
        Animals[i].x+=AnimalsS[i]
        if Animals[i].x>=830:
            winner=Animals[i].image.capitalize()
            gameover=True
            break


pgzrun.go()import pgzrun, random

HEIGHT=750
WIDTH=850

Rabbit=Actor("bunny.png",pos=(100,600))
Bear=Actor("bear.png",pos=(100,450))
Fox=Actor("fox.png",pos=(100,300))
Tiger=Actor("tiger.png",pos=(100,150))
Animals=[Rabbit,Bear,Fox,Tiger]
AnimalsS=[]

#random speed for all animals
for a in Animals:
    speed=random.randint(2,7)
    AnimalsS.append (speed)

winner=None
gameover=False

def draw():
    screen.blit("junglebackdrop.jpg",(0,0))
    for i in Animals:
        i.draw()
    screen.draw.line((830,0),(830,750),"white")
    if gameover and winner:
        screen.draw.text("winner is "+str(winner),center=(425,30),fontsize=40,color="white")

def update():
    pass
    global winner, gameover
    if gameover:
        return
    for i in range(len(Animals)):
        Animals[i].x+=AnimalsS[i]
        if Animals[i].x>=830:
            winner=Animals[i].image.capitalize()
            gameover=True
            break


pgzrun.go()WIDTH=850

Rabbit=Actor("bunny.png",pos=(100,600))
Bear=Actor("bear.png",pos=(100,450))
Fox=Actor("fox.png",pos=(100,300))
Tiger=Actor("tiger.png",pos=(100,150))
Animals=[Rabbit,Bear,Fox,Tiger]
AnimalsS=[]

#random speed for all animals
for a in Animals:
    speed=random.randint(2,7)
    AnimalsS.append (speed)

winner=None
gameover=False

def draw():
    screen.blit("junglebackdrop.jpg",(0,0))
    for i in Animals:
        i.draw()
    screen.draw.line((830,0),(830,750),"white")
    if gameover and winner:
        screen.draw.text("winner is "+str(winner),center=(425,30),fontsize=40,color="white")

def update():
    pass
    global winner, gameover
    for i in range(len(Animals)):
        Animals[i].x+=AnimalsS[i]
        if Animals[i].x>=830:
            winner=Animals[i].image.capitalize()
            gameover=True
            break


pgzrun.go()
