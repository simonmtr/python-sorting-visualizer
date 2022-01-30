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
        pass
    def create_sorting_array(self, ui_style):
        shapes_array_to_sort = []
        array_values_to_sort = np.random.choice(range(GlobalHelper.get_array_to_sort_size()), size=(GlobalHelper.get_array_to_sort_size()), replace=False)
        for i in array_values_to_sort:
            if ui_style == UiStylesE.BARS:
                print("bars")
            elif ui_style == UiStylesE.CIRCLE:
                cs = CircleSorting(self.ui.screensize)
                shapes_array_to_sort.append(Pixel(array_values_to_sort[i], i, self.ui, cs))
        
        print(shapes_array_to_sort)
        print(len(shapes_array_to_sort))
        return shapes_array_to_sort
    def circle_do_different_sorting_algorithms(self):
        for ui_style in UiStylesE:
            shapes_array_to_sort = self.create_sorting_array(ui_style)
            for sorting_algorithm in SortingAlgorithmE:
                if sorting_algorithm == SortingAlgorithmE.BUBBLE_SORT:
                    print("doing bubble sort")
                    # bubble_sort_shapes_array_to_sort = copy.deepcopy(shapes_array_to_sort)
                    # self.pixel_array = cs.paint_circle(bubble_sort_array_to_sort, ui.screen)
                    bubble_sort_shapes_array_to_sort = shapes_array_to_sort
                    self.sa.bubble_sort(bubble_sort_shapes_array_to_sort, self.ui)
                    print("bubble sort finished")
                    time.sleep(4)
                elif sorting_algorithm == SortingAlgorithmE.INSERTION_SORT:
                    print("doing insertion sort")
                    cs = CircleSorting(len(self.array_to_sort),self.ui.screensize)
                    insertion_sort_array_to_sort = copy.deepcopy(self.array_to_sort)
                    self.pixel_array = cs.paint_circle(insertion_sort_array_to_sort, self.ui.screen)
                    self.sa.insertion_sort(insertion_sort_array_to_sort, self.ui.screen, self.ui.screensize)
                    print("insertion sort finished")
                    time.sleep(4)
                if sorting_algorithm == SortingAlgorithmE.QUICK_SORT:
                    print("doing quick sort")
                    cs = CircleSorting(len(self.array_to_sort), self.ui.screensize)
                    quick_sort_array_to_sort = copy.deepcopy(self.array_to_sort)
                    self.pixel_array = cs.paint_circle(quick_sort_array_to_sort,  self.ui.screen)
                    self.sa.quickSort(quick_sort_array_to_sort, quick_sort_array_to_sort,  self.ui.screen,  self.ui.screensize)
                    print("quick sort finished")
                    time.sleep(4)
                else:
                    print("no sorting algorithm chosen")
    def bars_do_different_sorting_algorithms(self, array_to_sort, screen, screensize):
        for sorting_algorithm in SortingAlgorithmE:
            if sorting_algorithm == SortingAlgorithmE.BUBBLE_SORT:
                print("doing bubble sort for bars")
        print("bars")
