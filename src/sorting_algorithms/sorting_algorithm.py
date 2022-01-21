from sorting_visualisation_shapes.circle_sorting import CircleSorting
import time
from random import randint

class SortingAlgorithm:
    def __init__(self) -> None:
        pass
    def bubbleSort(full_array_to_sort,array_to_sort, SCREEN, SCREEN_SIZE):
        n = len(array_to_sort)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if array_to_sort[j] > array_to_sort[j + 1] :
                    array_to_sort[j], array_to_sort[j + 1] = array_to_sort[j + 1], array_to_sort[j]
            SCREEN.fill(0)
            CircleSorting.paint_circle(full_array_to_sort,array_to_sort, SCREEN, SCREEN_SIZE) # currently painting whole circle every time
    def insertionSort(full_array_to_sort,array_to_sort, SCREEN, SCREEN_SIZE):
          for i in range(1, len(array_to_sort)):
            key = array_to_sort[i]
            j = i-1
            while j >=0 and key < array_to_sort[j] :
                    array_to_sort[j+1] = array_to_sort[j]
                    j -= 1
            array_to_sort[j+1] = key
            SCREEN.fill(0)
            CircleSorting.paint_circle(full_array_to_sort,array_to_sort, SCREEN, SCREEN_SIZE) # currently painting whole circle every time
    def quickSort(self,full_array_to_sort,array_to_sort, SCREEN, SCREEN_SIZE):
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
        # SCREEN.fill(0)
        CircleSorting.paint_circle(full_array_to_sort,array_to_sort, SCREEN, SCREEN_SIZE) # currently painting whole circle every time
        time.sleep(1)
        return self.quickSort(full_array_to_sort,low, SCREEN, SCREEN_SIZE) + same + self.quickSort(full_array_to_sort,high, SCREEN, SCREEN_SIZE)
    
    