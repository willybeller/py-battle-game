from characters.character import Character
import random

class Spell:
    def __init__(self, name, damage, mana_cost):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

class Wizard(Character):
    def __init__(self, name, hp, weapon, armor, spells, mana):
        super().__init__(name, hp, weapon, armor)
        self.spells = spells
        self.mana = mana

    def attack(self, target,isPlayer=False):
        # Implement attack logic for Wizard
        if isPlayer:
            print("Choisissez votre arme :")
            print("1 - "+self.weapon.name)
            for i in range(len(self.spells)):
                print(str(i+2)+" - "+self.spells[i].name)
            weapon = int(input())
        else:
            weapon = random.randint(0,len(self.spells))
        if (weapon > 1):
            if (self.spells[weapon-2].mana_cost <= self.mana):
                damages = (self.spells[weapon-2].damage - target.armor.defense)
                self.mana -= self.spells[weapon-2].mana_cost
                target.hp -= damages
                print (target.name + " subit " + str(damages) + " dégâts magiques! il lui reste "+ str(target.hp) + " HP")
            else:
                print(self.name + " is out of mana.. basic attack")
                damages = (2 - target.armor.defense)
                if (damages < 0):
                    damages = 0
                target.hp -= damages
                print (target.name + " subit " + str(damages) + " dégâts! il lui reste "+ str(target.hp) + " HP")
        else:
            damages = (self.weapon.damage - target.armor.defense)
            if (damages < 0):
                damages = 0
            target.hp -= damages
            print (target.name + " subit " + str(damages) + " dégâts ! il lui reste "+ str(target.hp) + " HP")
       # pass
