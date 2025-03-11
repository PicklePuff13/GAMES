import pgzrun, random

WIDTH=850
HEIGHT=560

bulletlist=[]
playerscore=0
enemyscore=0
player=Actor("player.png")
player.pos=(420,530)
enemy=Actor("zombieenemy.png")
enemy.pos=(425,39)
youwin=False
win=""

def draw():
    if youwin:
        screen.blit("youwin.jpg",(0,0))
        if win=="enemy":
            screen.draw.text(str(win)+" wins",(300,450),color="red", fontsize=60)
        elif win=="player":
            screen.draw.text(str(win)+" wins",(300,450),color="darkgreen", fontsize=60)    
    else:        
        screen.blit("backround.jpg", (0,0))
        player.draw()
        enemy.draw()
        screen.draw.text("player's score = "+str(playerscore),(20,20),color="darkgreen")
        screen.draw.text("enemy's score = "+str(enemyscore),(680,20),color="red")
        for i in bulletlist:
         i.draw()

def Youwin(winner):
    global youwin, win
    youwin=True
    win=winner

#space key for the bullet
def on_key_down(key):
    if key==keys.SPACE:
        bulletlist.append(Actor("bullet.png"))
        bulletlist[-1].x=player.x+35
        bulletlist[-1].y=player.y-30
    
def update():
    global playerscore, enemyscore
    enemy.y+=2
    if enemy.y>=560:
        enemyscore=enemyscore+1
        enemy.y=0
        enemy.x=random.randint(20,830)
    if keyboard.left:
        player.x-=2
        if player.x<=20:
            player.x=20
    if keyboard.right:
        player.x+=2
        if player.x>=830:
            player.x=830
    if keyboard.a:
        enemy.x-=1
        if enemy.x<=20:
            enemy.x=20
    if keyboard.d:
        enemy.x+=1
        if enemy.x>=830:
            enemy.x=830
    for i in bulletlist:
        i.y-=3
        if i.colliderect(enemy):
            bulletlist.remove(i)
            enemy.y=0
            enemy.x=random.randint(20,830)
            playerscore=playerscore+1
    if playerscore==20:
        Youwin("player")
    if enemyscore==15:
        Youwin("enemy")

pgzrun.go()
