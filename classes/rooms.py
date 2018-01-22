import random

class Rooms:
    # Dette er baseklassa til allle romma
    def __init__(self, name, posX, posY):
        self.name = name
        self.posX = posX
        self.posY = posY

    def __str__(self):
        opt = random.randint(0,4)
        if opt == 0:
            return "Du kjem inn i {}.".format(self.name)
        elif opt == 1:
            return "Du opnar døra og kjem inn i {}.".format(self.name)
        elif opt == 2:
            return "Du er no kem inn i {}.".format(self.name)
        else:
            return "Du er no i {}.".format(self.name)


Kjøkenet = Rooms("Kjøkenet", 1, 1)

print(Kjøkenet. posX)
