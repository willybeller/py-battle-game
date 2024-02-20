import random
from characters.character import Character
from gears.weapon import Weapon
from gears.armor import Armor
from characters.barbarian import Barbarian
from characters.wizard import Wizard, Spell
from arena import Arena

# Instantiate characters, weapons, armor, etc.

# Example usage of Arena class
john = Barbarian("John", 100, Weapon("Sword", 10), Armor("Plate Mail", 5), False)
jane = Wizard("Jane", 92, Weapon("Staff", 8), Armor("Robe", 2), False, [Spell("Fireball", 15, 10), Spell("Tsunami", 25, 30)], 50)

print("Bienvenue sur py-battle-game !")
name = input("Entrez votre nom : ")
#Menu et sélection de personnage
classChoosen = False
while(not classChoosen):
    print("Selectionnez votre classe :")
    print("1 - Barbare\n2 - Mage")
    choice = input()
    if(choice=="1"):
        hero = Barbarian(str(name), 100, Weapon("Sword", 10), Armor("Plate Mail", 5), True)
        classChoosen = True
    elif(choice=="2"):
        hero = Wizard(str(name), 92, Weapon("Staff", 8), Armor("Robe", 2), True, [Spell("Fireball", 15, 10), Spell("Tsunami", 25, 30)], 50)
        classChoosen = True
    else:
        print("Merci de sélectionner un numéro de la liste")

#Randomisation de l'adversaire (Wizard ou Barbarian)
rdm = random.randint(1,2)
if(rdm==1):
    ops = jane #Wizard
else:
    ops = john #Barbarian

arena = Arena(hero, ops)
arena.fight()

#Flush du keyboard buffer rempli à cause du QCE
try:
    import msvcrt
    while msvcrt.kbhit():
        msvcrt.getch()
except ImportError:
    import sys, termios
    termios.tcflush(sys.stdin, termios.TCIOFLUSH)