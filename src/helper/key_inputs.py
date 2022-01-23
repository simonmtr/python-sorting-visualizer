import pygame
from pygame.locals import *

def KEY_INPUTS():
    for Event in pygame.event.get():
        if Event.type == pygame.KEYDOWN:
            if Event.key == K_ESCAPE:
                return "ESCAPE"
        if Event.type == pygame.QUIT:
            return "ESCAPE"
    return None
