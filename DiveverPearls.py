import pgzrun
import random
from time import time

start = time()
end_time = 0
finished = False

WIDTH = 800
HEIGHT = 400

Pearls = []
Lines = []
next_pearl = 0

# Create 10 pearls
for i in range(10):
    p = Actor("pearl")
    p.x = random.randint(50, 750)
    p.y = random.randint(50, 350)
    Pearls.append(p)

# Diver starts at the first pearl
diver = Actor("diver")
diver.pos = (50, 200)

def draw():
    screen.blit("ocean", (0, 0))

    # Draw pearls
    n = 1
    for pearl in Pearls:
        pearl.draw()
        screen.draw.text(str(n),
                         (pearl.x, pearl.y + 20),
                         color="white")
        n += 1

    # Draw collection path
    for line in Lines:
        screen.draw.line(line[0], line[1], "yellow")

    diver.draw()

    # Timer
    if finished == False:
        total = time() - start
    else:
        total = end_time

    screen.draw.text("Time: " + str(round(total, 2)),(20, 20),color="white")

    # Finished message
    if next_pearl == 10:
        screen.draw.text("All Pearls Collected!",center=(400, 50),color="gold",fontsize=50)

def update():
    pass

def on_mouse_down(pos):
    global next_pearl, Lines, finished, end_time

    if next_pearl < len(Pearls):

        # Correct pearl clicked
        if Pearls[next_pearl].collidepoint(pos):

            diver.pos = Pearls[next_pearl].pos

            if next_pearl > 0:
                Lines.append((Pearls[next_pearl - 1].pos,Pearls[next_pearl].pos))

            next_pearl += 1

            if next_pearl == 10:
                end_time = time() - start
                finished = True

        # Wrong pearl clicked
        else:
            Lines = []
            next_pearl = 0
            diver.pos = (50, 200)

pgzrun.go()