import pygame as pg
from pygame.locals import *
from classes.items import *
from classes.rooms import *
from classes.textInput import *
from render import *
import time
import random as r

pg.init()
W, H = 800, 600
boxWidth, boxHeight = W - 10, 40

screen = pg.display.set_mode((W, H))
input_box1 = InputBox(5, H-boxHeight-5, boxWidth, boxHeight)
posX = 0
posY = 0

 # romma
Kjøkenet = Rooms("Kuk", "Rommet lukta ost.")
Stova = Rooms("Stova","Dritlukt")


roomList = [[[Kjøkenet, 0, 0],["Garasja", 1, 0]],[[Stova, 0, 1],["Badet", 0, 2]]]




class App:

    def __init__(self):
        self._running = True
        self.clock = pg.time.Clock()

        pg.display.set_caption("Neversoft inc.") #

        pg.mixer.pre_init(44100, 16, 2, 4096) #
        soundObj = pg.mixer.Sound("beep.wav") # Legg til musikk i bakgrunnen
        soundObj.play()

        self.posY = posY
        self.posX = posX

    def on_event(self, event): # Her skjer all input
        if event.type == pg.QUIT:
            self._running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self._running = False

        # returnTxt er inputen frå spelaren etter han har trykt enter
        returnTxt = input_box1.handle_event(event)


        # Her skjer all forflytting av karakteren
        if "go" in str(returnTxt):
            if "north" in str(returnTxt):
                self.posY += 1
            elif "west" in str(returnTxt):
                self.posX -= 1
            elif "east" in str(returnTxt):
                self.posX += 1
            elif "south" in str(returnTxt):
                self.posY -= 1


            print("X posisjon:" + str(self.posX) + " Y posisjon:" + str(self.posY))
            print(roomList[self.posX][self.posY][0])



        # Denne biten forhindrar spelaren å gå utanfor bana, variablane ligg i room.py
        offBoundsMsg = offBoundsMsgs[r.randint(0, len(offBoundsMsgs)- 1 )]
        if self.posX < 0:
            print(offBoundsMsg)
            self.posX = 0
        if self.posX > roomSizeX:
            print(offBoundsMsg)
            self.posX -= 1

        if self.posY < 0:
            print(offBoundsMsg)
            self.posY = 0
        if self.posY > roomSizeY:
            print(offBoundsMsg)
            self.posY -= 1




    def on_loop(self): # Her legg vi alt som skal skje kvar gong bilete blir oppdatert


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
