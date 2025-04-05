import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1200, 800))
rect = pygame.Rect(600, 0, 50, 50)
rect1 = pygame.Rect(790, 790, 200, 10)
speed = [random.randint(5, 25), random.randint(5, 25)]

font = pygame.font.SysFont('Times New Roman', 48)
end_message = font.render('Game Over', True, (255, 220, 0))
conti = font.render('Press ↑ to Continue', True, (255, 220, 0))
exit_game = font.render('Press ↓ to Exit', True, (255, 220, 150))

clock = pygame.time.Clock()
n = 0
game_over = False


def counter():
    global n
    n += 1


def reset_game():
    global rect, rect1, speed, n, game_over
    rect = pygame.Rect(random.randint(50, 1150), 0, 50, 50)
    rect1 = pygame.Rect(random.randint(10, 790), 790, 200, 10)
    speed = [random.randint(15, 20), random.randint(5, 10)]
    n = 0
    game_over = False


running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if game_over:
        screen.blit(end_message, (450, 75))
        screen.blit(conti, (400, 400))
        screen.blit(exit_game, (400, 500))

        if keys[pygame.K_UP]:
            reset_game()
        elif keys[pygame.K_DOWN]:
            running = False
    else:
        # Move the ball
        rect = rect.move(speed)
        rect.x += speed[0]
        rect.y += speed[1]

        # Paddle control
        if keys[pygame.K_LEFT]:
            rect1.x -= 15
        if keys[pygame.K_RIGHT]:
            rect1.x += 15

        # Paddle bounds
        rect1.x = max(0, min(1200 - rect1.width, rect1.x))

        # Bounce
        if rect.top < 0 or rect.bottom > 800:
            speed[1] = -speed[1]
        if rect.left < 0 or rect.right > 1200:
            speed[0] = -speed[0]

        if rect.colliderect(rect1):
            speed[1] = -speed[1]
            counter()

        # Game Over trigger
        if rect.bottom >= 800:
            game_over = True

        # Draw
        counter1 = font.render(f"Score: {n}", True, (255, 220, 0))
        screen.blit(counter1, (10, 10))
        pygame.draw.rect(screen, (255, 200, 230), rect)
        pygame.draw.rect(screen, (255, 255, 255), rect1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
