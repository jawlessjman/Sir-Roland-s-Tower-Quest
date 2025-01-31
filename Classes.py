from random import randint

'''
Classes
K = knight
W = wizzard
A = Archer
T = Thief
H = cheat code
'''

class HealthPotion:
    def __init__(self, player):
        self.name = "Health Potion"
        self.player = player
        self.healthgained = 15

    def __str__(self):
        return f"{self.name}"

    def usePotion(self):
        if self.player.health == self.player.maxhealth:
            print("\nHealth is already at full\n")
        else:
            self.player.health += self.healthgained
            if self.player.health > self.player.maxhealth:
                self.player.health = self.player.maxhealth
            self.player.inventory.remove(self)
            print(f"\nHealth restored to {self.player.health}/{self.player.maxhealth}\n")

class MagicPotion:
    def __init__(self, player):
        self.name = "Magic Potion"
        self.player = player
        self.magicgained = 15

    def __str__(self):
        return f"{self.name}"

    def usePotion(self):
        if self.player.magic == self.player.maxmagic:
            print("\nMagic is already full\n")
        else:
            self.player.magic += self.magicgained
            if self.player.magic > self.player.maxmagic:
                self.player.magic = self.player.maxmagic
            self.player.inventory.remove(self)
            print(f"\nMagic restored to {self.player.magic}/{self.player.maxmagic}\n")

class Player:

    def __init__(self, name, job):
        self.name = name
        self.job = job
        self.level = 1
        self.xp = 0
        self.xptolevel = 50
        self.health = 1
        self.maxhealth = 0
        self.attack = 0
        self.defense = 0
        self.maxmagic = 0
        self.magic = 0
        self.magicpower = 0
        self.gold = 0
        self.inventory = []
        self.oldhealth = 0
        self.oldmaxhealth = 0
        self.oldattack = 0
        self.olddefense = 0
        self.oldmagic = 0
        self.oldmaxmagic = 0
        self.oldmagicpower = 0
    
    def levelUp(self):
        if self.level * self.xp == self.xptolevel:
            self.level += 1

            self.oldhealth = self.health
            self.oldmaxhealth = self.maxhealth
            self.oldattack = self.attack
            self.olddefense = self.defense
            self.oldmagic = self.magic
            self.oldmaxmagic = self.maxmagic
            self.oldmagicpower = self.magicpower

            randomnum = randint(2, 5)

            self.health += randomnum
            self.maxhealth += randomnum
            self.attack += randint(2, 5)
            self.defense += randint(2, 5)
            self.magic += randomnum
            self.maxmagic += randomnum
            self.magicpower += randint(2, 5) 

            self.xp -= self.xptolevel
            self.xptolevel += 50
            print(f"{self.name} leveled up to level {self.level}")
            self.showNewStats()

    def StartGame(self):
        if self.job == "K":
            self.health = randint(15, 20)
            self.maxhealth = self.health
            self.attack = randint(6, 9)
            self.defense = randint(5, 10)
            self.magic = randint(10, 20)
            self.maxmagic = self.magic
            self.magicpower = randint(2, 5) + self.attack
            self.gold = 50

        elif self.job == "W":
            self.health = randint(10, 14)
            self.maxhealth = self.health
            self.attack = randint(2, 5)
            self.defense = randint(2, 5)
            self.magic = randint(20, 30)
            self.maxmagic = self.magic
            self.magicpower = randint(7, 11)
            self.gold = 50

        elif self.job == "A":
            self.health = randint(12, 16)
            self.maxhealth = self.health
            self.attack = randint(3, 7)
            self.defense = randint(3, 7)
            self.magic = randint(10, 20)
            self.maxmagic = self.magic
            self.magicpower = self.attack * randint(1, 3)
            self.gold = 50

        elif self.job == "T":
            self.health = randint(11, 15)
            self.maxhealth = self.health
            self.attack = randint(4, 7)
            self.defense = randint(4, 7)
            self.magic = randint(10, 20)
            self.maxmagic = self.magic
            self.magicpower = self.attack
            self.gold = 100

        elif self.job == "H":
            self.health = 9999
            self.maxhealth = self.health
            self.attack = 999
            self.defense = 999
            self.magic = 9999
            self.maxmagic = self.magic
            self.magicpower = 999
            self.gold = 9999

    def showStats(self):
        inventoryList = []
        for x in range(len(self.inventory)):
            inventoryList.append(self.inventory[x].name)
        print(f"-----Player Stats-----\nName: {self.name}\nClass: {self.job}\nLevel: {self.level}\nHealth: {self.health}/{self.maxhealth}\nMagic: {self.magic}/{self.maxmagic}\nAttack: {self.attack}\nMagic Power: {self.magicpower}\nDefense: {self.defense}\nGold: {self.gold}\nXP: {self.xp}/{self.xptolevel}\nInventory: {inventoryList}\n-----Player Stats-----")

    def die(self):
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYour quest ends here {self.name}, slayed by an enemy. GAME OVER")
        quit()

    def showHealth(self):
        return f"Health: {self.health}/{self.maxhealth}"
    
    def showNewStats(self):
        print("-----Level Up-----")
        print(f"Health: {self.oldhealth}/{self.oldmaxhealth} --> {self.health}/{self.maxhealth}\nMagic: {self.oldmagic}/{self.oldmaxmagic} --> {self.magic}/{self.maxmagic}\nAttack: {self.oldattack} --> {self.attack}\n Magic Power: {self.oldmagicpower} --> {self.magicpower}\nDefense: {self.olddefense} --> {self.defense}")