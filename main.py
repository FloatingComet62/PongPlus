import pygame
from objects import Paddle, Ball

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    running = True
    died = False
    ballSpeed = 0.5


    paddle = Paddle(screen)
    ball = Ball(screen, ballSpeed)
    score = 0

    def end():
        ball.y_speed = 0
        ball.x_speed = 0
        paddle.speed = 0
        return True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: paddle.left()
        elif keys[pygame.K_RIGHT]: paddle.right()

        if died:
            windowColor = (255, 0, 0)
            if keys[pygame.K_r]:
                ball.reset(screen)
                paddle.reset()
                died = False
                score = 0
        else:
            windowColor = (120, 120, 255)

        screen.fill(windowColor)

        collision = ball.draw(paddle, score)
        score = collision[1]
        if collision[0]: died = end()
        paddle.draw()

        pygame.display.update()
        pygame.display.set_caption(f"PongPlus: Your score is {score}")