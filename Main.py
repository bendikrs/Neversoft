import pygame as pg
from pygame.locals import *
from classes.items import *
from classes.rooms import *
from classes.textInput import *
from render import *
import time

pg.init()
w, h = 1200, 800
boxWidth, boxHeight = 140, 35

screen = pg.display.set_mode((w, h))
input_box1 = InputBox(1, h-boxHeight-1, boxWidth, boxHeight)


class App:

    def __init__(self):
        self._running = True
        # self._display_surf = None
        # self.size = self.width, self.height = 1200, 800
        # self._display_surf = pg.display.set_mode(self.size)
        self.clock = pg.time.Clock()

        pg.display.set_caption("Neversoft inc.")

        pg.mixer.pre_init(44100, 16, 2, 4096) #
        soundObj = pg.mixer.Sound("beep.wav") # Legg til musikk i bakgrunnen
        soundObj.play()                           #
		# self.clock = pg.time.Clock()



    def on_event(self, event): # Her skjer all input
        if event.type == pg.QUIT:
            self._running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self._running = False

            elif event.key == pg.K_k:
                print(Kjøkenet)

        input_box1.handle_event(event)

    def on_loop(self): # Her legg vi alt som skal skje kbar gong bilete blir oppdatert

        input_box1.update()
        pg.display.set_mode().fill(colorDict["darkblue"])
        input_box1.draw(screen)

        pg.display.update()

    def on_cleanup(self): # Denne metoden køyrer når spelet blir avslutta
        pg.quit()

    def on_execute(self):
        while( self._running ):         # Dette er game loopen som køyrer heile tida spelet køyrer
            for event in pg.event.get():
                self.on_event(event)
            self.on_loop()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()


    #
    #
    # pg.init()
    # screen = pg.display.set_mode((400, 300))
    # done = False
    # is_blue = True
    # x = 30
    # y = 30
    #
    # pg.display.set_caption('Neversoft inc.')
    # clock = pg.time.Clock()
    #
    # while not done:
    #         for event in pg.event.get():
    #                 if event.type == pg.QUIT:
    #                         done = True
    #                 if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
    #                         is_blue = not is_blue
    #                 if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
    #                         done = True
    #
    #         pressed = pg.key.get_pressed()
    #         if pressed[pg.K_UP]:
    #             y -= 3
    #         if pressed[pg.K_DOWN]:
    #             y += 3
    #         if pressed[pg.K_LEFT]:
    #             x -= 3
    #         if pressed[pg.K_RIGHT]:
    #             x += 3
    #
    #         screen.fill((0, 0, 0))
    #         if is_blue:
    #             color = (0, 128, 255)
    #         else:
    #             color = (255, 100, 0)
    #         pg.draw.rect(screen, color, pg.Rect(x, y, 60, 60))
    #
    #         pg.display.flip()
    #         clock.tick(60)
