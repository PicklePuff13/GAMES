import pgzrun, random

WIDTH=700
HEIGHT=700

Mouse=Actor("mouse.png")
Cheese=Actor("cheese.png")
GameOver=False
Score=0
Time=10

Mouse.pos=(525,650)

def draw():
    screen.blit("kitchen floor.jpg", (0,0))
    Mouse.draw()
    Cheese.draw()
    screen.draw.text("Score: " + str(Score), color="black", topleft=(250,50))
    if GameOver==True:
      screen.fill("black")
      screen.draw.text("Game Over, Score: " + str(Score), color="white", center=(300,350))

def position():
    Cheese.x=random.randint(0,700)
    Cheese.y=random.randint(0,700)

def GameisOver():
    global GameOver
    GameOver=True

def update():
    pass
    global Score
    if keyboard.left:
        Mouse.x=Mouse.x-7
    if keyboard.right:
        Mouse.x=Mouse.x+7
    if keyboard.up:
        Mouse.y=Mouse.y-7
    if keyboard.down:
        Mouse.y=Mouse.y+7
    
    if Mouse.colliderect(Cheese):
          position()
          Score+=1

clock.schedule(GameisOver, Time)

pgzrun.go()

