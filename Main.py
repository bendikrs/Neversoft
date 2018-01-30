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
from images import *

kjøkenet_img = pg.image.load("images/kjøkenet_img.png")
badet_img = pg.image.load("images/badet_img.png")
gangen_img = pg.image.load("images/gangen_img.png")
soverommet_img = pg.image.load("images/soverommet_img.png")
stova_img = pg.image.load("images/stova_img.png")
garasja_img = pg.image.load("images/garasja_img.png")
pg.init()
W, H = 800, 600
boxWidth, boxHeight = W - 10, 40

FONT = pg.font.SysFont("lucidaconsole", 15)
TEXT_COLOR = pg.Color("White")


screen = pg.display.set_mode((W, H))
input_box1 = InputBox(5, H-boxHeight-5, boxWidth, boxHeight)
posX = 0
posY = 0

 # romma
Kjøkenet = Rooms("Kjøkenet.", "ost.",
"golvflisa under deg og noko vått under foten.",
"gamalt grillkrydder og noko som minner litt om gamal banan.",
"skitne kaseroller og asjettar. På golvet ligg eit bananskal.",
"takvifta som snurrar og ein pakke leverpostei som råtnar.",
"treff taklampa. I det du treff bakken, klirrar det i asjettane.")
Stova = Rooms("Stova","drit",
"vegg-til-vegg-teppet under deg. Nokon har sølt noko som har tørka og blitt stivt",
"Pepsi Max og ostepop. Sofaen smakar ræv.",
"Eit vegg-til-vegg-teppe og ein sliten sofa. Golvet og veggane er flekkete.",
"kakerlakkar under sofaen og sigarettrøyk impregnert i veggane.",
"når du landar lagar golvet ein lyd som minner om ein våt svamp.")
Garasja = Rooms("Garasja", "spylevæske og svette","","","","","")
Badet = Rooms("Badet", "urin og mugg","","","","","")
Gangen = Rooms("Gangen", "sure sko og kattemat","","","","","")
Soverommet = Rooms("Soverommet", "sæd og morgenånde","","","","","")

roomList = [[[Garasja, 0, 0, garasja_img],[Soverommet, 0, 1, soverommet_img]]
            ,[[Gangen, 1, 0, gangen_img],[Stova, 1, 1, stova_img]],
            [[Badet, 2, 0, badet_img],[Kjøkenet, 2, 1, kjøkenet_img]]]

class App:

    def __init__(self):
        self._running = True
        self.clock = pg.time.Clock()
        self.posY = posY
        self.posX = posX
        self.screenText = "Bruk sansane til å utforske huset"

        pg.display.set_caption("Neversoft inc.") #

        pg.mixer.music.load("bensound-psychedelic.mp3")
        pg.mixer.music.play(-1, 0.0)
        #
        # pg.mixer.pre_init(44100, 16, 2, 4096) #
        # soundObj = pg.mixer.music("beep.wav") # Legg til musikk i bakgrunnen
        # soundObj.play()                       #
        #
        #
    def on_event(self, event): # Her skjer all input
        if event.type == pg.QUIT:
            self._running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self._running = False

        # returnTxt er inputen frå spelaren etter han har trykt enter
        returnTxt = input_box1.handle_event(event)


        # Her skjer all forflytting av karakteren
        if "gå" in str(returnTxt):

            if "nord" in str(returnTxt):
                self.posY += 1
            elif "vest" in str(returnTxt):
                self.posX -= 1
            elif "aust" in str(returnTxt):
                self.posX += 1
            elif "sør" in str(returnTxt):
                self.posY -= 1
            else:
                self.screenText = "Du må velje ei retning."
                return
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
                # printar posisjonen til karakteren
                print("X posisjon:" + str(self.posX) + " Y posisjon:" + str(self.posY))
                # om koordinatane er gyldige så rendra denne __str__ til objektet i klassa Rooms
                if self.posX >= 0 and self.posY >= 0:
                    self.screenText = roomList[self.posX][self.posY][0]

        # Her ligg dei andre sansane
        if "lukt" in str(returnTxt):
            self.screenText = roomList[self.posX][self.posY][0].Roomsmell()
        if "kjenn" in str(returnTxt):
            self.screenText = roomList[self.posX][self.posY][0].Roomfeel()
        if "smak" in str(returnTxt):
            self.screenText = roomList[self.posX][self.posY][0].Roomtaste()
        if "sjå" in str(returnTxt):
            self.screenText = roomList[self.posX][self.posY][0].Roomlook()
        if "hør" in str(returnTxt):
            self.screenText = roomList[self.posX][self.posY][0].Roomsound()
        if "hopp" in str(returnTxt):
            self.screenText = roomList[self.posX][self.posY][0].Roomjump()





    def on_loop(self): # Her legg vi alt som skal skje kvar gong bilete blir oppdatert

        self.clock.tick(30)
        screen.blit((roomList[self.posX][self.posY][3]),(0,0))
        input_box1.draw(screen)
        screen.blit(FONT.render(str(self.screenText), True, TEXT_COLOR), (35, 450))
        pg.display.update()

    def on_cleanup(self): # Denne metoden køyrer når spelet blir avslutta
        pg.quit()

    def on_execute(self):
        while( self._running ): # Dette er game loopen som køyrer heile tida spelet køyrer
            for event in pg.event.get():
                self.on_event(event)
            self.on_loop()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
