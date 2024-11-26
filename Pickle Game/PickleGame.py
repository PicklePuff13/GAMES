import pgzrun, random

WIDTH=700
HEIGHT=700

Score=0
Message="Pickle Clicker"
Pickle=Actor("pickle character.png")

#defining draw
def draw():
    screen.fill("light green")
    Pickle.draw()
    screen.draw.text(Message, center=(350,100), fontsize=35)
    screen.draw.text(str(Score), center=(75, 625), fontsize=50)

#random position for the pickle
def position():
    Pickle.x=random.randint(0,700)
    Pickle.y=random.randint(0,700)

#update function
def update():
    pass

def on_mouse_down(pos):
    global Message, Score
    if Pickle.collidepoint(pos):
        Message="You caught me!"
        Score=(Score+1)
        position()
    else:
        Message="You missed!"
        Score=(Score-1)

position()

clock.schedule_interval(position, 2.5)

pgzrun.go()
