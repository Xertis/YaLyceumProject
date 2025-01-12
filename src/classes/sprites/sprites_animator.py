from pygame import image, surface, transform, time
from src.utils.nums_utils import nums
from src.utils.atlas_utils import atlas
from src.classes.sprites.sprites_loader import LOADER


class ANIMATOR:
    def __init__(self, sprites: tuple, frame_duration=0):
        self.sprites = sprites
        self.frame_duration = frame_duration
        self.current_sprite = 0
        self.last_frame_time = time.get_ticks()

        if isinstance(sprites, surface.Surface):
            atlas_width, atlas_height = self.sprites.get_size()
            self.sprites = atlas.split(self.sprites, atlas_width, atlas_width)

    def place(self, pos, screen: surface.Surface, angle=0, is_static: bool = False):
        current_time = time.get_ticks()
        sprite = self.sprites[self.current_sprite]

        if not is_static and (current_time - self.last_frame_time) >= self.frame_duration:
            self.current_sprite = nums.in_range(
                self.current_sprite + 1,
                0, 
                len(self.sprites)-1
            )

            self.last_frame_time = current_time

        LOADER.sprite.place(pos, sprite, screen, angle)