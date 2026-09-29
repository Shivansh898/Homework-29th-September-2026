import pgzrun
from time import sleep

WIDTH = 800
HEIGHT = 525

Galaga = Actor("galaga")
Galaga.x = 400
Galaga.y = 475

print("Welcome to Galaga...")
sleep(3.5)

print("1) Easy 2) Medium 3) Hard")
UserInput = int(input("Enter your option: "))

game = False
n = 0
game_over = False
score = 0
BulletList = []
BugList = []

y = 15
d = 3
direction = 1

if UserInput == 1:
    y += 15
    game = True
    n += 6

elif UserInput == 2:
    y += 2
    d += 0.5
    game = True
    n += 7

elif UserInput == 3:
    y += 28
    d += 1
    game = True
    n += 8

else:
    print("Invalid Choice")

# Create bugs
if game:
    for j in range(6):
        for i in range(n):
            bug = Actor("bug")
            bug.x = 25 + (50 * i)
            bug.y = 25 + (45 * j)
            BugList.append(bug)


def draw():
    if game:

        if game_over:
            screen.fill("red")
            screen.draw.text(
                "GAME OVER",
                center=(WIDTH // 2, HEIGHT // 2 - 40),
                fontsize=60,
                color="white"
            )

            screen.draw.text(
                f"Final Score: {score}",
                center=(WIDTH // 2, HEIGHT // 2 + 30),
                fontsize=40,
                color="yellow"
            )
            return

        if len(BugList) == 0:
            screen.fill("black")

            screen.draw.text("YOU WIN!",center=(WIDTH // 2, HEIGHT // 2 - 40),fontsize=60,color="white")

            screen.draw.text(f"Final Score: {score}",center=(WIDTH // 2, HEIGHT // 2 + 30),fontsize=40,color="yellow")
            return

        screen.fill("blue")

        # Draw score
        screen.draw.text(f"Score: {score}",topleft=(10, 10),fontsize=35,color="white")

        Galaga.draw()

        for bullet in BulletList:
            bullet.draw()

        for bug in BugList:
            bug.draw()


def update():
    global direction, game_over, y, d, score

    if game:

        if game_over:
            return

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

                    # Add score
                    score += 10

                    if bullet in BulletList:
                        BulletList.remove(bullet)

                    break

        # Move bugs
        if len(BugList) > 0:

            for bug in BugList:
                bug.x += d * direction

            rightmost = max(bug.x for bug in BugList)
            leftmost = min(bug.x for bug in BugList)

            if rightmost >= WIDTH - 10:
                direction = -1

                for bug in BugList:
                    bug.y += y

            elif leftmost <= 10:
                direction = 1

                for bug in BugList:
                    bug.y += y

            # Game over check
            for bug in BugList:
                if bug.y >= Galaga.y - 20:
                    game_over = True


def on_key_down(key):
    if game:

        if key == keys.SPACE:
            bullet = Actor("bullet")
            bullet.x = Galaga.x
            bullet.y = Galaga.y - 35

            BulletList.append(bullet)


if game:
    pgzrun.go()