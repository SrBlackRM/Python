import soldier

#CRIA AS CLASSES DE SOLDADOS
tankSoldier = soldier.soldiers(3,1,'lifeSteal')
assaultSoldier = soldier.soldiers(1,2,'positionChange')
medicSoldier = soldier.soldiers(1,1,'lifeHeal')
normalSoldier = soldier.soldiers(1,1,'none')


def attack(whoshoot,whodie):
    whoshoot.shoot()
    whodie.takeDamage(whoshoot.shootAmount)

'''
print(tankSoldier.life)
attack(assaultSoldier,tankSoldier)
print(tankSoldier.life)
print(assaultSoldier.life)
'''