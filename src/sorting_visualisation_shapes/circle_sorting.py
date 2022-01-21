from ui.single_pixel import SinglePixel
import math
import pygame
import numpy as np 
from ui.rgb_handling import RGBHandling
from helper.global_helper import GlobalHelper


class CircleSorting:
    def paint_circle(full_array_to_sort,array_to_sort, SCREEN, SCREEN_SIZE):
        # each dot's distance from the outer circle is how incorrect of a position the number that dot represent is.
        # for example, if 1 is the smallest number in the array and it is currently in position 500 of 1000, it is in the
        # worst possible position, so it will be in the center of the screen, the farthest from its ideal position in the outer circle
        single_pixels = []
        # circle divided by the number of pixel to evenly distribute them
        step = 360/len(full_array_to_sort)
        # angle 
        angle = 0
        # x and y coordinate for the single pixel
        x = 0
        y = 0
        
        # set middle of circle according to current position
        middle_of_screen_x = SCREEN_SIZE[0]/2
        middle_of_screen_y = SCREEN_SIZE[1]/2

        pixel_multiplicator = 3 * GlobalHelper.get_pixel_size()

        for i in range(len(array_to_sort)):
            index_in_sorting_array = np.where(full_array_to_sort == i)[0][0]
            worst_case_index_difference = i
            if len(full_array_to_sort)/2 < i:
                worst_case_index_difference=i
            else:
                worst_case_index_difference=len(full_array_to_sort)-i
            
            display_at_percentage_of_radius = (abs(i-index_in_sorting_array))/worst_case_index_difference
            
            display_at_percentage_of_radius = 1 - display_at_percentage_of_radius
            x = (middle_of_screen_x - pixel_multiplicator) * math.cos(step * array_to_sort[i]) * display_at_percentage_of_radius + middle_of_screen_x 
            y = (middle_of_screen_y - pixel_multiplicator)* math.sin(step *array_to_sort[i]) * display_at_percentage_of_radius + middle_of_screen_y

            single_pixels.append(SinglePixel(SCREEN, RGBHandling.get_rgb_color(len(array_to_sort), array_to_sort[i]), x, y))

        for sp in single_pixels:
            sp.update()
        pygame.display.update()
        return single_pixels
    
    def paint_from_pyramid_to_line (array_to_sort, SCREEN, SCREEN_SIZE):

        # //////////////////////
        # remove sin or cos from one axis
        # /////////////////////


        # each dot's distance from the outer circle is how incorrect of a position the number that dot represent is.
        # for example, if 1 is the smallest number in the array and it is currently in position 500 of 1000, it is in the
        # worst possible position, so it will be in the center of the screen, the farthest from its ideal position in the outer circle
        single_pixels = []
        # circle divided by the number of pixel to evenly distribute them
        step = 360/len(array_to_sort)
        # angle 
        angle = 0
        # x and y coordinate for the single pixel
        x = 0
        y = 0
        
        # set middle of circle according to current position
        middle_of_screen_x = SCREEN_SIZE[0]/2
        middle_of_screen_y = SCREEN_SIZE[1]/2

        pixel_multiplicator = 3 * GlobalHelper.get_pixel_size()

        for i in range(len(array_to_sort)):
            index_in_sorting_array = np.where(array_to_sort == i)[0][0]
            worst_case_index_difference = i
            if len(array_to_sort)/2 < i:
                worst_case_index_difference=i
            else:
                worst_case_index_difference=len(array_to_sort)-i
            
            display_at_percentage_of_radius = (abs(i-index_in_sorting_array))/worst_case_index_difference
            
            display_at_percentage_of_radius = 1 - display_at_percentage_of_radius
            x = (middle_of_screen_x - pixel_multiplicator) * math.cos(round(angle)) * display_at_percentage_of_radius + middle_of_screen_x 
            y = (middle_of_screen_y - pixel_multiplicator)* display_at_percentage_of_radius + middle_of_screen_y
            angle += step

            single_pixels.append(SinglePixel(SCREEN, RGBHandling.get_rgb_color(len(array_to_sort), i), x, y))

        for sp in single_pixels:
            sp.update()
        pygame.display.update()
        return single_pixels
    
        