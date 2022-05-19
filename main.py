import pygame
from objects import Paddle, Ball

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    windowColor = (120, 120, 255)
    running = True


    paddle = Paddle(screen)
    ball = Ball(screen)

    def end():
        ball.y_speed = 0
        ball.x_speed = 0
        paddle.speed = 0
        windowColor = (120, 0, 0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.left()
        elif keys[pygame.K_RIGHT]:
            paddle.right()

        screen.fill(windowColor)

        collision = ball.draw(paddle)
        if collision:
            end()
        paddle.draw()

        pygame.display.update()
        pygame.display.set_caption(f"PongPlus")