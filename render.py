import pygame
from pygame.locals import *
from Main import *

White = (255,255,255)
Black = (0,0,0)

class Render(App):
    def __init__(self):
        super().__init__(self)

    pygame.display.set_mode().fill((White))

# screen.fill((white))
