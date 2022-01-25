import pygame
import sys
import numpy as np 
from pygame.locals import *
from helper.key_inputs import KEY_INPUTS
from sorting_visualisation_shapes.circle_sorting import CircleSorting
from sorting_algorithms.sorting_algorithm import SortingAlgorithm
import copy

 

pygame.init()
MAIN_LOOP = True
HEIGHT = 300
WIDTH = 300
CAPTION = "simonmtr sorting visualization"
FramePerSec = pygame.time.Clock()

SCREEN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
SCREEN_SIZE = pygame.display.get_window_size()
SORTING_ARRAY = np.random.choice(range(50), size=(50), replace=False)

# while MAIN_LOOP:
pygame.display.set_caption(CAPTION)
KEY = KEY_INPUTS()
if KEY == "ESCAPE":
    MAIN_LOOP = False
    pygame.quit()
    sys.exit()
SCREEN.fill(0) # fill with backcolor
sa = SortingAlgorithm()
sa.do_different_sorting_algorithms(SORTING_ARRAY, SCREEN, SCREEN_SIZE)

