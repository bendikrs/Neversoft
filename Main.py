import pygame as pg
from pygame.locals import *
from classes.items import *
from classes.rooms import *
from classes.textInput import *
from render import *
import time
import random as r
import sys
import os.path

kitchenimg = pg.image.load("speletbase.png")
pg.init()
W, H = 800, 600
boxWidth, boxHeight = W - 10, 40

FONT = pg.font.SysFont("lucidaconsole", 26)
TEXT_COLOR = pg.Color("White")


screen = pg.display.set_mode((W, H))
input_box1 = InputBox(5, H-boxHeight-5, boxWidth, boxHeight)
posX = 0
posY = 0

 # romma
Kjøkenet = Rooms("Kjøkenet", "Rommet luktar ost.")
Stova = Rooms("Stova","Rommet luktar drit")
Garasja = Rooms("Garasja", "Rommet luktar spylevæske og svette")
Badet = Rooms("Badet", "Rommet luktar urin og mugg")
Gangen = Rooms("Gangen", "Rommet luktar sure sko og kattemat")
Soverommet = Rooms("Soverommet", "Rommet luktar sæd og morgenånde")

roomList = [[[Garasja, 0, 0, kitchenimg],[Soverommet, 0, 1]]
            ,[[Gangen, 1, 0],[Stova, 1, 1]],[[Badet, 2, 0],[Kjøkenet, 2, 1]]]

class App:

    def __init__(self):
        self._running = True
        self.clock = pg.time.Clock()

        pg.display.set_caption("Neversoft inc.") #

        # pg.mixer.pre_init(44100, 16, 2, 4096) #
        # soundObj = pg.mixer.Sound("beep.wav") # Legg til musikk i bakgrunnen
        # soundObj.play()                       #

        self.posY = posY
        self.posX = posX
        self.screenText = ""

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

            # Denne biten forhindrar spelaren å gå utanfor bana, variablane ligg i room.py
            offBoundsMsg = offBoundsMsgs[r.randint(0, len(offBoundsMsgs)- 1 )]
            if self.posX < 0:
                print(offBoundsMsg)
                self.screenText = ''
                self.screenText = offBoundsMsg
                self.posX = 0
                pass
            elif self.posX > roomSizeX:
                print(offBoundsMsg)
                self.screenText = ''
                self.screenText = offBoundsMsg
                self.posX -= 1
                pass
            elif self.posY < 0:
                print(offBoundsMsg)
                self.screenText = ''
                self.screenText = offBoundsMsg
                self.posY = 0
                pass
            elif self.posY > roomSizeY:
                print(offBoundsMsg)
                self.screenText = ''
                self.screenText = offBoundsMsg
                self.posY -= 1
                pass

            else:
                print("X posisjon:" + str(self.posX) + " Y posisjon:" + str(self.posY))
                if self.posX >= 0 and self.posY >= 0:
                    self.screenText = roomList[self.posX][self.posY][0]




        # if "smell" in str(returnTxt):
        #     self.screenText = roomList([self.posX][self.posY][0]).Roomsmell
        #


    def on_loop(self): # Her legg vi alt som skal skje kvar gong bilete blir oppdatert

        self.clock.tick(30)
        screen.fill(colorDict["darkblue"])
        #screen.blit((roomList[self.posX][self.posY][3]),(0,0))
        input_box1.draw(screen)
        screen.blit(FONT.render(str(self.screenText), True, TEXT_COLOR), (35, 450))
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
