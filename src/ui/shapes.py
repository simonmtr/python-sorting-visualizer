import math
import pygame
from ui.single_pixel import SinglePixel

class Shapes:
    def circle(screen, array_to_sort, x, y):
        # each dot's distance from the outer circle is how incorrect of a position the number that dot represent is.
        # for example, if 1 is the smallest number in the array and it is currently in position 500 of 1000, it is in the
        # worst possible position, so it will be in the center of the screen, the farthest from its ideal position in the outer circle

        
        single_pixels = []
        step = 360/len(array_to_sort)
        angle = 0
        # initial painting values

        for i in range(len(array_to_sort)):
            x -= math.sin(angle*math.pi/180) * step
            y += math.cos(angle*math.pi/180) * step
            angle += 10
            single_pixels.append(SinglePixel(screen, "orange", x, y))
        return single_pixels








#RECTANGLE BELOW

# #sorting_array = np.random.choice(range(40), size=(40), replace=False)
# print(sorting_array)
# quarter_sorting_array = len(sorting_array)/4
# single_pixels = []
# x, y = quarter_sorting_array,quarter_sorting_array
# pixel_size = 5
# step = 0 # pixel size
# for i in range(len(sorting_array)):
#     # x and y value depend on where on the rectangle you are
#     y = 0
#     x = 0
#     print(i)
#     if i == quarter_sorting_array or i == quarter_sorting_array*2 or i == quarter_sorting_array*3:
#         print("reseting steps")
#         step=0
#     if i < quarter_sorting_array:
#         y = 0
#         x = x*pixel_size + step
#     elif i<quarter_sorting_array*2:
#         y = y + step
#         x=quarter_sorting_array*pixel_size
#     elif i<quarter_sorting_array*3:
#         y=quarter_sorting_array*pixel_size
#         x=(quarter_sorting_array*pixel_size)-step
#     else:
#         y=(quarter_sorting_array*pixel_size)-step
#         x=0
#     step += 5
#     # y += i * step 
#     single_pixels.append(SinglePixel(screen, "orange",x,y))
#     print(f"appended pixel at {x} and {y}")

# while MAIN_LOOP:
#     pygame.display.set_caption("simonmtr sorting visualizaton")
#     KEY = KEY_INPUTS()
#     if KEY == "ESCAPE":
#         MAIN_LOOP = False
#         pygame.quit()
#         sys.exit()
#     screen.fill(0)
#     for sp in single_pixels:
#         sp.update(sp.rect.x,sp.rect.y)
#     pygame.display.update()