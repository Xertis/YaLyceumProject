from pygame import image, surface, transform
import sys
import os


class LOADER:
    @staticmethod
    def load(path, size: tuple = None):

        base_path = ''
        if hasattr(sys, '_MEIPASS'):
            base_path = sys._MEIPASS
        else:
            base_path = os.getcwd()

        path = os.path.join(base_path, "res", "sprites", path)

        if os.path.exists(path):
            sprite = image.load(path)

            if not size:
                return sprite
            else:
                return transform.scale(sprite, size)

        else:
            return False

    @staticmethod
    def place(pos, sprite: surface.Surface, screen: surface.Surface, angle=0):
        rect = sprite.get_rect()

        rect.x = pos[0]
        rect.y = pos[1]

        sprite = transform.rotate(sprite, angle)
        screen.blit(sprite, rect)
