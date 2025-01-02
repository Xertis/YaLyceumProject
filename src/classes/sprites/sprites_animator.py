from pygame import image, surface, transform
from src.utils.nums_utils import nums
from src.utils.atlas_utils import atlas


class ANIMATOR:
    def __init__(self, sprites: tuple, is_atlas: False = False):
        self.sprites = sprites
        self.pos = ()
        self.current_sprite = 0

        if is_atlas:
            atlas_width, atlas_height = self.sprites.get_size()
            self.sprites = atlas.split(self.sprites, atlas_width, atlas_width)

    def place(self, pos, screen: surface.Surface, angle=0, is_static: bool = False):
        self.pos = pos
        sprite = self.sprites[self.current_sprite]

        if not is_static:
            self.current_sprite = nums.in_range(
                self.current_sprite + 1, 0, len(self.sprites)-1)

        rect = sprite.get_rect()

        rect.x = pos[0]
        rect.y = pos[1]

        sprite = transform.rotate(sprite, angle)
        screen.blit(sprite, rect)
