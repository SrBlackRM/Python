class soldiers():
    def __init__(self, life, shootAmount, skill):
        self.life = life
        self.shootAmount = shootAmount
        self.skill = skill
        
        self.position = []

        self.skillCast(skill)

    def skillCast(self, skill):
        if skill == 'resistente':
            pass
        elif skill == 'cura':
            pass
        elif skill == 'furia':
            pass
    
    def setPosition(self,x,y):
        self.position.append((x,y))

    def shoot(self):
        self.shootVector = []

        def createShoot():
            for i in range(0,self.shootAmount):
                self.shootVector.append('*')
        
        createShoot()
    
    
    def takeDamage(self,someShootAmount):
            self.life -= someShootAmount

'''
tank = soldier(3,1,'resistente')
tank.setPosition(100,230)
medic = soldier(1,1,'cura')
medic.setPosition(150,231)
assalt = soldier(1,2,'furia') 
assalt.setPosition(423,320)      

print(f'TANK - Vida: {tank.life}, Qnt Tiros: {tank.shoot}, Habilidade: {tank.skill}, Posição: {tank.position}')
print(f'MEDICO - Vida: {medic.life}, Qnt Tiros: {medic.shoot}, Habilidade: {medic.skill}, Posição: {medic.position}')
print(f'ASSALTO - Vida: {assalt.life}, Qnt Tiros: {assalt.shoot}, Habilidade: {assalt.skill}, Posição: {assalt.position}')
'''