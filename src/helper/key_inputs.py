import pygame
from pygame.locals import *

def KEY_INPUTS():
    for Event in pygame.event.get():
        if Event.type == pygame.KEYDOWN:
            if Event.key == K_ESCAPE:
                return "ESCAPE"
            if Event.key == K_1:
                return "ONE"
            if Event.key == K_2:
                return "TWO"
        if Event.type == pygame.QUIT:
            return "ESCAPE"
    return None
