from abc import ABC, abstractmethod
from helper.global_helper import GlobalHelper
from ui.rgb_handling import RGBHandling

class Shape(ABC):
    @abstractmethod
    def __init__(self, value, index, ui, sorting_visualization_a) -> None:
        self.value = value
        self.index = index
        self.ui = ui
        self.x = sorting_visualization_a.get_coordinates(value, index)[0]
        self.y = sorting_visualization_a.get_coordinates(value, index)[1]
        self.sorting_visualization_a = sorting_visualization_a
        self.color = RGBHandling.get_rgb_color(GlobalHelper.get_array_to_sort_size(), value)
    @abstractmethod
    def draw(self):
        pass
    @abstractmethod
    def update_value(self, value, index):
        self.value = value
        self.index = index
        new_coordinates = self.sorting_visualization_a.get_coordinates(value, index)
        self.x = new_coordinates[0]
        self.y = new_coordinates[1]
        self.draw()