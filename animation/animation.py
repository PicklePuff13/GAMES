import pgzrun,random,itertools

HEIGHT=750
WIDTH= 750

cheeseblock=Actor("squarecheese.png")
cheeseblock.pos=80,80
mouse=Actor("mouse.png")
mouse.pos=375,375

def draw():
    screen.blit("background.jpeg", (0,0))
    cheeseblock.draw()
    mouse.draw()


def update():
    pass

pgzrun.go()