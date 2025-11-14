import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
gameOver = False  # game loop control
dt = 0  # delta time in seconds since last frame


pygame.display.set_caption('Snake Byte')

# game loop
while not gameOver:
    # poll for events
    # pygame.QUIT, user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    screen.fill("grey")

    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()