from ui.shape_A import Shape
import pygame
from helper.global_helper import GlobalHelper



class Pixel(Shape):
    def __init__(self, value, index, ui, sorting_visualization_a) -> None:
        super().__init__(value, index, ui, sorting_visualization_a)
        self.pixel = ""
        self.sorting_visualisation_a = sorting_visualization_a
    def draw(self):
        self.pixel = pygame.draw.circle(self.ui.screen, self.color, (self.x, self.y), GlobalHelper.get_pixel_size())
        pygame.display.update()
        print("pixel created")
    def update_value(self, value, index):
        return super().update_value(value, index)