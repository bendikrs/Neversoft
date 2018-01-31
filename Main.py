import pygame as pg
from pygame.locals import *
from classes.items import *
from classes.rooms import *
from classes.textInput import *
import time
import random as r
import sys
import os.path
from images import *
# from wraptest import *

kjøkenet_img = pg.image.load("images/kjøkenet_img.png")
badet_img = pg.image.load("images/badet_img.png")
gangen_img = pg.image.load("images/gangen_img.png")
soverommet_img = pg.image.load("images/soverommet_img.png")
stova_img = pg.image.load("images/stova_img.png")
garasja_img = pg.image.load("images/garasja_img.png")
pg.init()
W, H = 800, 600
boxWidth, boxHeight = W - 10, 40

scrArr = []

txtArea = pg.Rect(35,450,500,200)
FONT_SIZE = 15
FONT = pg.font.SysFont("lucidaconsole", FONT_SIZE)
TEXT_COLOR = pg.Color("White")


screen = pg.display.set_mode((W, H))
input_box1 = InputBox(5, H-boxHeight-5, boxWidth, boxHeight)
posX = 0
posY = 0

 # romma

Kjøkenet = Rooms("kjøkenet",
"mygla polarbrød og brent grandiosa",
"golvflisa under deg og noko vått under foten",
"gamalt grillkrydder og noko som minner litt om brun banan",
"skitne kaseroller og asjettar. På golvet ligg eit bananskal",
"takvifta som snurrar og ein pakke leverpostei som råtnar",
"treff taklampa. I det du treff bakken, klirrar det i asjettane")
Stova = Rooms("stova",
"drit",
"vegg-til-vegg-teppet under deg. Nokon har sølt noko som har tørka og blitt stivt",
"Pepsi Max og ostepop. Sofaen smakar ræv",
"Eit vegg-til-vegg-teppe og ein sliten sofa. Golvet og veggane er flekkete",
"kakerlakkar under sofaen og sigarettrøyk impregnert i veggane",
"når du landar lagar golvet ein lyd som minner om ein våt svamp")
Garasja = Rooms("garasja",
"spylevæske og svette",
"det kalde betonggolvet under sokkelestane. Du kjenner på bilen. Den er nypolert",
"grus og motorolje. Bilen smakar såpe",
"ein knallraud Saab 9-5,  antakelig frå rundt tusenårsskifte. Rundt bilen flyt det olje og spylevæske",
"ein sildrande bekk av diverse drit som flyt ut garasjeporten",
"beina forlet bakken. Etter kvart landar dei på bakken att. Du synes at hoppet gjekk nokså greitt")
Badet = Rooms("badet",
"urin, mugg, dobbel dusch og ei dobørste som skulle ha blitt bytta for lenge sidan",
"at golvet er betrakteleg meir klissete rundt doen. Badekaret er fylt med ei hårete masse",
'"kroppens fornødenheter" og ein ukjent smak frå badekaret',
"at all flisa er dekt av flekkar i diverse fargar. I badekaret ligg noko grønt",
"det du trur er den hårete massen i badekaret som veks",
"sklir i det du landar. Du riv med deg dusjforhenget på veg ned")
Gangen = Rooms("gangen",
"sure sko og kattemat",
"at det er lenge sidan du har vaska deg bak øyrene. Du skriv det ned på ein lapp",
"lim. Du konkluderer med at dei ikkje er ferdige med å pusse opp rommet",
"nokre flotte gummistøvlar. Du prøver dei på, men konkluderer med at dei ikkje passar",
"ikkje ein drit",
'og ned fleire gongar. Du tørkar deg i panna og tenkjer "det var dagens trim"')
Soverommet = Rooms("soverommet",
"sæd, morgenånde og vannmelon",
"at du blir litt svimmel. Det er i grunnen ganske digg",
"sæd som av ein eller annan grunn virkar avhengigheitsdannande",
"ikkje stort. Nokon har dampa fullt heile rommet",
"skinnjakka di som knirkar. Ho er enda ikkje gådd inn",
"flyg ut vindauget. Etter kvart kjem du til sansane att, og oppdagar at du framleis er i rommet")


roomList = [[[Garasja, 0, 0, garasja_img],[Soverommet, 0, 1, soverommet_img]]
            ,[[Gangen, 1, 0, gangen_img],[Stova, 1, 1, stova_img]],
            [[Badet, 2, 0, badet_img],[Kjøkenet, 2, 1, kjøkenet_img]]]

goList = ["gå","go", "walk", "move","spaser"]
northList = ["nord", "north", "opp", "up", "åpp"]
southList = ["sør", "south", "ned", "down", "syd"]
eastList = ["aust", "øst", "east","høyre", "høgre"]
westList = ["vest", "venstre","west", "left", "heim"]

smellList = ["lukt", "smell", "innhaler"]
feelList = ["kjenn", "føl", "ta"]
tasteList = ["smak", "slikk", "sug"]
lookList = ["sjå", "se", "see"]
soundList = ["lytt", "hør", "listen"]
jumpList = ["hopp", "jump", "flyg"]

class App:

    def __init__(self):
        self._running = True
        self.clock = pg.time.Clock()
        self.posY = posY
        self.posX = posX
        self.screenText = "Bruk sansane til å utforske huset"

        pg.display.set_caption("Neversoft inc.") #

        icon = pg.image.load('images.OR_ICON.png')    # legg til ikon
        pg.display.set_icon(icon)

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
        for word in goList:
            if word in str(returnTxt):
                for i in range(len(northList)):
                    if northList[i] in str(returnTxt):
                        self.posY += 1
                        break
                    elif westList[i] in str(returnTxt):
                        self.posX -= 1
                        break
                    elif eastList[i] in str(returnTxt):
                        self.posX += 1
                        break
                    elif southList[i] in str(returnTxt):
                        self.posY -= 1
                        break
                    if i >= len(northList):
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
                break

        # Her ligg dei andre sansane
        for word in smellList:
            if word in str(returnTxt):
                self.screenText = roomList[self.posX][self.posY][0].Roomsmell()
        for word in feelList:
            if word in str(returnTxt):
                self.screenText = roomList[self.posX][self.posY][0].Roomfeel()
        for word in tasteList:
            if word in str(returnTxt):
                self.screenText = roomList[self.posX][self.posY][0].Roomtaste()
        for word in lookList:
            if word in str(returnTxt):
                self.screenText = roomList[self.posX][self.posY][0].Roomlook()
        for word in soundList:
            if word in str(returnTxt):
                self.screenText = roomList[self.posX][self.posY][0].Roomsound()
        for word in jumpList:
            if word in str(returnTxt):
                self.screenText = roomList[self.posX][self.posY][0].Roomjump()


    def on_loop(self): # Her legg vi alt som skal skje kvar gong bilete blir oppdatert

        scrArr = str(self.screenText).split()
        self.clock.tick(30)
        screen.blit((roomList[self.posX][self.posY][3]),(0,0))
        input_box1.draw(screen)

        screen.blit(FONT.render(" ".join(scrArr[:9]), True, TEXT_COLOR), (30, 450))
        screen.blit(FONT.render(" ".join(scrArr[9:18]), True, TEXT_COLOR), (30, 450+5+FONT_SIZE))
        screen.blit(FONT.render(" ".join(scrArr[18:]), True, TEXT_COLOR), (30, 450+5+5+FONT_SIZE+FONT_SIZE))
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
