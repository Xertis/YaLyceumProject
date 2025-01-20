from pygame import image, surface, transform, mixer
from pygame.font import Font
import sys
import os

def __get_path__(*path):
    base_path = ''
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.getcwd()
    
    return os.path.join(base_path, "res", '\\'.join(path))

class sprite:
    @staticmethod
    def load(path, size: tuple = None):

        path = __get_path__("sprites", path)

        if not os.path.exists(path):
            return False

        sprite = image.load(path)

        if not size:
            return sprite
        else:
            return transform.scale(sprite, size)
        
    @staticmethod
    def place(pos, sprite: surface.Surface, screen: surface.Surface, angle=0):
        rect = sprite.get_rect()

        sprite_width, sprite_height = sprite.get_size()
        
        rect.x = pos[0] - sprite_width // 2
        rect.y = pos[1] - sprite_height // 2

        sprite = transform.rotate(sprite, angle)
        screen.blit(sprite, rect)

class font:
    @staticmethod
    def load(path, size: int = None):

        path = __get_path__("fonts", path)

        if not os.path.exists(path):
            return False

        return Font(path, size)


class sound:
    @staticmethod
    def load(path):
        path = __get_path__("sounds", path)
        if not os.path.exists(path):
            return False
        return mixer.Sound(path)


class LOADER:
    sprite = sprite
    font = font
    sound = sound