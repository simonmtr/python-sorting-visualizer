from ui.shape_A import Shape
import pygame


class Bar(Shape):
    def __init__(self, value, ui, color, x, y, width, height) -> None:
        super().__init__(value, ui, color, x, y)
        self.rect = pygame.Rect(x, y, width, height) # get height as percentage of screen height
    def update_one(self):
        print("updateone")
    def draw(self):
        self.rect = pygame.draw.rect(self.ui.screen, self.color, self.rect)
        pygame.display.update()
        print("bars created")
    def update_value(self, value):
        return super().update_value(value)
        