import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((1200, 800))
rect = pygame.Rect(600, 0, 50, 50)  # A 50x50 rectangle at (600, 0)
rect1 = pygame.Rect(790, 790, 200, 10)
speed = [random.randint(5, 25), random.randint(5, 25)]

font = pygame.font.SysFont('Times New Roman', 74)
end_message = font.render('Game Over', True, (255, 220, 0))
conti = font.render('Continue', True, (255, 220, 0))
exit_game = font.render('Exit', True, (255, 220, 150))

clock = pygame.time.Clock()
n = 0  # Score counter


def counter():
    global n
    n += 1


# Function to handle the game over screen
def game_over_screen():
    while True:
        screen.fill((0, 0, 0))
        screen.blit(end_message, (450, 75))
        screen.blit(conti, (450, 400))
        screen.blit(exit_game, (450, 500))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:  # Restart the game
            return True
        elif keys[pygame.K_DOWN]:  # Exit the game
            pygame.quit()
            sys.exit()


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the rectangle
    rect = rect.move(speed)
    rect.x += speed[0]
    rect.y += speed[1]

    # Handle player input for moving the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect1.x -= random.randint(15, 20)
    if keys[pygame.K_RIGHT]:
        rect1.x += random.randint(15, 20)

    # Keep the paddle within the screen bounds
    if rect1.left < 0:
        rect1.x = 0
    if rect1.right > 1200:
        rect1.x = 1200 - rect1.width

    # Ball collision with the walls
    if rect.top < 0 or rect.bottom > 800:
        speed[1] = -speed[1]
    if rect.left < 0 or rect.right > 1200:
        speed[0] = -speed[0]

    # Ball collision with the paddle and update score
    if rect.colliderect(rect1):
        speed[1] = -speed[1]
        counter()

    # Clear screen
    screen.fill((0, 0, 0))

    # Render and display the updated score
    counter1 = font.render(f"Score : {n}", True, (255, 220, 0))
    screen.blit(counter1, (10, 10))

    # Draw the ball and the paddle
    pygame.draw.rect(screen, (255, 200, 230), rect)
    pygame.draw.rect(screen, (255, 255, 255), rect1)

    # Check for game over condition
    if rect.bottom > 800:
        if game_over_screen():
            # Reset positions if the game is restarted
            rect = pygame.Rect(random.randint(50, 1150), 0, 50, 50)
            rect1 = pygame.Rect(random.randint(10, 790), 790, 200, 10)
            speed = [random.randint(15, 20), random.randint(5, 10)]
            n = 0  # Reset score
        else:
            running = False

    # Update display
    pygame.display.flip()
    clock.tick(60)