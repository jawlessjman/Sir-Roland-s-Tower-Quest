from Classes import *
from GameLogic import *
from Enemy import *
import threading as th
from time import *

'''
Programmar: Jared Johnston
Project Name: Sir Rolands Tower Quest - Text Based RPG Remastered
Date: Saturday May 13, 2023.
'''

player = Player("Test", "K")
battle = None
puzzle = None
trap = None

classes = ["K", "W", "A", "T", "H"]

def checkIfDead():
    global player, timer
    if player.health <= 0:
        player.die()

timer = th.Timer(1.0, checkIfDead)

#def TestFight(player):
#    enemies = [Goblin(), Goblin()]
#    battle = Battle(enemies, player)
#    battle.fight()

def chooseDoor():
    door = None
    isdoorselected = False
    while isdoorselected == False:
        print("\nWhich door do you choose (L)eft or (R)ight?")
        selectedDoor = input("Enter which door you want to enter: ")

        if selectedDoor.upper() == "L":
            door = "L"
            isdoorselected = True
        elif selectedDoor.upper() == "R":
            door = "R"
            isdoorselected = True
        else:
            print("Error - Please enter either (L) or (R)")
    return door

def floorOne(player):
    global battle, puzzle
    #goblin fight and math puzzle
    print("\nYou approach the tower of legends. this tower is said to contain unimaginary amounts of gold and jewels\n\nThe tower is said to have been here for centuries with no one able to get to the top.\n\nYou enter the tower. There are skeletons all around of the people who didn't make it\n\nTo reach the next floor you must enter one of two doors in front of you")
    selectedDoor = chooseDoor()
    if selectedDoor == "L":
        puzzle = Puzzle("What is the answer to this math problem? 2(2 * 2) + 2", 10, player)
        puzzle.solve()
    elif selectedDoor == "R":
        enemies = [Goblin(), Goblin()]
        battle = Battle(enemies, player)
        battle.fight()
    print("\nThe Door at the end of the room opens leading to the next floor. You proceed up the stairs.\n")
    floorTwo(player)

def floorTwo(player):
    global battle
    #troll boss fight
    print("\nAs you reach the next level, there is a large door with a red skull\nYou open the door and the room is empty, you begin to walk foraward\nthe doors slam shut behind you and a large troll falls from the sky to the middle of the room.")
    enemies = [Troll()]
    battle = Battle(enemies, player)
    battle.fight()
    print("You defeat the floor two boss, The door at the end of the room opens.\nYou head up the stairs")
    floorThree(player)

def floorThree(player):
    global battle, trap
    #skeleton fight and trap room
    print("\nYou enter the third floor and are greeted by two doors.")
    selectedDoor = chooseDoor()
    if selectedDoor == "L":
        enemies = [Skeleton(), Skeleton()]
        battle = Battle(enemies, player)
        battle.fight()
    elif selectedDoor == "R":
        trap = Trap(player)
        trap.trap()
    print("The door at the end of the room opens, you proceed up the stairs")
    floorFour(player)

def floorFour(player):
    global battle
    #spider queen boss fight
    print("\nAs you reach the next level, there is a large door with a red skull\nYou open the door and the room is filled with cobwebs and spiders, as you walk into the room\nthe doors slam shut behind you and the spider queen comes down the web.")
    enemies = [Spider_Queen()]
    battle = Battle(enemies, player)
    battle.fight()
    print("You defeat the floor Four boss, The door at the end of the room opens.\nYou head up the stairs")
    floorFive(player)

def floorFive(player):
    town = Town(player)
    isInTown = True
    while isInTown == True:
        print("\nYou have entered a town, your options are (S)hop, (I)nn, (P)layer Stats, (E)xit")
        response = input("Enter your action: ")
        if response.upper() == "S":
            town.Shop()
        elif response.upper() == "I":
            town.Inn()
        elif response.upper() == "P":
            player.showStats()
        elif response.upper() == "E":
            town.ExitTown()
            floorSix(player)

def floorSix(player):
    global battle, puzzle
    #skeleton fight and puzzle
    print("\nYou reach floor six and are again greeted by two doors")
    selectedDoor = chooseDoor()
    if selectedDoor == "L":
        puzzle = Puzzle("What is 3^3 / 3", 9, player)
        puzzle.solve()
    elif selectedDoor == "R":
        enemies = [Skeleton(), Skeleton(), Skeleton()]
        battle = Battle(enemies, player)
        battle.fight()
    print("The door at the end of the room opens and you proceed to the next room")
    floorSeven(player)

def floorSeven(player):
    global battle
    #dragon boss fight
    print("\nAs you reach the next level, there is a large door with a red skull\nYou open the door and the room is all chared some parts still on fire, as you walk into the room\nthe doors slam shut behind you and a Dragon flys down from the ceiling.")
    enemies = [Dragon()]
    battle = Battle(enemies, player)
    battle.fight()
    print("You defeat the Seventh Floor boss, The door at the end of the room opens.\nYou head up the stairs")
    floorEight(player)

def floorEight(player):
    global battle, trap
    #fight with 2 trolls and trap
    print("\nYou reach floor eight, two doors are infront of you")
    selectedDoor = chooseDoor()
    if selectedDoor == "L":
        trap = Trap(player)
        trap.trap()
    elif selectedDoor == "R":
        enemies = [Troll(), Troll()]
        battle = Battle(enemies, player)
        battle.fight()
    print('The door at the end of the room opens leading to the stairs to next floor. You think to yourself, "How many more floors are there".')
    floorNine(player)

def floorNine(player):
    global battle, puzzle
    #guard fight and puzzle
    print("\nYou are now on floor nine, are you almost to the top; two doors are infront of you")
    selectedDoor = chooseDoor()
    if selectedDoor == "L":
        enemies = [Guard(), Guard(), Guard()]
        battle = Battle(enemies, player)
        battle.fight()
    elif selectedDoor == "R":
        puzzle = Puzzle("What floor was the town on?", 5, player)
    print("The door leading to the next floor opens, you proceed up the stairs to the next floor.")
    floorTen(player)

def floorTen(player):
    global battle
    #final boss fight against the king
    print('As you reach the final level, there is a large door with a gold trim and a red skull in the middle of the door\nYou open the door and the room is full of gold and a throne with someone sitting on it at the end of the room\nYou begin to walk foraward and the man gets up from his throne, he says "Have you come to Challenge me for all of my loot if you want it you must beat me in a fight"\nThe doors slam shut behind you, get ready for the final fight!!!')
    enemies = [The_King()]
    battle = Battle(enemies, player)
    battle.fight()
    print("Congratulations you beat the final boss, you take all the gold and jewels you can and head back home")
    print("\nCongrats on beating the game")
    exit()

def exit():
    print("Exitting Game")
    quit()

def Intro():
    global player, timer
    classSelected = False
    while classSelected == False:
        print("\nWelcome to Sir Rolands Tower Quest Remastered\nthis game is a text based rpg that was orginally created by me as my grade 11 final assignment\nhope you enjoy")
        print("\nClass Selection")
        print("K - Knight: a brave knight appointed by the king himself.\nW - Wizzard: a legend in the realm of magic and sorcery.\nA - Archer: nothing gets past their bow\nT - Thief: sometimes a thief other times a hero")
        playerClass = input("\nEnter the letter assosiated with class: ")
        if playerClass.upper() in classes:
            classSelected = True
        else:
            print("Error - Please enter a valid class letter\n")
    name = input("Enter a name for your character: ")

    player = Player(name, playerClass.upper())
    player.StartGame()
    player.inventory = [HealthPotion(player),HealthPotion(player), MagicPotion(player), MagicPotion(player)]
    print("\n\n")
    player.showStats()
    print("\n\n")
    #TestFight(player)
    timer.start()
    floorOne(player)

def title_screen():
    rightAnswer = False
    while rightAnswer == False:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nSir Rolands Tower Quest Remastered")
        print("Type S to start or E to exit")
        startgame = input("Enter your input now: ")
        if startgame.upper() == "S":
            rightAnswer = True
            Intro()
        elif startgame.upper() == "E":
            rightAnswer = True
            exit()
        else:
            print("Error - Please enter eithe S to Start or E to Exit\n")

title_screen()