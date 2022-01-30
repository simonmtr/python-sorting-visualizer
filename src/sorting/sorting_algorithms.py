import copy
import time

from random import randint
from sorting.circle_sorting import CircleSorting


class SortingAlgorithms:
    def __init__(self) -> None:
        self.pixel_array = []
        self.is_adjusted = 1
        pass
    def bubble_sort(self, shapes_array_to_sort):
        n = len(shapes_array_to_sort)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if shapes_array_to_sort[j].value > shapes_array_to_sort[j + 1].value :
                    temp_value = shapes_array_to_sort[j].value
                    shapes_array_to_sort[j].update_value(shapes_array_to_sort[j+1].value,j+1)
                    shapes_array_to_sort[j+1].update_value(temp_value,j)
                    time.sleep(0.02)
    def insertion_sort(self, shapes_array_to_sort):
        # temp_array_for_ui = []
        for i in range(1, len(shapes_array_to_sort)):
            currentValue = shapes_array_to_sort[i].value
            # temp_array_for_ui = copy.deepcopy(shapes_array_to_sort)
            while i > 0 and shapes_array_to_sort[i - 1].value > currentValue:
                temp_value = shapes_array_to_sort[i - 1].value
                shapes_array_to_sort[i - 1].update_value(shapes_array_to_sort[i].value, i)
                shapes_array_to_sort[i].update_value(temp_value, i - 1)
                i = i - 1
            time.sleep(0.02)
            # shapes_array_to_sort[i] = currentValue