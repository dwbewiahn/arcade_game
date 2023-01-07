#Python arcade game style 
import pygame
import math

pygame.init()
fps = 60 
timer = pygame.time.clock()
font = pygame.font.Font('assets/font/myFont.ttf',32)
WIDTH = 900
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
bgs = []
banners = []
guns = []
level = 0
for i in range (1,4):
    bgs.append(pygame.image.load(f'assets/bgs/{i}.png'))
    banners.append(pygame.image.load(f'assets/banners/{i}.png'))
    guns.append(pygame.image.load(f'assets/guns/{i}.png'))

    





