import pygame
import sys
import numpy as np 
import time
from pygame.locals import *
from key_inputs import KEY_INPUTS
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
SORTING_ARRAY = np.random.choice(range(200), size=(200), replace=False)

while MAIN_LOOP:
    pygame.display.set_caption(CAPTION)
    KEY = KEY_INPUTS()
    if KEY == "ESCAPE":
        MAIN_LOOP = False
        pygame.quit()
        sys.exit()
    SCREEN.fill(0)
    sa = SortingAlgorithm()
    sa.quickSort(SORTING_ARRAY,SORTING_ARRAY,SCREEN,SCREEN_SIZE)
    temp_array = copy.deepcopy(SORTING_ARRAY)
    temp_array_2 = copy.deepcopy(SORTING_ARRAY)
    SortingAlgorithm.bubbleSort(SORTING_ARRAY,SORTING_ARRAY,SCREEN, SCREEN_SIZE)
    CircleSorting.paint_circle(temp_array,SORTING_ARRAY,SCREEN, SCREEN_SIZE)
    SortingAlgorithm.insertionSort(temp_array,SORTING_ARRAY,SCREEN, SCREEN_SIZE)
    CircleSorting.paint_circle(temp_array_2,SORTING_ARRAY,SCREEN,SCREEN_SIZE)

    # np.random.shuffle(SORTING_ARRAY)

