import pygame
from snake import Snake

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Snake Byte')

snake = Snake()
clock = pygame.time.Clock()
move_interval = 1.0 / snake.speed
move_timer = 0.0
dt = 0  # delta time in seconds

gameOver = False


# game loop
while not gameOver:
    # poll for events
    # pygame.QUIT, user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    move_timer += dt

    screen.fill(pygame.Color(34, 40, 49))

    if move_timer >= move_interval:
        snake.move()
        move_timer -= move_interval

    # draw snake
    for i, section in enumerate(snake.body):
        x, y = section
        if i == 0:
            color = (238, 238, 238)
        else:
            color = (0, 173, 181)

        pygame.draw.rect(screen, color, [x*20, y*20, 20, 20])

    # handle direction change
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake.change_direction(pygame.Vector2(0, -1))
    elif keys[pygame.K_s]:
        snake.change_direction(pygame.Vector2(0, 1))
    elif keys[pygame.K_a]:
        snake.change_direction(pygame.Vector2(-1, 0))
    elif keys[pygame.K_d]:
        snake.change_direction(pygame.Vector2(1, 0))

    pygame.display.update()
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()