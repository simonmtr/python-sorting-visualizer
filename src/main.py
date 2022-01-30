import pygame
import sys
from pygame.locals import *
from helper.key_inputs import KEY_INPUTS
from sorting.sorting_controller import SortingController
from ui.bar import Bar 
from ui.ui import UI


pygame.init()
MAIN_LOOP = True
FramePerSec = pygame.time.Clock()

SCREEN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
SCREEN_SIZE = pygame.display.get_window_size()
UI = UI(SCREEN,SCREEN_SIZE)
CAPTION = "Sorting Visualization"

while MAIN_LOOP:
    pygame.display.set_caption(CAPTION)
    sc = SortingController(UI)
    KEY = KEY_INPUTS()
    if KEY == "ESCAPE":
        MAIN_LOOP = False
        pygame.quit()
        sys.exit()
    if KEY == "ONE":
        print("doing circle sorting")
        sc.circle_do_different_sorting_algorithms()
    if KEY == "TWO":
        print("doing bar sorting")
        bar = Bar(UI,"green",100,100)
        bar.move()
        # sc.bars_do_different_sorting_algorithms()
    SCREEN.fill(0) # fill with backcolor

