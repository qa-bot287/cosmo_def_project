import pygame
import sys


def events(gun):
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
        elif event.type == pygame.KEYUP:
            # Right
            if event.key == pygame.K_RIGHT:
                gun.move_right = False
            elif event.key == pygame.K_LEFT:
                gun.move_left = False


def update(bg_color, screen, gun):
    """Update screen"""
    screen.fill(bg_color)
    gun.output()
    pygame.display.flip()
