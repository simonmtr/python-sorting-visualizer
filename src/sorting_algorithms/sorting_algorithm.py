import copy
from sorting_visualisation_shapes.circle_sorting import CircleSorting
from ui.rgb_handling import RGBHandling
from ui.single_pixel import SinglePixel
import time

class SortingAlgorithm:
    def __init__(self) -> None:
        self.sorting_functions = ['bubble_sort', 'insertion_sort', 'quick_sort']
        self.pixel_array = []
        pass
    def do_different_sorting_algorithms(self, array_to_sort, screen, screensize):
        for i in range(len(self.sorting_functions)):
            if self.sorting_functions[i] =='bubble_sort':
                cs = CircleSorting(len(array_to_sort),screensize)
                print("doing bubble sort")
                bubble_sort_array_to_sort = copy.deepcopy(array_to_sort)
                self.pixel_array = cs.paint_circle(bubble_sort_array_to_sort, screen)
                self.bubbleSort(bubble_sort_array_to_sort, screen, screensize)
            elif self.sorting_functions[i] =='insertion_sort':
                print("doing insertion sort")
                # self.insertionSort()
            elif self.sorting_functions[i]  =='quick_sort':
                print("doing quick sort")
                # self.quickSort()
            else:
                print("no sorting algorithm chosen")

    def bubbleSort(self, array_to_sort, screen, screensize):
        cs = CircleSorting(len(array_to_sort),screensize)
        n = len(array_to_sort)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if array_to_sort[j] > array_to_sort[j + 1] :
                    array_to_sort[j], array_to_sort[j + 1] = array_to_sort[j + 1], array_to_sort[j]
                    print(f"array to sort at j({j}): {array_to_sort[j]}")
                    self.pixel_array[j] = SinglePixel(screen, RGBHandling.get_rgb_color(len(array_to_sort),array_to_sort[j]), cs.get_x_and_y(array_to_sort,array_to_sort[j])[0],cs.get_x_and_y(array_to_sort,array_to_sort[j])[1])
                    self.pixel_array[j+1] = SinglePixel(screen, RGBHandling.get_rgb_color(len(array_to_sort),array_to_sort[j+1]), cs.get_x_and_y(array_to_sort,array_to_sort[j+1])[0],cs.get_x_and_y(array_to_sort,array_to_sort[j+1])[1])
                    SinglePixel.update_many(self.pixel_array,screen)
        print('buttle sort finished')
    def insertionSort(self,full_array_to_sort,array_to_sort, SCREEN, SCREEN_SIZE):
        cs = CircleSorting()
        for i in range(1, len(array_to_sort)):
 
            key = array_to_sort[i]
            j = i-1
            while j >= 0 and key < array_to_sort[j] :
                    array_to_sort[j + 1] = array_to_sort[j]
                    j -= 1
                    SCREEN.fill(0)
                    # cs.paint_circle(full_array_to_sort,array_to_sort, SCREEN, SCREEN_SIZE) # currently painting whole circle every time
            print(array_to_sort)

            array_to_sort[j + 1] = key

            
    def quickSort(self,full_array_to_sort,array_to_sort, SCREEN, SCREEN_SIZE):
        cs = CircleSorting()
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
        SCREEN.fill(0)
        cs.paint_circle(full_array_to_sort,array_to_sort, SCREEN, SCREEN_SIZE) # currently painting whole circle every time
        return self.quickSort(full_array_to_sort,low, SCREEN, SCREEN_SIZE) + same + self.quickSort(full_array_to_sort,high, SCREEN, SCREEN_SIZE)
    
    