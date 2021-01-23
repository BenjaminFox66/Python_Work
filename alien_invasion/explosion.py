import pygame

class Explosion:
    '''爆炸效果'''
    def __init__(self, ai_settings, screen):
        self.screen = screen
        # 设置效果图片和音效
        self.image = pygame.image.load('images/explosion.png')
        self.rect = self.image.get_rect()
        self.visible = False
        self.stop_time = ai_settings.explosion_time
        self.stop = ai_settings.explosion_time

    def creat(self, x, y):
        # 显示时长与位置
        self.visible = True
        self.stop = self.stop_time
        self.rect.centerx = x
        self.rect.centery = y

    def update(self):
        self.stop -= 1
        if self.stop == 0:
            self.visible = False

    def display(self):
        # 显示图片
        if self.visible:
            self.screen.blit(self.image, self.rect)
