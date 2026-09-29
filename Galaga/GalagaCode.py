import pgzrun

WIDTH = 800
HEIGHT = 525

Galaga = Actor("galaga")
Galaga.x = 400
Galaga.y = 475

BulletList = []
BugList = []

direction = 1

# Create bugs
for j in range(3):
    for i in range(6):
        bug = Actor("bug")
        bug.x = 25 + (50 * i)
        bug.y = 25 + (45 * j)
        BugList.append(bug)


def draw():
    screen.fill("blue")

    if len(BugList) == 0:
        screen.fill("black")
        screen.draw.text("YOU WIN!",center=(WIDTH // 2, HEIGHT // 2),fontsize=60,color="white")
        return

    Galaga.draw()

    for bullet in BulletList:
        bullet.draw()

    for bug in BugList:
        bug.draw()


def update():
    global direction

    # Move player
    if keyboard.left:
        Galaga.x -= 5

    if keyboard.right:
        Galaga.x += 5

    Galaga.x = max(50, min(750, Galaga.x))

    # Move bullets
    for bullet in BulletList[:]:
        bullet.y -= 5

        if bullet.y < 0:
            BulletList.remove(bullet)
            continue

        for bug in BugList[:]:
            if bug.colliderect(bullet):
                BugList.remove(bug)
                if bullet in BulletList:
                    BulletList.remove(bullet)
                break

    # Move bugs
    if len(BugList) > 0:
        for bug in BugList:
            bug.x += 3 * direction

        rightmost = max(bug.x for bug in BugList)
        leftmost = min(bug.x for bug in BugList)

        if rightmost >= WIDTH - 10:
            direction = -1
            for bug in BugList:
                bug.y += 20

        elif leftmost <= 10:
            direction = 1
            for bug in BugList:
                bug.y += 20


def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor("bullet")
        bullet.x = Galaga.x
        bullet.y = Galaga.y - 35
        BulletList.append(bullet)


pgzrun.go()