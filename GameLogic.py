from Classes import *
from Enemy import *

isenchanted = False

class Puzzle:
    def __init__(self, puzzle, puzzleAnswer, player):
        self.traps = ["A bunch of arrows come flying out of the wall damaging you", "The floor beneath you disapears, you fall a down but are still alive, there is a ladder up", "Poison gas starts filling the room, you lose some health but are still alive"]
        self.roomType = "Puzzle"
        self.puzzle = puzzle
        self.type = type(puzzleAnswer)
        self.answer = puzzleAnswer
        self.attempts = 3
        self.player = player

    def solve(self):
        print("-----Puzzle Start-----")
        issolved = False
        while issolved == False:
            print(f"In the room there are writtings on the wall, it says: {self.puzzle} and that you only have {self.attempts} tries to get the answer correct")
            guess = input("\nEnter what you think the answer is: ")
            try:
                guess = self.type(guess)
            except:
                pass
            if self.attempts <= 1:
                issolved = True
                response = randint(0, 2)
                print(f"No, you ran out of attempts, {self.traps[response]}")
                print(f"You are now at {self.player.showHealth()}")
                print("You may have taken damage but the door still opens to the next floor.")
            elif guess == self.answer:
                issolved = True
                print("Yes, you got the right answer.")
            else:
                print("That wasn't right try again.")
                self.attempts -= 1
        print("-----Puzzle Finish-----")

class Trap:
    def __init__(self, player):
        self.roomType = "Trap"
        self.player = player

    def trap(self):
        damage = 6
        print("-----Trap Room Start-----")
        print("You enter the room, the room is empty, The door to the next floor is also open")
        isChoosing = False
        while isChoosing == False:
            print("What do you want to do (R)un for the door, (C)arefully walk to the door, (I)nvestigate the Room,or (S)tats")
            action = input("Enter the action you want to do: ")
            if action.upper() == "R":
                self.player.health -= damage
                print(f"You run through the room, you realize the room was trapped and you have activated every trap, you take 6 damage, Health: {self.player.health}/{self.player.maxhealth}")
                isChoosing = True
            elif action.upper() == "C":
                self.player.health -= (damage / 2)
                print(f"You carefully walk through the room, you accidently step on something triggering a trap, you take 3 damage, Health: {self.player.health}/{self.player.maxhealth}")
                isChoosing = True
            elif action.upper() == "I":
                print("You Investigate the room and find out the room was trapped, you disarm it.")
                isChoosing = True
            elif action.upper() == "S":
                self.player.showStats()
            else:
                print("Error - Please enter a valid Action")
        print("-----Trap Room Finish-----")

class Battle:
    def __init__(self, enemies, player):
        self.eneimes = enemies
        self.player = player

    def fight(self):
        #list for the actions
        print('\n\n\n\n\n-----Battle Start-----')
        print(f"{len(self.eneimes)} eneimes appear")
        while len(self.eneimes) > 0:
            enemyselected = False
            #while loop for selecting an enemy
            while enemyselected == False:
                if len(self.eneimes) <= 0:
                    enemyselected = True
                    actionselected = True
                    return

                print("\nType the number next to the enemey to select which one you want to fight then choose an action")
                for x in range(len(self.eneimes)):
                    print(f"{x + 1} - {self.eneimes[x].name}")
                selectedenemy = input("\nEnter the number of which enemy you want to target: ")
                selectedenemy = self.isNum(selectedenemy)
                if type(selectedenemy) == int:
                    if selectedenemy - 1 > x:
                        print("\nError - there is no enemy with that number\n")

                    elif selectedenemy == -1 or selectedenemy < 0:
                        print("\nError - please enter a number that is associated with an enemy\n")

                    elif selectedenemy - 1 <= x and selectedenemy - 1 >= 0:
                        enemyselected = True

                    else:
                        print("\nError - please enter a valid number\n")
            actionselected = False

            #while loop for the player selecting an action
            while actionselected == False:
                if len(self.eneimes) < 0:
                    return

                print(f"\nBattle Actions - (A)ttack, (M)agic Attack, (I)nventory, (R)eturn, or (S)tats")
                action = input("\nEnter the letter of the action you want to do: ")

                selectedenemy = selectedenemy - 1

                if action.upper() == "A":
                    actionselected = True
                    damage = self.player.attack - self.eneimes[selectedenemy].defense
                    if damage <= 0:
                        damage = 1
                    self.eneimes[selectedenemy].health -= damage
                    print(f"{self.player.name} hits a {self.eneimes[selectedenemy].name} for {damage} damage, the {self.eneimes[selectedenemy].name} has {self.eneimes[selectedenemy].health}/{self.eneimes[selectedenemy].maxhealth} health left")
                    self.checkEnemy()

                elif action.upper() == "M":
                    if self.player.magic < 3:
                        print("You do not have enough magic to use a magic attack")
                        actionselected = True
                    elif self.player.magic >= 3:
                        actionselected = True
                        damage = self.player.magicpower - self.eneimes[selectedenemy].defense
                        if damage <= 0:
                            damage = 1
                        self.eneimes[selectedenemy].health -= damage
                        print(f"{self.player.name} blasts a {self.eneimes[selectedenemy].name} for {damage} damage, the {self.eneimes[selectedenemy].name} has {self.eneimes[selectedenemy].health}/{self.eneimes[selectedenemy].maxhealth} health left")
                        self.player.magic -= 3
                        self.checkEnemy()

                elif action.upper() == "I":
                    actionselected = True
                    itemselected = False
                    while itemselected == False:
                        print("-----Inventory-----")
                        for items in range(len(self.player.inventory)):
                            print(f"{items + 1} - {self.player.inventory[items].name}")
                        print("-----Inventory-----")
                        item = input("\nEnter the number of the item you want to use: ")
                        item = self.isNum(item)
                        if item - 1 < 0 or item <= -1:
                            print("\nError - please enter a valid item number\n")
                        elif item - 1 >= 0:
                            itemselected = True
                    self.player.inventory[item - 1].usePotion()
                    self.checkEnemy()

                elif action.upper() == "R":
                    actionselected = True

                elif action.upper() == "S":
                    self.player.showStats()
                    actionselected = True

                else:
                    print("\nError - Please enter a valid action\n")

                enemyselected = False
        print("-----Battle Finish-----\n")
                

    def isNum(self, num):
        try:
            num = int(num)
        except:
            return -1
        if type(num) == int:
            return int(num)

    def checkEnemy(self):
        try:
            for x in range(len(self.eneimes)):
                if self.eneimes[x].health <= 0:
                    self.player.xp += self.eneimes[x].xp
                    self.player.levelUp()
                    print(f"\nyou killed a {self.eneimes[x].name}")
                    self.eneimes.pop(x)
        except:
            pass
        self.attackPlayer()

    def attackPlayer(self):
        for x in range(len(self.eneimes)):
            damage = self.eneimes[x].attack - self.player.defense
            if damage <= 0:
                damage = 1
            self.player.health -= damage
            print(f"\na {self.eneimes[x].name} attacks you for {damage} damage, your health: {self.player.health}/{self.player.maxhealth}")
        if self.player.health <= 0:
            self.player.die()

class Town:
    def __init__(self, player):
        self.player = player

    def Shop(self):
        isbuying = False
        while isbuying == False:
            print("-----Shop-----")
            print("1 - Enchant Weapon $100")
            print("2 - Health Potion $50")
            print("3 - Magic Potion $50")
            print("4 - Leave the Shop")

            print(f"You have ${self.player.gold}")

            #print("Enter the number next to item you want to purchase")
            bought = input("Enter the number associated with the item you want to buy: ")
            if bought == "1" and isenchanted == False and self.player.gold >= 100:
                isbuying = True
                self.player.attack = self.player.attack * 1.5
                self.player.magicpower = self.player.magicpower * 2
                print("You enchant your weapon, your attack and magic power has increased!")
                isenchanted == True
                self.player.gold -= 100
                print("-----Shop-----")
            elif bought == "2" and self.player.gold >= 50:
                isbuying = True
                self.player.gold -= 50
                self.player.inventory.append(HealthPotion(self.player))
                print("You purchase a Health Potion - Health Potion added to your inventory")
                print("-----Shop-----")
            elif bought == "3" and self.player.gold >= 50:
                isbuying = True
                self.player.gold -= 50
                self.player.inventory.append(MagicPotion(self.player))
                print("You purchase a Health Potion - Magic Potion added to your inventory")
                print("-----Shop-----")
            elif bought == "4":
                isbuying = True
                print("You leave the shop and head back into the town")
                return
            else:
                print("Error - Please enter a valid number")  

    def Inn(self):
        isstaying = False
        while isstaying == False:
            print("-----Inn-----")
            print("Welcome to the Tower's Inn")
            print("It costs $20 to sleep at the Inn. Sleeping at the Inn fill fully restore your Health and Magic")
            print("Do you want to stay at the Inn? (Y)es or (N)o")
            response = input("Enter your response here: ")
            if response.upper() == "Y":
                isstaying = True
                print("You sleep at the Inn, and wake up fully restored")
                print("-----Inn-----")
                self.player.health = self.player.maxhealth
                self.player.magic = self.player.maxmagic
            elif response.upper() == "N":
                isstaying = True
                print("You decide not to sleep at the Inn and go back to the town")
                print("-----Inn-----")
                return
            else:
                print("Error - Please enter either (Y)es or (N)o")

    def ExitTown(self):
        print("You leave the town and proceed to the next floor")