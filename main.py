import pygame
from snake import Snake

# --- CONSTANTS --- #
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
GRID_SIZE = 20

# Colors
COLOR_BACKGROUND = (34, 40, 49)
COLOR_HEAD = (238, 238, 238)
COLOR_BODY = (0, 173, 181)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Byte')

snake = Snake()
snake_speed = 15
clock = pygame.time.Clock()
move_interval = 1.0 / snake_speed
move_timer = 0.0
dt = 0  # delta time in seconds

game_over = False


# game loop
while not game_over:
    # poll for events
    # pygame.QUIT, user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    move_timer += dt

    screen.fill(pygame.Color(COLOR_BACKGROUND))

    if move_timer >= move_interval:
        snake.move()
        move_timer -= move_interval

    # draw snake
    for i, section in enumerate(snake.body):
        x, y = section
        if i == 0:
            color = COLOR_HEAD
        else:
            color = COLOR_BODY

        pygame.draw.rect(screen, color, [x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE])

    # handle direction change
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake.change_direction("UP")
    elif keys[pygame.K_s]:
        snake.change_direction("DOWN")
    elif keys[pygame.K_a]:
        snake.change_direction("LEFT")
    elif keys[pygame.K_d]:
        snake.change_direction("RIGHT")

    pygame.display.update()
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()
