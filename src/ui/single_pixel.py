from json.tool import main
import pygame

class SinglePixel:
    def __init__(self, screen, color, x,y):
        self.screen = screen
        self.color = color
        self.pixel_size = 10 # GlobalHelper.get_pixel_size()    
        self.x = x
        self.y = y
    def draw_pixel(self):
        pygame.draw.circle(self.screen, self.color, (self.x,self.y), self.pixel_size)
    def update_many(single_pixels, screen):
        screen.fill(0)
        for sp in single_pixels:
            sp.draw_pixel()
        pygame.display.update()
