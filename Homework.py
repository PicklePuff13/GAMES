import pgzrun, random, pygame

WIDTH=700
HEIGHT=700

def draw():
    screen.fill("black")
    width=WIDTH
    height=HEIGHT-200
    radius = 10
    for i in range(40):
        blue=random.randint(0,255)
        red=random.randint(0,255)
        green=random.randint(0,255)
        pygame.draw.circle(window, (red,green,blue), 0, radius, 2) #(r, g, b) is color, (x, y) is center, R is radius and w is the thickness of the circle border
        
        radius#=10

def update():
    pass

pgzrun.go()
