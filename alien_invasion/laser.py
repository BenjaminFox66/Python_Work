import pygame
from pygame.sprite import Sprite

class Laser(Sprite):
    '''镭射激光'''
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        # 绘制激光内部的结构
        self.color_out = ai_settings.laser_color_out
        self.color_mid = ai_settings.laser_color_mid
        self.color_in = ai_settings.laser_color_in
        self.rect = pygame.Rect(0, 0, ai_settings.laser_width_out, ai_settings.screen_height)
        self.rect_mid = pygame.Rect(0, 0, ai_settings.laser_width_mid, ai_settings.screen_height)
        self.rect_in = pygame.Rect(0, 0, ai_settings.laser_width_in, ai_settings.screen_height)
        self.base_out = ai_settings.base_width_out
        self.base_mid = ai_settings.base_width_mid
        self.base_in = ai_settings.base_width_in

        self.damage = ai_settings.laser_damage

    def update(self, ship):
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.top - self.base_mid
        self.rect_mid.centerx = ship.rect.centerx
        self.rect_mid.bottom = ship.rect.top - self.base_in
        self.rect_in.centerx = ship.rect.centerx
        self.rect_in.bottom = ship.rect.top

    def draw_laser(self, ship):
        pygame.draw.circle(self.screen, self.color_out, (ship.rect.centerx, ship.rect.top), self.base_out)
        pygame.draw.circle(self.screen, self.color_mid, (ship.rect.centerx, ship.rect.top), self.base_mid)
        pygame.draw.circle(self.screen, self.color_in, (ship.rect.centerx, ship.rect.top), self.base_in)
        pygame.draw.rect(self.screen, self.color_out, self.rect)
        pygame.draw.rect(self.screen, self.color_mid, self.rect_mid)
        pygame.draw.rect(self.screen, self.color_in, self.rect_in)
