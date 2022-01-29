from ui.single_pixel import SinglePixel
import math
import pygame
import numpy as np 
from ui.rgb_handling import RGBHandling
from helper.global_helper import GlobalHelper



class CircleSorting:
    def __init__(self, array_length, screensize) -> None:
        # set middle of circle according to current position
        self.middle_of_screen_x = screensize[0]/2
        self.middle_of_screen_y = screensize[1]/2
        self.step = 360/array_length
        self.pixel_multiplicator = 3 * GlobalHelper.get_pixel_size()
    def get_x_and_y(self, array_to_sort, value):
        display_percentage_of_radius = self.get_display_percentage_of_radius(array_to_sort, value)
        x = (self.middle_of_screen_x - self.pixel_multiplicator) * math.cos(self.step * value) * display_percentage_of_radius + self.middle_of_screen_x 
        y = (self.middle_of_screen_y - self.pixel_multiplicator) * math.sin(self.step * value) * display_percentage_of_radius + self.middle_of_screen_y
        return [x,y]
    def get_display_percentage_of_radius(self, array_to_sort, value):
        index_in_sorting_array = np.where(array_to_sort == value)[0][0]
        worst_case_index_difference = value
        if value > len(array_to_sort)/2:
            worst_case_index_difference = value
        else: # value < len(array_to_sort)/2
            worst_case_index_difference=len(array_to_sort)-value
        return 1 - (abs(value-index_in_sorting_array))/worst_case_index_difference
    def paint_circle(self, array_to_sort, screen):
        # each dot's distance from the outer circle is how incorrect of a position the number that dot represent is.
        # for example, if 1 is the smallest number in the array and it is currently in position 500 of 1000, it is in the
        # worst possible position, so it will be in the center of the screen, the farthest from its ideal position in the outer circle
        # circle divided by the number of pixel to evenly distribute them
        pixels = []
        screen.fill(0)
        for i in range(len(array_to_sort)):
            sp = SinglePixel(screen, RGBHandling.get_rgb_color(len(array_to_sort),i), self.get_x_and_y(array_to_sort, i)[0],self.get_x_and_y(array_to_sort, i)[1])
            pixels.append(sp)
            sp.draw_pixel()
        pygame.display.update()
        return pixels
    
    def paint_from_pyramid_to_line (array_to_sort, SCREEN, SCREEN_SIZE):

        # //////////////////////
        # remove sin or cos from one axis
        # /////////////////////
        print("abc")
    
        