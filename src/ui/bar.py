import pygame

from ui.shape_A import Shape

class Bar(Shape):
    def __init__(self, value, index, ui, sorting_visualization_a) -> None:
        super().__init__(value, index, ui, sorting_visualization_a)
        print("values for rect")
        print(self.sorting_visualization_a.bar_width)
        height = self.sorting_visualization_a.get_height(value)
        print("=================")
        print(height)
        self.rect = pygame.Rect(self.x, self.y, self.sorting_visualization_a.bar_width, height)
    def draw(self):
        self.rect = pygame.draw.rect(self.ui.screen, self.color, self.rect)
        pygame.display.update()
    def update_value(self, value, index):
        return super().update_value(value, index)
        