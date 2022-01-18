from ctypes.wintypes import RGB
from dis import dis
from operator import index
from ui.single_pixel import SinglePixel
import math
import pygame
import time
import numpy as np 
from ui.rgb_handling import RGBHandling


class CircleSorting:
    def create_initial_circle(screen, array_to_sort):
        # each dot's distance from the outer circle is how incorrect of a position the number that dot represent is.
        # for example, if 1 is the smallest number in the array and it is currently in position 500 of 1000, it is in the
        # worst possible position, so it will be in the center of the screen, the farthest from its ideal position in the outer circle

        # radius is the number of dots/2 times the pixel size
        # radius = len(array_to_sort)/2*5
        radius = 100
        single_pixels = []
        # circle divided by the number of pixel to evenly distribute them
        step = 360/len(array_to_sort)
        # angle 
        angle = 0
        # x and y coordinate for the single pixel
        x = 0
        y = 0
        
        for i in range(len(array_to_sort)):
            # get display value in the array: i=value; array_to_sort.index(i)=perfect place for i to be
            # example: i=15, radius=20*5, array_to_sort.index(i)=7 ===> away from optimal point: 15 - 7 = 8  --> percentage of radius= 8/radius*100
            index_in_sorting_array = np.where(array_to_sort == i)[0][0]
            print(f"i: {i}")
            worst_case_index_difference = i
            if len(array_to_sort)/2 < i:
                print(f"setting worst case to {i}")
                worst_case_index_difference=i
            else:
                print(f"setting worst case to {len(array_to_sort)-i}")
                worst_case_index_difference=len(array_to_sort)-i
            
            print(f"worst case for {i} is {worst_case_index_difference}")

            print(f"percentag of worst case: {(abs(i-index_in_sorting_array))/worst_case_index_difference}")
            display_at_percentage_of_radius = (abs(i-index_in_sorting_array))/worst_case_index_difference
            
            display_at_percentage_of_radius = 1 - display_at_percentage_of_radius
            x = 150 * math.cos(angle) * display_at_percentage_of_radius + 150
            y = 150 * math.sin(angle) * display_at_percentage_of_radius + 150
            print(f"creating new pixel at {x} and {y}")

            angle += step
            single_pixels.append(SinglePixel(screen, RGBHandling.get_rgb_color(len(array_to_sort), i), x, y))

        for sp in single_pixels:
            sp.update()
            pygame.display.update()
        return single_pixels
    
        