import pygame


class CONTROLLER:
    def __init__(self, radius, speed):
        self.radius = radius
        self.speed = speed

    def collision(self, pos):
        rect = pygame.Rect(
            pos[0] - self.radius,
            pos[1] - self.radius,
            self.radius * 2,
            self.radius * 2
        )

        return False  # Пока, обработка столкновений не работает, доработайте

    def snake_move(self, pos):
        keys = pygame.key.get_pressed()
        move_x, move_y = 0, 0

        if keys[pygame.K_a]:
            move_x = -self.speed
        if keys[pygame.K_d]:
            move_x = self.speed
        if keys[pygame.K_w]:
            move_y = -self.speed
        if keys[pygame.K_s]:
            move_y = self.speed

        if_collision = self.collision((move_x + pos[0], move_y + pos[1]))

        if not if_collision:
            pos[0] += move_x
            pos[1] += move_y

        return pos
