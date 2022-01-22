import random
class obstacle():
    def __init__(self):
        self.LIMIT_MAX = 21
        self.LIMIT_MIN = 13
        self.apparence = 'X'
        self.obstacles = []
        self.position = []

    def createObstacles(self):
        random_amount = random.randrange(self.LIMIT_MIN, self.LIMIT_MAX)
        for i in range(random_amount):
            self.obstacles.append(self.apparence)
        
    def setPositions(self,x,y):
        for i in self.obstacles:
            randomPosX = random.randrange(0,x)
            randomPosY = random.randrange(0,y)
            randomPos = str(randomPosX),str(randomPosY)
            self.position.append(randomPos)