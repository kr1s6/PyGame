from Settings import *
from Player import Player
class Level:
    def __init__(self):
        # ------------------------------SPRITE GROUPS----------------------------------------------#
        self.player_group = pygame.sprite.Group()
        self.hearts_group = pygame.sprite.Group()
        self.all_sprites = CameraGroup()
        self.front_sprites = FrontCameraGroup()
        self.collision_sprites = pygame.sprite.Group()
        self.pushable_tiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        # -------------------------------------PLAYER----------------------------------------------------#
        self.player = Player((250, HIGH - 180), [self.all_sprites, self.player_group], self.collision_sprites,
                             self.enemies, self.pushable_tiles)

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.SURFACE = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(0, 0)
        # ------------------------------LEVEL 1 GRAPHIC----------------------------------------------#
        self.background = pygame.image.load('../Assets/Level1/background_lvl1.png').convert()
        self.background = pygame.transform.scale_by(self.background, 8)
        self.background_rect = self.background.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        # ------------------------------PLAYER CENTERING----------------------------------------------#
        level_end_width = 8320
        if WIDTH/2 <= player.rect.centerx <= (level_end_width - WIDTH / 2):
            self.offset.x = player.rect.centerx - WIDTH/2
        if player.rect.centery <= HIGH/2:
            self.offset.y = player.rect.centery - HIGH/2
        # ------------------------------DRAWING GRAPHICS CENTERED ON PLAYER---------------------------#
        background_offset = self.background_rect.topleft
        self.SURFACE.blit(self.background, background_offset)

        for sprite in self.sprites():
            offset_rect = sprite.rect.copy()
            offset_rect.center -= self.offset
            self.SURFACE.blit(sprite.image, offset_rect)

class FrontCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.SURFACE = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(0, 0)

    def custom_draw(self, player):
        # ------------------------------PLAYER CENTERING----------------------------------------------#
        if player.rect.centerx >= WIDTH/2:
            self.offset.x = player.rect.centerx - WIDTH/2
        if player.rect.centery <= HIGH/2:
            self.offset.y = player.rect.centery - HIGH/2
        # ------------------------------DRAWING GRAPHICS CENTERED ON PLAYER---------------------------#
        for sprite in self.sprites():
            offset_rect = sprite.rect.copy()
            offset_rect.center -= self.offset
            self.SURFACE.blit(sprite.image, offset_rect)