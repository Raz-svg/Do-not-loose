import pygame
import sys
import random


pygame.init()
screen = pygame.display.set_mode((1200, 800))
rect = pygame.Rect(600, 0, 50, 50)  # A 50x50 rectangle at (375, 275)
rect1=pygame.Rect(790, 790, 200, 10)
speed=[random.randint(15,20),random.randint(5,10)]

font = pygame.font.SysFont('Times New Roman', 74)
end_message = font.render('Game Over', True, (255, 220, 0))
conti=font.render('Continue', True, (255, 220, 0))
exit=font.render('Exit', True, (255, 220, 150))
clock = pygame.time.Clock()
# Main loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Move the rectangle down by 5 pixels every frame
    rect =rect.move(speed)



    rect.x+=speed[0]
    rect.y+=speed[1]

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect1.x -= random.randint(15,20)
    if keys[pygame.K_RIGHT]:
        rect1.x += random.randint(15,20)

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw the rectangle
    pygame.draw.rect(screen, (255, 200, 230), rect)
    pygame.draw.rect(screen, (255, 255, 255), rect1)

    pygame.display.update()
    if rect.top < 0 or rect.bottom > 800:
        speed[1] = -speed[1]
    if rect.left < 0 or rect.right > 1200:
        speed[0] = -speed[0]
    if rect.colliderect(rect1):
        speed[1] = -speed[1]
        speed[0] = -speed[0]


    if  rect1.left < 0 :
        rect1.x= 0
    if rect1.right > 1200:
        rect1.x=1200-rect1.width

    if rect.bottom >800:
        game_over = True
        screen.fill((0, 0, 0))  # Clear screen
        screen.blit(end_message, (450, 300))  # Display the message
        pygame.display.flip()  # Update the display

        pygame.time.wait(1000)  # Wait for 2 seconds  # Exit the game
        screen.fill((0, 0, 0))  # Clear screen
        screen.blit(conti, (450, 300))  # Display the message
        screen.blit(exit, (450, 400))
        pygame.time.wait(5000)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            rect = pygame.Rect(random.randint(50, 1150), 0, 50, 50)  # A 50x50 rectangle at (375, 275)
            rect1 = pygame.Rect(random.randint(10, 790), 790, 200, 10)
        elif keys[pygame.K_DOWN]:
            sys.exit()

        # Update display
    pygame.display.flip()
    pygame.time.Clock().tick(60)
