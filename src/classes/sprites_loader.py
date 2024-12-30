from pygame import image, surface, transform
import os

class LOADER:
    @staticmethod
    def load(path, size: tuple=None):
        path = os.path.join(os.getcwd(), "res", "sprites", path)

        if os.path.exists(path):
            sprite = image.load(path)

            if not size:
                return sprite
            else:
                return transform.scale(sprite, size)

        else:
            return False
        
    @staticmethod
    def place(pos, sprite: surface.Surface, screen: surface.Surface):
        rect = sprite.get_rect()

        rect.x = pos[0]
        rect.y = pos[1]

        screen.blit(sprite, rect)