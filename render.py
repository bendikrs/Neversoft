import pygame
from pygame.locals import *
from Main import *

White = (255,255,255)
Black = (0,0,0)

class Render(App):
    def __init__(self):
        super().__init__(self)
    screen = pygame.display.set_mode((self.width, self.height))

    def __str__(self):
        return "{} {}".format(self._display_surf, self.size)

screen.fill((white))
