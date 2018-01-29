import random as r


offBoundsMsgs = ["Der er ikkje noko i den retninga.", "Du møtte ein vegg.", "Du kjem deg ikkje vidare i den retninga."]


roomSizeX, roomSizeY = 3, 3

class Rooms:
    # Dette er baseklassa til allle romma
    def __init__(self, name, smell):
        self.name = name
        self.smell = smell
        # return roomDict[currentRoom]

    def __str__(self):
        # opt = r.randint(0,4)
        # if opt == 0:
        #     return "Du kjem inn i {}.".format(self.name)
        # elif opt == 1:
        #     return "Du opnar døra og kjem inn i {}.".format(self.name)
        # elif opt == 2:
        #     return "Du er no komen inn i {}.".format(self.name)
        # else:
            return "Du er no i {}.".format(self.name)
    def Roomsmell(self):
        return self.smell




# Her er alle romma som er med i spelet
