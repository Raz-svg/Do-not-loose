import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Bounce Game")

rect = pygame.Rect(600, 0, 50, 50)
rect1 = pygame.Rect(790, 790, 200, 10)
speed = [random.randint(5, 10), random.randint(5, 10)]

# Use default font (cross-platform compatible)
font = pygame.font.Font(None, 74)

end_message = font.render('Game Over', True, (255, 220, 0))
conti = font.render('Continue (↑)', True, (255, 220, 0))
exit_game = font.render('Exit (↓)', True, (255, 220, 150))

clock = pygame.time.Clock()
n = 0

def counter():
    global n
    n += 1

def game_over_screen():
    while True:
        screen.fill((0, 0, 0))
        screen.blit(end_message, (450, 75))
        screen.blit(conti, (450, 400))
        screen.blit(exit_game, (450, 500))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            return True
        elif keys[pygame.K_DOWN]:
            return False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Paddle movement
    if keys[pygame.K_LEFT]:
        rect1.x -= 15
    if keys[pygame.K_RIGHT]:
        rect1.x += 15

    rect1.x = max(0, min(1200 - rect1.width, rect1.x))

    rect.x += speed[0]
    rect.y += speed[1]

    if rect.top <= 0:
        speed[1] = -speed[1]
    if rect.left <= 0 or rect.right >= 1200:
        speed[0] = -speed[0]

    if rect.colliderect(rect1) and speed[1] > 0:
        rect.bottom = rect1.top
        speed[1] = -speed[1]
        counter()

    if rect.bottom >= 800:
        if game_over_screen():
            rect = pygame.Rect(random.randint(50, 1150), 0, 50, 50)
            rect1 = pygame.Rect(random.randint(10, 990), 790, 200, 10)
            speed = [random.randint(5, 10), random.randint(5, 10)]
            n = 0
        else:
            running = False

    screen.fill((0, 0, 0))
    counter1 = font.render(f"Score : {n}", True, (255, 220, 0))
    screen.blit(counter1, (10, 10))
    pygame.draw.rect(screen, (255, 200, 230), rect)
    pygame.draw.rect(screen, (255, 255, 255), rect1)

    pygame.display.flip()
    clock.tick(60)
