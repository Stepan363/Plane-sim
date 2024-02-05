import pygame
WIDTH = 1200
HEIGHT = 700

plane = pygame.image.load('plane.png')
def update():
    if keyboard.up:
        plane = pygame.transform.rotate(plane, -2)

    if keyboard.down:
        plane = pygame.transform.rotate(plane, 2)
pygame.display.flip()

pgzrun.go()