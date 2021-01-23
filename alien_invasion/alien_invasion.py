import pygame
from button import Button
from game_stats import GameStats
from explosion import Explosion
from laser import Laser
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    #游戏初始化
    pygame.init()
    # 初始化混音器模块
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
    #创建屏幕对象
    ai_settings = Settings()
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(('奥特曼之保卫地球'))
    # 添加音效
    pygame.mixer.music.load('sound/bgm.mp3')
    # loops = -1，表示无限重复播放
    pygame.mixer.music.play(-1)
    # 创建Play按钮
    play_button = Button(ai_settings, screen, 'Play')
    # # 创建GameOver
    # GameOver_button = Button(ai_settings, screen, 'Game  Over!')

    # 创建飞船
    ship = Ship(ai_settings, screen)
    # 创建子弹组
    bullets = Group()
    # 创建冲击波组
    impacts = Group()
    # 创建激光
    laser = Group()
    laser.add(Laser(ai_settings, screen))
    # 创建敌人
    aliens = Group()
    # 创建爆炸
    explosions = [Explosion(ai_settings, screen) for _ in range(20)]

    # 创建一个时间对象,设置帧率为 200
    fps = 150
    Game_clock = pygame.time.Clock()

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, stats, play_button,
                        ship, aliens, bullets, impacts)
        if ship.hp <= 0:
            pygame.mouse.set_visible(True)
            stats.game_active = False
            ai_settings.speed_reset()
            ai_settings.speedchange()
            if stats.game_active:
                stats.reset_stats()

        if stats.game_active:
            if len(aliens) == 0:
                ai_settings.speedup()
                ai_settings.speedchange()
                gf.create_fleet(ai_settings, screen, ship, aliens)
            ship.update()
            hit = gf.update_alien(ai_settings, ship, aliens)
            if hit:
                aliens.empty()
                continue
            gf.update_impact(ai_settings, stats, aliens, impacts, explosions)
            gf.update_laser(ai_settings, stats, laser, ship, aliens, explosions)
            gf.update_bullets(ai_settings, stats, aliens, bullets, explosions)
            gf.update_explosion(explosions)

        # 调用Clock()类创建的对象中的tick()函数
        Game_clock.tick(fps)

        gf.update_screen(ai_settings, screen, stats, ship, aliens,
                         bullets, laser, impacts, explosions, play_button)


run_game()
