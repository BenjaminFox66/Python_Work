import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''表示某个外星人的类'''
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载外星人图像，并设置rect属性
        self.image = pygame.image.load('images/alien.png')
        # self.image = pygame.image.load('images/Gudon0.png')
        self.rect = self.image.get_rect()
        # 每个外星人最初都在屏幕左上附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储外星人的准确位置
        self.x = float(self.rect.x)

        self.max_hp = ai_settings.alien_max_hp
        self.hp = ai_settings.alien_max_hp

    def draw_hp(self):
        '''绘制外星人血条'''
        rect = pygame.Rect(self.rect.left, self.rect.bottom + 5, self.rect.width, 10)
        pygame.draw.rect(self.screen, (255, 255, 255), rect)
        rect = pygame.Rect(self.rect.left + 2, self.rect.bottom + 6, self.rect.width - 4, 8)
        pygame.draw.rect(self.screen, (0, 0, 0), rect)
        rect = pygame.Rect(self.rect.left + 2, self.rect.bottom + 6, (self.rect.width - 4) * self.hp / self.max_hp, 8)
        pygame.draw.rect(self.screen, (255, 0, 0), rect)

    def draw(self):
        '''在某个指定位置绘制外星人'''
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        '''如果外星人位于屏幕边缘，就返回True'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        '''向左或向右移动外星人'''
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
