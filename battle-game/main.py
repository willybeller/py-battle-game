from characters.character import Character
from gears.weapon import Weapon
from gears.armor import Armor
from characters.barbarian import Barbarian
from characters.wizard import Wizard, Spell
from arena import Arena

# Instantiate characters, weapons, armor, etc.

# Example usage of Arena class
john = Barbarian("John", 100, Weapon("Sword", 10), Armor("Plate Mail", 5))
jane = Wizard("Jane", 92, Weapon("Staff", 8), Armor("Robe", 2), [Spell("Fireball", 15, 10)], 50)

print("Bienvenue sur py-battle-game !")
name = input("Entrez votre nom : ")
#Menu et sélection de personnage
classChoosen = False
while(not classChoosen):
    print("Selectionnez votre classe :")
    print("1 - Barbare\n2 - Mage")
    choice = input()
    if(choice=="1"):
        hero = Barbarian(str(name), 100, Weapon("Sword", 10), Armor("Plate Mail", 5))
        classChoosen = True
    elif(choice=="2"):
        hero = Wizard(str(name), 92, Weapon("Staff", 8), Armor("Robe", 2), [Spell("Fireball", 15, 10)], 50)
        classChoosen = True
    else:
        print("Merci de sélectionner un numéro de la liste")



arena = Arena(hero, jane)
arena.fight()
