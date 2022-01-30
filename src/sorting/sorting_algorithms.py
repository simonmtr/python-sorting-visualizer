import copy
import time

from random import randint
from sorting.circle_sorting import CircleSorting


class SortingAlgorithms:
    def __init__(self) -> None:
        self.pixel_array = []
        pass
    def bubble_sort(self, shapes_array_to_sort, ui):
        n = len(shapes_array_to_sort)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if shapes_array_to_sort[j].value > shapes_array_to_sort[j + 1].value :
                    temp_value = shapes_array_to_sort[j].value
                    shapes_array_to_sort[j].update_value(shapes_array_to_sort[j+1].value,j+1)
                    shapes_array_to_sort[j+1].update_value(temp_value,j)
                    time.sleep(0.02)
        print('buttle sort finished')
    def insertion_sort(self,array_to_sort, screen, screensize):
        cs = CircleSorting(len(array_to_sort),screensize)
        temp_array_for_ui = []
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