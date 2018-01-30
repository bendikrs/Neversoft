import random as r


offBoundsMsgs = ["Der er ikkje noko i den retninga.", "Du møtte ein vegg.", "Du kjem deg ikkje vidare i den retninga."]


roomSizeX, roomSizeY = 2, 1

class Rooms:
    # Dette er baseklassa til allle romma
    def __init__(self, name, smell, feel, taste, look, sound, jump):
        self.name = name
        self.smell = smell
        self.feel = feel
        self.taste = taste
        self.look = look
        self.sound = sound
        self.jump = jump

    def __str__(self):
            return "Du er no i {}.".format(self.name)

    def Roomsmell(self):
        return "Rommet luktar {}.".format(self.smell)
    def Roomfeel(self):
        return "Du kjenner {}.".format(self.feel)
    def Roomtaste(self):
        return "Du sleikjer rundt om i rommet og kjenner smaken av {}.".format(self.taste)
    def Roomlook(self):
        return "Du ser rundt i rommet og ser {}.".format(self.look)
    def Roomsound(self):
        return "Om du er heilt stille kan du høre lyden av {}.".format(self.sound)
    def Roomjump(self):
        return "Du hoppar opp og {}.".format(self.jump)
