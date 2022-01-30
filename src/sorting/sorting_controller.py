import pygame
from enums.sorting_algorithms_e import SortingAlgorithmE
import time
import copy
import numpy as np
from enums.ui_styles_e import UiStylesE
from helper.global_helper import GlobalHelper 
from sorting.sorting_algorithms import SortingAlgorithms
from sorting.circle_sorting import CircleSorting
from ui.pixel import Pixel



class SortingController:
    def __init__(self, ui) -> None:
        self.sa = SortingAlgorithms()
        self.ui = ui
        self.order_of_shapes_array_for_reshuffling = []
        self.sorting_visualisation_a = ""
        self.array_is_sorted = True
        pass
    def create_initial_sorting_array(self, ui_style):
        print("creating initial sorting array")
        shapes_array_to_sort = []
        array_values_to_sort = np.random.choice(range(GlobalHelper.get_array_to_sort_size()), size=(GlobalHelper.get_array_to_sort_size()), replace=False)
        for i in array_values_to_sort:
            if ui_style == UiStylesE.BARS:
                print("bars")
            elif ui_style == UiStylesE.CIRCLE:
                self.sorting_visualisation_a = CircleSorting(self.ui.screensize)
                pixel = Pixel(array_values_to_sort[i], i, self.ui, self.sorting_visualisation_a)
                shapes_array_to_sort.append(pixel)
                pixel.draw()
                self.order_of_shapes_array_for_reshuffling.append((array_values_to_sort[i],i))
        self.array_is_sorted = False
        time.sleep(1)
        return shapes_array_to_sort
    def reshuffle_sorting_array(self):
        reshuffled_shapes_array_to_sort = []
        print("reshuffling array")
        for (i,j) in self.order_of_shapes_array_for_reshuffling:
            pixel = Pixel(i, j, self.ui, self.sorting_visualisation_a)
            reshuffled_shapes_array_to_sort.append(pixel)
            pixel.draw()
        self.array_is_sorted = False
        time.sleep(1)
        return reshuffled_shapes_array_to_sort
    def circle_do_different_sorting_algorithms(self):
        for ui_style in UiStylesE:
            shapes_array_to_sort = self.create_initial_sorting_array(ui_style)
            for sorting_algorithm in SortingAlgorithmE:
                if self.array_is_sorted == True:
                    shapes_array_to_sort = self.reshuffle_sorting_array()
                if sorting_algorithm == SortingAlgorithmE.BUBBLE_SORT:
                    print("doing bubble sort")
                    self.sa.bubble_sort(shapes_array_to_sort)
                    self.array_is_sorted = True
                    print("bubble sort finished")
                    time.sleep(4)
                    self.ui.screen.fill(0) # fill with backcolor
                elif sorting_algorithm == SortingAlgorithmE.INSERTION_SORT:
                    print("doing insertion sort")
                    self.sa.insertion_sort(shapes_array_to_sort)
                    self.array_is_sorted = True
                    print("insertion sort finished")
                    self.ui.screen.fill(0) # fill with backcolor
                    time.sleep(4)
                else:
                    print("no sorting algorithm chosen")
    def bars_do_different_sorting_algorithms(self, array_to_sort, screen, screensize):
        for sorting_algorithm in SortingAlgorithmE:
            if sorting_algorithm == SortingAlgorithmE.BUBBLE_SORT:
                print("doing bubble sort for bars")
        print("bars")
