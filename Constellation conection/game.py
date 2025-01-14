import random, pgzrun, time

WIDTH=700
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
    global Start_Time
    for i in range(8):
        Star=Actor("star.png")
        Star.pos=random.randint(50,650),random.randint(50,650)
        Stars.append(Star)
    Start_Time=time.time()

def draw():
    global End_Time
    screen.blit("galaxy bg.jpg",(0,0))
    number=1
    for a in Stars:
        a.draw()
        screen.draw.text(str(number),(a.pos[0],a.pos[1]))
        number+=1
    for i in Lines:
        screen.draw.line(i[0],i[1],"white")
    if Next_Star<Total_Stars:
        End_Time=time.time()-Start_Time
        screen.draw.text(str(round(End_Time,1)),(50,50))
    else:
        screen.draw.text(str(round(End_Time,1)),(50,50))

def update():
    pass

def on_mouse_down(pos):
    global Next_Star,Lines
    if Next_Star<Total_Stars:
        if Stars[Next_Star].collidepoint(pos):
            if Next_Star:
                Lines.append((Stars[Next_Star-1].pos,Stars[Next_Star].pos))
            Next_Star+=1

starmaker()

pgzrun.go()
