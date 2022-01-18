from dataclasses import replace
from encodings import normalize_encoding
from pickle import TRUE
from pstats import SortKey
import pygame
import sys
import numpy as np 
import time
from pygame.locals import *
from key_inputs import KEY_INPUTS
from ui.single_pixel import SinglePixel
from sorting_visualisation_shapes.circle_sorting import CircleSorting
from sorting_algorithms.bubble_sort import SortingAlgorithm
 
pygame.init()
MAIN_LOOP = True
HEIGHT = 300
WIDTH = 300
CENTER = (500,500)
CAPTION = "simonmtr sorting visualization"
FramePerSec = pygame.time.Clock()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SORTING_ARRAY = np.random.choice(range(100), size=(100), replace=False)
print(SORTING_ARRAY)

while MAIN_LOOP:
    pygame.display.set_caption(CAPTION)
    KEY = KEY_INPUTS()
    if KEY == "ESCAPE":
        MAIN_LOOP = False
        pygame.quit()
        sys.exit()
    SCREEN.fill(0)
    SortingAlgorithm.bubbleSort(SORTING_ARRAY,SCREEN)
    # CircleSorting.create_initial_circle(SCREEN, SORTING_ARRAY, CENTER)
    time.sleep(5)


