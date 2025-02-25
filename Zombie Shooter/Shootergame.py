import pgzrun, random

WIDTH=850
HEIGHT=560

player=Actor("player.png")
player.pos=(420,530)

def draw():
    screen.blit("backround.jpg", (0,0))
    player.draw()


pgzrun.go()