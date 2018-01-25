import pygame as pg
from pygame.locals import *

pg.init()
BOX_COLOR = pg.Color("Black")
FONT = pg.font.SysFont("lucidaconsole", 28)

class InputBox:

    def __init__(self, x, y, w, h, text='>'):
        self.rect = pg.Rect(x, y, w, h)
        self.color = BOX_COLOR
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = True
        self.x = x
    def handle_event(self, event):

        if event.type == pg.KEYDOWN:
            if self.active:
                returnText = ""
                if event.key == pg.K_RETURN:
                    returnText = self.text
                    print(self.text)
                    self.text = ""
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
                return returnText.split()

    def draw(self, screen):
        width = self.x
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
