import pygame
from gun import Gun
import controls
from pygame.sprite import Group


def run():
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("Cosmo defenders")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    enemys = Group()
    controls.create_army(screen, enemys)
    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        controls.update(bg_color, screen, gun, bullets, enemys)
        controls.update_bullets(bullets)
        controls.update_enemys(enemys)


run()
