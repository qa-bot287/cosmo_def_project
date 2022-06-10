import pygame
import sys
from bullet import Bullet
from enemy import Enemy


def events(screen, gun, bullets):
    """event handling"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Right
            if event.key == pygame.K_RIGHT:
                gun.move_right = True
            elif event.key == pygame.K_LEFT:
                gun.move_left = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # Right
            if event.key == pygame.K_RIGHT:
                gun.move_right = False
            elif event.key == pygame.K_LEFT:
                gun.move_left = False


def update(bg_color, screen, gun, bullets, enemys):
    """Update screen"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    enemys.draw(screen)
    pygame.display.flip()


def update_bullets(bullets):
    """Update bullets position"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_enemys(enemys):
    """"update enemy position"""
    enemys.update()


def create_army(screen, enemys):
    """Create army of enemy"""
    enemy = Enemy(screen)
    enemy_width = enemy.rect.width
    number_enemy_x = int(((600 - 2 * enemy_width) / enemy_width))
    enemy_height = enemy.rect.height
    number_enemy_y = int((800 - 100 - 2 * enemy_height) / enemy_height)

    for row_number in range(number_enemy_y - 3):
        for enemy_num in range(number_enemy_x):
            enemy = Enemy(screen)
            enemy.x = enemy_width + (enemy_width * enemy_num)
            enemy.y = enemy_height + (enemy_height * row_number)
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.rect.height + (enemy.rect.height * row_number)
            enemys.add(enemy)
