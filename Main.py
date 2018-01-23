import pygame
from pygame.locals import *
from classes.items import *
from classes.rooms import *
from render import *
import time

class App:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 1200, 800
        self.clock = pygame.time.Clock()
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size)
        pygame.display.set_mode().fill(colorDict["darkblue"])
        pygame.display.set_caption("Neversoft inc.")

        pygame.mixer.pre_init(44100, 16, 2, 4096) #
        soundObj = pygame.mixer.Sound("beep.wav") # Legg til musikk i bakgrunnen
        soundObj.play()                           #
		# self.clock = pygame.time.Clock()


    def on_event(self, event): # Her skjer all input
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._running = False

            elif event.key == pygame.K_k:
                print(Kjøkenet)


    def on_loop(self): # Her legg vi alt som skal skje kbar gong bilete blir oppdatert

        pygame.display.update()

    def on_cleanup(self): # Denne metoden køyrer når spelet blir avslutta
        pygame.quit()

    def on_execute(self):
        while( self._running ):         # Dette er game loopen som køyrer heile tida spelet køyrer
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()


    #
    #
    # pygame.init()
    # screen = pygame.display.set_mode((400, 300))
    # done = False
    # is_blue = True
    # x = 30
    # y = 30
    #
    # pygame.display.set_caption('Neversoft inc.')
    # clock = pygame.time.Clock()
    #
    # while not done:
    #         for event in pygame.event.get():
    #                 if event.type == pygame.QUIT:
    #                         done = True
    #                 if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    #                         is_blue = not is_blue
    #                 if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
    #                         done = True
    #
    #         pressed = pygame.key.get_pressed()
    #         if pressed[pygame.K_UP]:
    #             y -= 3
    #         if pressed[pygame.K_DOWN]:
    #             y += 3
    #         if pressed[pygame.K_LEFT]:
    #             x -= 3
    #         if pressed[pygame.K_RIGHT]:
    #             x += 3
    #
    #         screen.fill((0, 0, 0))
    #         if is_blue:
    #             color = (0, 128, 255)
    #         else:
    #             color = (255, 100, 0)
    #         pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
    #
    #         pygame.display.flip()
    #         clock.tick(60)
