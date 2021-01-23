import pygame

class Ship:

    def __init__(self, ai_settings, screen):
        # 飞船属性
        self.screen = screen
        self.ai_settings = ai_settings
        # self.image = pygame.image.load('images/ship.png')
        self.image = pygame.image.load('images/Ace.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.max_hp = ai_settings.ship_max_hp
        self.hp = ai_settings.ship_max_hp
        # 飞船位置
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        # 弹仓
        self.max_magazine = ai_settings.max_magazine
        self.magazine = ai_settings.max_magazine
        self.reload_completion = 0
        self.reload_speed = ai_settings.reload_speed
        # 冲击波
        self.temperature = 0
        self.colddown_speed = ai_settings.colddown_speed
        # 激光
        self.max_energy = ai_settings.max_energy
        self.energy = ai_settings.max_energy
        self.charge_speed = ai_settings.charge_speed
        self.spend_speed = ai_settings.spend_speed
        self.ready_fire = False
        self.laser_fire = False

    def center_ship(self):
        '''让飞船在屏幕上居中'''
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)
        self.hp = self.max_hp
        self.temperature = 0
        self.reload_completion = 0
        self.magazine = self.max_magazine
        self.energy = self.max_energy

    def charge(self):
        if self.energy < self.max_energy:
            self.energy += self.charge_speed

    def filling(self):
        if self.magazine < self.max_magazine:
            self.reload_completion += self.reload_speed
            if self.reload_completion >= 1000:
                self.reload_completion = 0
                self.magazine += 1

    def colddown(self):
        if self.temperature > 0:
            self.temperature -= self.colddown_speed
            if self.temperature < 0:
                self.temperature = 0

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= 0.75 * self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 0.75 * self.ai_settings.ship_speed_factor

        self.rect.centerx = self.x
        self.rect.centery = self.y

        if self.ready_fire and self.energy >= 200:
            self.laser_fire = True
        elif not self.ready_fire or self.energy <= 0:
            self.laser_fire = False
        self.charge()
        self.filling()
        self.colddown()

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)
