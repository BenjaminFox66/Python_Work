import pygame


class Settings:
    """储存游戏设置的类"""
    def __init__(self):
        self.font = pygame.font.Font('font/simhei.ttf', 20)
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        # 背景图片
        self.background = pygame.image.load("images/background.jpeg")

        self.explosion_time = 40

        self.base_speed = 1.0

        # 飞船属性
        self.ship_max_hp = 400.0
        self.ship_speed_factor = 1.5
        # 敌人属性
        self.alien_point = 50
        self.alien_max_hp = 160.0
        self.alien_speed_factor = 1.8
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        # 子弹属性
        self.bullet_damage = 60.0
        self.bullet_speed_factor = 2.0
        self.max_magazine = 30
        self.reload_speed = 5.0
        # 冲击波属性
        self.impact_damage = 4.0
        self.impact_speed_factor = 4.0
        self.colddown_speed = 2.0
        # 激光属性
        self.laser_damage = 1.5
        self.max_energy = 1000.0
        self.charge_speed = 2.0
        self.spend_speed = 6.0

        self.laser_color_out = (255, 0, 0)
        self.laser_width_out = 20
        self.base_width_out = 15
        self.laser_color_mid = (255, 255, 0)
        self.laser_width_mid = 14
        self.base_width_mid = 9
        self.laser_color_in = (255, 255, 255)
        self.laser_width_in = 6
        self.base_width_in = 3

    def speedchange(self):
        # 飞船属性
        self.ship_speed_factor = 1.5 * self.base_speed
        # 敌人属性
        self.alien_point = int(50 * self.base_speed)
        self.alien_speed_factor = 1.8 * self.base_speed
        self.fleet_drop_speed = 10.0 * self.base_speed
        # 子弹属性
        self.bullet_speed_factor = 2.0 * self.base_speed
        self.reload_speed = 5.0 * self.base_speed
        # 冲击波属性
        self.colddown_speed = 2.0 * self.base_speed
        # 激光属性
        self.charge_speed = 2.0 * self.base_speed

    def speedup(self):
        self.base_speed *= 1.05

    def speed_reset(self):
        self.base_speed = 1.0
