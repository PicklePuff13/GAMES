import random, pgzrun, time

WIDTH=700
HEIGHT=700

#variables
Birds= []
Lines= []
Next_Bird= 0
Total_Birds=8
Start_Time= 0
Middle_Time= 0
End_Time= 0

def birdmaker():
    global Start_Time
    for i in range(8):
       Bird=Actor("bird.png")
       Bird.pos=random.randint(50,650),random.randint(50,650)
       Birds.append(Bird)
    Start_Time=time.time()

def draw():
    global End_Time
    screen.blit("forest bg.jpg",(0,0))
    number=1
    for a in Birds:
        a.draw()
        screen.draw.text(str(number),(a.pos[0],a.pos[1]))
        number+=1
    for i in Lines:
        screen.draw.line(i[0],i[1],"white")
    if Next_Bird<Total_Birds:
        End_Time=time.time()-Start_Time
        screen.draw.text(str(round(End_Time,1)),(50,50))
    else:
        screen.draw.text(str(round(End_Time,1)),(50,50))

def update():
    pass

def on_mouse_down(pos):
    global Next_Bird,Lines
    if Next_Bird<Total_Birds:
        if Birds[Next_Bird].collidepoint(pos):
            if Next_Bird:
                Lines.append((Birds[Next_Bird-1].pos,Birds[Next_Bird].pos))
            Next_Bird+=1

birdmaker()

pgzrun.go()
