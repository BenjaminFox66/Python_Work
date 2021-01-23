import sys
import pygame
from alien import Alien
from bullet import Bullet
from impact import Impact


def check_keydown_events(event, ai_settings, screen, ship, bullets, impacts):
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True

    elif event.key == pygame.K_x and ship.magazine:
        ship.magazine -= 1
        new_bullet = Bullet(ai_settings, screen, ship)
        new_bullet.sound.play()
        bullets.add(new_bullet)

    elif event.key == pygame.K_s and ship.temperature <= 6000:
        ship.temperature += 3000
        new_impact = Impact(ai_settings, screen, ship)
        new_impact.sound.play()
        impacts.add(new_impact)
    elif event.key == pygame.K_SPACE:
        pygame.mixer.Sound('sound/laser.wav').play()
        ship.ready_fire = True


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_SPACE:
        ship.ready_fire = False


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets, impacts):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, impacts)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, impacts, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, impacts, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        aliens.empty()
        bullets.empty()
        impacts.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def display_temperature(ai_settings, screen, ship):
    text = ai_settings.font.render('冲击热度:', 1, (255, 255, 255))
    screen.blit(text, (0, ai_settings.screen_height - 80))

    rect = pygame.Rect(0, ai_settings.screen_height - 60, 104, 20)
    pygame.draw.rect(screen, (255, 255, 255), rect)
    rect = pygame.Rect(2, ai_settings.screen_height - 58, 100, 16)
    pygame.draw.rect(screen, (0, 0, 0), rect)
    rect = pygame.Rect(2, ai_settings.screen_height - 58, ship.temperature / 90, 16)
    pygame.draw.rect(screen, (255, 0, 0), rect)
    rect = pygame.Rect(66, ai_settings.screen_height - 58, 2, 16)
    pygame.draw.rect(screen, (255, 255, 0), rect)


def display_energy(ai_settings, screen, ship):
    text = ai_settings.font.render('激光充能:', 1, (255, 255, 255))
    screen.blit(text, (0, ai_settings.screen_height - 120))

    rect = pygame.Rect(0, ai_settings.screen_height - 100, 104, 20)
    pygame.draw.rect(screen, (255, 255, 255), rect)
    rect = pygame.Rect(2, ai_settings.screen_height - 98, 100, 16)
    pygame.draw.rect(screen, (0, 0, 0), rect)
    rect = pygame.Rect(2, ai_settings.screen_height - 98, ship.energy / 10, 16)
    pygame.draw.rect(screen, (255, 0, 0), rect)


def display_magazine(ai_settings, screen, ship):
    text = ai_settings.font.render('弹仓:'+str(ship.magazine)+'/'+str(ship.max_magazine), 1, (255, 255, 255))
    screen.blit(text, (0, ai_settings.screen_height - 40))

    rect = pygame.Rect(0, ai_settings.screen_height - 20, 104, 20)
    pygame.draw.rect(screen, (255, 255, 255), rect)
    rect = pygame.Rect(2, ai_settings.screen_height - 18, 100, 16)
    pygame.draw.rect(screen, (0, 0, 0), rect)
    rect = pygame.Rect(2, ai_settings.screen_height - 18, ship.reload_completion / 10, 16)
    pygame.draw.rect(screen, (255, 0, 0), rect)


def display_hp(ai_settings, screen, ship):
    text = ai_settings.font.render('生命值:', 1, (255, 255, 255))
    screen.blit(text, (0, ai_settings.screen_height - 160))

    rect = pygame.Rect(0, ai_settings.screen_height - 140, 104, 20)
    pygame.draw.rect(screen, (255, 255, 255), rect)
    rect = pygame.Rect(2, ai_settings.screen_height - 138, 100, 16)
    pygame.draw.rect(screen, (0, 0, 0), rect)
    rect = pygame.Rect(2, ai_settings.screen_height - 138, ship.hp / 4, 16)
    pygame.draw.rect(screen, (0, 255, 0), rect)


def display_speed(ai_settings, screen):
    text = ai_settings.font.render('游戏速度:'+'%.2f' % ai_settings.base_speed, 1, (255, 255, 255))
    screen.blit(text, (0, ai_settings.screen_height - 180))


def display_score(ai_settings, screen, stats):
    text = ai_settings.font.render('得分:' + str(stats.score), 1, (255, 255, 255))
    screen.blit(text, (0, ai_settings.screen_height - 200))


def update_screen(ai_settings, screen, stats, ship, aliens, bullets, laser, impacts, explosions, play_botton):
    screen.fill(ai_settings.bg_color)

    # 加载背景图片
    screen.blit(ai_settings.background, (0, 0))

    display_temperature(ai_settings, screen, ship)
    display_energy(ai_settings, screen, ship)
    display_magazine(ai_settings, screen, ship)
    display_hp(ai_settings, screen, ship)
    display_speed(ai_settings, screen)
    display_score(ai_settings, screen, stats)
    for alien in aliens:
        alien.draw()
        alien.draw_hp()
    if ship.laser_fire:
        for ls in laser.sprites():
            ls.draw_laser(ship)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for impact in impacts.sprites():
        impact.draw_impact()
    ship.blitme()
    for explosion in explosions:
        explosion.display()

    if not stats.game_active:
        play_botton.draw_button()
    pygame.display.flip()


def update_impact(ai_settings, stats, aliens, impacts, explosions):
    impacts.update()

    for impact in impacts.copy():
        if impact.rect.bottom <= 0:
            impacts.remove(impact)

    collisions = pygame.sprite.groupcollide(impacts, aliens, False, False)
    damage(ai_settings, stats, collisions, aliens, explosions)


def update_bullets(ai_settings, stats, aliens, bullets, explosions):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, False)
    damage(ai_settings, stats, collisions, aliens, explosions)


def update_laser(ai_settings, stats, laser, ship, aliens, explosions):
    if ship.laser_fire:
        ship.energy -= ship.spend_speed
        if ship.energy <= 0:
            ship.energy = 0
        else:
            laser.update(ship)
            collisions = pygame.sprite.groupcollide(laser, aliens, False, False)
            damage(ai_settings, stats, collisions, aliens, explosions)


def update_explosion(explosions):
    for explosion in explosions:
        explosion.update()


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - (3 * ship_height))
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算每行可容纳多少个外星人
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def update_alien(ai_settings, ship, aliens):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship.hp -= 1
    for alien in aliens:
        if alien.rect.bottom >= ai_settings.screen_height:
            return True


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def damage(ai_settings, stats, collisions, aliens, explosions):
    for weapon, targets in collisions.items():
        for alien in targets:
            alien.hp -= weapon.damage
    for alien in aliens.copy():
        if alien.hp <= 0:
            for explosion in explosions:
                if not explosion.visible:
                    explosion.creat(alien.rect.centerx, alien.rect.centery)
                    pygame.mixer.Sound('sound/explosion.wav').play()
                    break
            aliens.remove(alien)
            stats.score += ai_settings.alien_point
