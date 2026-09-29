import pgzrun
import random
from time import time

start = time()
WIDTH = 800
HEIGHT = 400

SatelliteNames = []
Lines = []
next = 0
win = False
lose = False
limit = 20

for i in range(10):
    s = Actor("satellite")
    s.x = random.randint(0,700)
    s.y = random.randint(0,300)
    SatelliteNames.append(s)
def draw():
    global total

    screen.blit("background",(0,0))

    n = 1
    for i in SatelliteNames:
        i.draw()
        screen.draw.text(str(n),(i.x,i.y+16),color="red")
        n += 1

    for l in Lines:
        screen.draw.line(l[0],l[1],"green")

    if win == False and lose == False:
        total = time() - start

    screen.draw.text("Time: " + str(round(total,2)),
                     (25,25),color="white")

    if win:
        screen.draw.text("YOU WIN!",
                         center=(400,200),
                         fontsize=60,
                         color="green")

    if lose:
        screen.draw.text("TIME'S UP!",
                         center=(400,200),
                         fontsize=60,
                         color="red")

def update():
    global lose

    if time() - start >= limit and win == False:
        lose = True

def on_mouse_down(pos):
    global Lines,next,win

    if win or lose:
        return

    if SatelliteNames[next].collidepoint(pos):
        if next > 0:
            Lines.append((SatelliteNames[next-1].pos,
                          SatelliteNames[next].pos))
        next += 1

        if next == 10:
            win = True

    else:
        Lines = []
        next = 0

pgzrun.go()
