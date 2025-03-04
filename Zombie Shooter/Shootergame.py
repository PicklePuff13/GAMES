import pgzrun, random

WIDTH=850
HEIGHT=560

bulletlist=[]
player=Actor("player.png")
player.pos=(420,530)
enemy=Actor("zombieenemy.png")
enemy.pos=(425,39)

def draw():
    screen.blit("backround.jpg", (0,0))
    player.draw()
    enemy.draw()
    for i in bulletlist:
      i.draw()

#space key for the bullet
def on_key_down(key):
    if key==keys.SPACE:
        bulletlist.append(Actor("bullet.png"))
        bulletlist[-1].x=player.x+35
        bulletlist[-1].y=player.y-30
    
def update():
    enemy.y+=2
    if enemy.y>=560:
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

pgzrun.go()
