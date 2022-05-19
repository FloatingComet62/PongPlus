import pygame

class BaseEntity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Paddle(BaseEntity):
    def __init__(self, screen):
        self.width = 100
        self.height = 10
        self.screen = screen
        self.speed = 1
    
        super().__init__(screen.get_width() / 2 - self.width / 2, 5)
    
    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (self.x, self.y, self.width, self.height))
    
    def left(self):
        if self. x + self.width > 0:
            self.x -= self.speed
    
    def right(self):
        if self.x + self.width < self.screen.get_width():
            self.x += self.speed

class Ball(BaseEntity):
    def __init__(self, screen):
        self.radius = 10
        self.x_speed = 0.5
        self.y_speed = 0.5
        self.screen = screen

        super().__init__(screen.get_width() / 2, screen.get_height() / 2)
    
    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed
    
    def draw(self, paddle):
        self.move()
        pygame.draw.circle(self.screen, (255, 255, 255), (self.x, self.y), self.radius)

        # bouncing
        if (
            self.x + self.radius >= self.screen.get_width() or
            self.x - self.radius <= 0
        ):
            self.x_speed *= -1

        if (
            self.y + self.radius >= self.screen.get_height() or
            self.y - self.radius <= 0
        ):
            self.y_speed *= -1

        # paddle collision
        if (
            self.x + self.radius >= paddle.x and
            self.x - self.radius <= paddle.x + paddle.width
        ):
            if (
                self.y + self.radius >= paddle.y and
                self.y - self.radius <= paddle.y + paddle.height
            ):
                self.y_speed *= -1
                self.x_speed += 0.2
                self.y_speed += 0.2
        # end check
        if self.y - self.radius <= 0:
            return True
        else:
            return False
