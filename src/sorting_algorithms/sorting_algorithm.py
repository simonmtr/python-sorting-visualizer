import copy
import time

from random import randint
from sorting_visualisation_shapes.circle_sorting import CircleSorting
from ui.rgb_handling import RGBHandling
from ui.single_pixel import SinglePixel


class SortingAlgorithm:
    def __init__(self) -> None:
        self.sorting_functions = ['quick_sort', 'bubble_sort', 'insertion_sort']
        self.pixel_array = []
        pass
    def do_different_sorting_algorithms(self, array_to_sort, screen, screensize):
        for i in range(len(self.sorting_functions)):
            if self.sorting_functions[i] =='bubble_sort':
                print("doing bubble sort")
                cs = CircleSorting(len(array_to_sort),screensize)
                bubble_sort_array_to_sort = copy.deepcopy(array_to_sort)
                self.pixel_array = cs.paint_circle(bubble_sort_array_to_sort, screen)
                self.bubble_sort(bubble_sort_array_to_sort, screen, screensize)
                time.sleep(4)
            elif self.sorting_functions[i] =='insertion_sort':
                print("doing insertion sort")
                cs = CircleSorting(len(array_to_sort),screensize)
                insertion_sort_array_to_sort = copy.deepcopy(array_to_sort)
                self.pixel_array = cs.paint_circle(insertion_sort_array_to_sort, screen)
                self.insertion_sort(insertion_sort_array_to_sort, screen, screensize)
                time.sleep(4)
            elif self.sorting_functions[i]  =='quick_sort':
                print("doing quick sort")
                cs = CircleSorting(len(array_to_sort),screensize)
                quick_sort_array_to_sort = copy.deepcopy(array_to_sort)
                self.pixel_array = cs.paint_circle(quick_sort_array_to_sort, screen)
                self.quickSort(quick_sort_array_to_sort, quick_sort_array_to_sort, screen, screensize)
                time.sleep(4)
            else:
                print("no sorting algorithm chosen")

    def bubble_sort(self, array_to_sort, screen, screensize):
        cs = CircleSorting(len(array_to_sort),screensize)
        n = len(array_to_sort)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if array_to_sort[j] > array_to_sort[j + 1] :
                    array_to_sort[j], array_to_sort[j + 1] = array_to_sort[j + 1], array_to_sort[j]
                    # only two pixel are changing values in this case
                    self.pixel_array[j] = SinglePixel(screen, RGBHandling.get_rgb_color(len(array_to_sort),array_to_sort[j]), cs.get_x_and_y(array_to_sort,array_to_sort[j])[0],cs.get_x_and_y(array_to_sort,array_to_sort[j])[1])
                    self.pixel_array[j+1] = SinglePixel(screen, RGBHandling.get_rgb_color(len(array_to_sort),array_to_sort[j+1]), cs.get_x_and_y(array_to_sort,array_to_sort[j+1])[0],cs.get_x_and_y(array_to_sort,array_to_sort[j+1])[1])
                    SinglePixel.update_many(self.pixel_array,screen)
                    time.sleep(0.02)
        print('buttle sort finished')
    def insertion_sort(self,array_to_sort, screen, screensize):
        cs = CircleSorting(len(array_to_sort),screensize)
        temp_array_for_ui = []
        print(f"before: {array_to_sort}")
        for index in range(1, len(array_to_sort)):
            currentValue = array_to_sort[index]
            currentPosition = index
            temp_array_for_ui = copy.deepcopy(array_to_sort)
            while currentPosition > 0 and array_to_sort[currentPosition - 1] > currentValue:
                array_to_sort[currentPosition] = array_to_sort[currentPosition -1]
                currentPosition = currentPosition - 1
            self.pixel_array = cs.paint_circle(temp_array_for_ui, screen)
            time.sleep(0.02)
            array_to_sort[currentPosition] = currentValue
    def quickSort(self,full_array_to_sort,array_to_sort, screen,screensize):
        cs = CircleSorting(len(full_array_to_sort),screensize)
        if len(array_to_sort) < 2:
            return array_to_sort
        low, same, high = [], [], []
        pivot = array_to_sort[randint(0, len(array_to_sort) - 1)]
        for item in array_to_sort:
            if item < pivot:
                low.append(item)
            elif item == pivot:
                same.append(item)
            elif item > pivot:
                high.append(item)
        self.pixel_array = cs.paint_circle(full_array_to_sort, screen)
        time.sleep(0.02)
        return self.quickSort(full_array_to_sort,low, screen,screensize) + same + self.quickSort(full_array_to_sort,high, screen,screensize)