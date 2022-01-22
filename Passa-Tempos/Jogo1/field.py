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
        self.screenBackground = pygame.image.load('imgs/battlefield.jpg')
        pygame.display.set_caption('Guerrilha')
        self.screen.blit(pygame.transform.scale(self.screenBackground,(self.fieldSizeX,self.fieldSizeY)),(0,0))

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
        pass

    def showObstacles(self):
        print(f'{self.obstacle_camp.obstacles} \n {len(self.obstacle_camp.obstacles)}')
        print(f'posição de cada: {self.obstacle_camp.position}')
        

    def showVeihclePlayer(self):
        pass

    def showSoldiersPlayer(self):
        pass




