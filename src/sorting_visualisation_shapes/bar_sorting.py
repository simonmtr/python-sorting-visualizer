from sorting_visualisation_shapes.sorting_visualisation_A import SortingVisualisationA
from helper.global_helper import GlobalHelper

class BarSorting(SortingVisualisationA):
    def __init__(self, screensize) -> None:
        super().__init__()
        # set middle of circle according to current position
        self.screensize = screensize
        self.x_distance_to_border = 1/20 * screensize[0]
        self.y_distance_to_border = 1/20 * screensize[1]
        self.bar_height_multiplicator = (screensize[0] - self.x_distance_to_border * 2)/GlobalHelper.get_array_to_sort_size()
        self.bar_width = (screensize[0] - 2 * self.x_distance_to_border) / GlobalHelper.get_array_to_sort_size()
    def get_coordinates(self, value, index):
        x = index * self.bar_width + self.x_distance_to_border
        y = self.y_distance_to_border
        return [x,y]
    def get_height(self, value):
        print("value")
        print(value)
        print("height multiplicator")
        print(self.bar_height_multiplicator)
        return self.bar_height_multiplicator * value / 2
