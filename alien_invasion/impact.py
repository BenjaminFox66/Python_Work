import pygame
from pygame.sprite import Sprite

class Impact(Sprite):
    # 冲击波
    def __init__(self, ai_settings, screen, ship):
        # 在飞船所处的位置创建一个子弹对象
        super().__init__()
        self.screen = screen
        # 设置冲击波图片和音效
        self.image_pro = pygame.image.load('images/impact.png')
        self.sound = pygame.mixer.Sound('sound/impact.wav')
        self.image = self.image_pro
        self.rect = self.image.get_rect()

        self.x = ship.rect.centerx
        self.height = self.rect.height
        self.width = self.rect.width

        self.rect.centerx = self.x
        self.rect.centery = ship.rect.top
        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.speed_factor = ai_settings.impact_speed_factor
        self.damage = ai_settings.impact_damage

    def update(self):
        self.width += int(self.speed_factor / 2)
        # self.image = smoothscale(self.image_pro, (self.width, self.height))
        self.rect = self.image.get_rect()
        # 更新表示子弹位置的小数值
        self.rect.centerx = self.x
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_impact(self):
        """在屏幕上绘制"""
        self.screen.blit(self.image, self.rect)
