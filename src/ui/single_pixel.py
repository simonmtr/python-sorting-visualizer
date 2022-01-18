import pygame

class SinglePixel:
    def __init__(self, screen, color,x,y):
        self.screen = screen
        self.color = color
        self.pixel_size = 1
        self.x = x
        self.y = y
    def update(self):
        pygame.draw.circle(self.screen, self.color, (self.x,self.y), self.pixel_size)