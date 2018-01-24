playerPosx = 0
playerPosy = 0
gonorth = False

def gonorth():
    global playerPosy
    playerPosy += 1
""""gosouth = playerPos.y -= 1
gowest = playerPos.x -= 1
goeast = playerPos.x += 1"""



randomString = input("Skriv nåke drit: ")

randomList = randomString.split()

if "go" in randomList:
    direction = input("Where do you want to go?")
    if direction == ("north"):
        gonorth()
print (playerPosx, playerPosy)
