import pgzrun, random

WIDTH=700
HEIGHT=700

Message="Pickle Clicker"
Pickle=Actor("pickle character.png")

#defining draw
def draw():
    screen.fill("light green")
    Pickle.draw()
    screen.draw.text(Message, center=(350,100), fontsize=35)

#random position for the pickle
def position():
    Pickle.x=random.randint(0,700)
    Pickle.y=random.randint(0,700)

#update function
def update():
    pass

def on_mouse_down(pos):
    global Message
    if Pickle.collidepoint(pos):
        Message="You caught me!"
        position()
    else:
        Message="You missed!"

position()

clock.schedule_interval(position, 1)

pgzrun.go()