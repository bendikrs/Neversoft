class Item():
    #baseklasse for alle gjenstandar
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return "Foran deg ligg ei %s. Den %s." % (self.name, self.description)
        # return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description)

class Knife(Item):
    def __init__(self):
        super().__init__(name = "Knife",
                         description = "Looks like it was used recently")

kakespade = Item("kakespade", "ser ut som ei kakespade")

#print (kakespade)
#print (Knife())
