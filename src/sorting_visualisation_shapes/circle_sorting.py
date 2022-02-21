import math

from sorting_visualisation_shapes.sorting_visualisation_A import SortingVisualisationA
from helper.global_helper import GlobalHelper

class CircleSorting(SortingVisualisationA):
    def __init__(self, screensize) -> None:
        super().__init__()
        self.step = 360/GlobalHelper.get_array_to_sort_size()
        self.middle_of_screen_x = screensize[0]/2
        self.middle_of_screen_y = screensize[1]/2
        self.pixel_multiplicator = 3 * GlobalHelper.get_pixel_size()
    def get_coordinates(self, value, index):
        display_percentage_of_radius = self.get_display_percentage_of_radius(value, index)
        x = (self.middle_of_screen_x - self.pixel_multiplicator) * math.cos(self.step * value) * display_percentage_of_radius + self.middle_of_screen_x 
        y = (self.middle_of_screen_y - self.pixel_multiplicator) * math.sin(self.step * value) * display_percentage_of_radius + self.middle_of_screen_y
        return [x,y]
    def get_display_percentage_of_radius(self, value, index): # maybe array to sort.value
        worst_case_index_difference = value
        if value > GlobalHelper.get_array_to_sort_size()/2:
            worst_case_index_difference = value
        else: # value < len(array_to_sort)/2
            worst_case_index_difference=GlobalHelper.get_array_to_sort_size()-value
        return 1 - (abs(value-index))/worst_case_index_difference     