import pygame
import soldier
import obstacle
import vehicle

pygame.init()

class battlefield():
    def __init__(self):
        self.fieldSizeX = 640
        self.fieldSizeY = 480
        self.screen = pygame.display.set_mode((self.fieldSizeX,self.fieldSizeY))
        pygame.display.set_caption('Guerrilha')

        self.obstacle_camp = obstacle.obstacle()

        self.addcampObstacles()
        self.addcampSoldiersPlayer()
        self.addcampVeihclePlayer()

    def addcampObstacles(self):
        self.obstacle_camp.createObstacles()      
        self.obstacle_camp.setPositions(self.fieldSizeX,self.fieldSizeY)  

    def addcampVeihclePlayer(self):
        pass

    def addcampSoldiersPlayer(self):
        soldier.tank.setPosition(100,230)
        soldier.medic.setPosition(100,230)
        soldier.assalt.setPosition(100,230)

    def showObstacles(self):
        print(f'{self.obstacle_camp.obstacles} \n {len(self.obstacle_camp.obstacles)}')
        print(f'posição de cada: {self.obstacle_camp.position}')

    def showVeihclePlayer(self):
        pass

    def showSoldiersPlayer(self):
        pass




