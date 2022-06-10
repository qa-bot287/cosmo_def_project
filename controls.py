import pygame
import sys
from bullet import Bullet


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


def update(bg_color, screen, gun, bullets):
    """Update screen"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    pygame.display.flip()


def update_bullets(bullets):
    """Update bullets position"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
