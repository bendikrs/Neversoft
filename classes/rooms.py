import random as r


offBoundsMsgs = ["Der er ikkje noko i den retninga.", "Du møtte ein vegg.", "Du kjem deg ikkje vidare i den retninga."]


roomSizeX, roomSizeY = 2, 1

class Rooms:
    # Dette er baseklassa til allle romma
    def __init__(self, name, smell):
        self.name = name
        self.smell = smell
    

    def __str__(self):
            return "Du er no i {}.".format(self.name)

    def Roomsmell(self):
        return "Rommet luktar {}.".format(self.smell)
