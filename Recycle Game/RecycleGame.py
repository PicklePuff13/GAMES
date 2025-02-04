import pgzrun, random

WIDTH=700
HEIGHT=700

Levels=5
CLevel=1
GOver=False
GWin=False
Items=["bag.png","bottle.png","crisps.png","tub.png"]
Combination=[]
Starts=11

#function for creating items
def itemmaker(L):
    New=[]
    Options=["leaf.png"]+random.choices(Items,k=L)
    for i in Options:
        Object=Actor(i)
        New.append(Object)
    gap_size=WIDTH/(len(New)+1)
    for index, item in enumerate(New):
        item.x=(index+1)*gap_size
        item.y=0
        animate(item,duration=Starts-CLevel,y=HEIGHT)
    return New

def update():
    global Combination, CLevel
    if len(Combination)==0:
        Combination=itemmaker(CLevel)

def draw():
    screen.blit("background.jpg",(0,0))
    if GWin==True:
        screen.blit("youwin.jpg",(0,0))
    else:
       for i in Combination:
          i.draw()

def on_mouse_down(pos):
    global Combination, CLevel, GWin
    for i in Combination:
        if i.collidepoint(pos):
            if "leaf" in i.image:
                if CLevel==Levels:
                    GWin=True
                else:
                    CLevel+=1
                    Combination.clear()

    
pgzrun.go()
