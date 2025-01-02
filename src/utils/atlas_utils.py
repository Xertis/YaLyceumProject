import pygame


class atlas:
    @staticmethod
    def split(atlas, width, height):

        if isinstance(atlas, str):
            atlas = pygame.image.load(atlas).convert_alpha()

        sprites = []
        atlas_width, atlas_height = atlas.get_size()

        for y in range(0, atlas_height, height):
            for x in range(0, atlas_width, width):

                rect = pygame.Rect(x, y, width, height)

                sprite = atlas.subsurface(rect)
                sprites.append(sprite)

        return sprites
