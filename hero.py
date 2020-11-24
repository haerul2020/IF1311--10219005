class Hero:

    jumlah = 0

    def __init__(self,inputName,inputHealth,inputPower,inputArmor):

        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1

    #void function, method return, tanpa argumen
    def siapa(self):
        print('namaku adalah ' + self.name)

    #method dengan argumen, tanpa return
    def healthUp(self,up):
        self.health += up

    #method dengan return
    def getHealth(self):
        return self.health
hero1 = Hero("sniper",100, 15, 4)
hero2 = Hero("mirana",100, 10, 5)
hero1 = Hero("naruto",1000, 100, 3)

hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())
