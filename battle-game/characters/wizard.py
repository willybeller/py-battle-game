import time
from characters.character import Character
import random

class Spell:
    def __init__(self, name, damage, mana_cost):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

class Wizard(Character):
    def __init__(self, name, hp, weapon, armor, isPlayer1, spells, mana):
        super().__init__(name, hp, weapon, armor, isPlayer1)
        self.spells = spells
        self.mana = mana

    def attack(self, target,isPlayer=False):
        # Implement attack logic for Wizard
        if isPlayer:
            weaponChoosen = False
            while (not weaponChoosen):
                print("Choisissez votre arme : (Il vous reste "+str(self.mana)+" points de mana)")
                print("1 - "+self.weapon.name)
                for i in range(len(self.spells)):
                    print(str(i+2)+" - "+self.spells[i].name+" ("+str(self.spells[i].mana_cost)+")")
                try:
                    weapon = int(input())
                except ValueError:
                    print("Merci de sélectionner un chiffre entre 1 et "+str(len(self.spells)+1))
                    continue
                if (weapon>0 and weapon<=(len(self.spells)+1)):
                    weaponChoosen = True
                    break
                else:
                    print("Merci de sélectionner un chiffre entre 1 et "+str(len(self.spells)+1))
        else:
            weapon = random.randint(1,len(self.spells)+1)
        if (weapon > 1):
            if (self.spells[weapon-2].mana_cost <= self.mana):
                damages = (self.spells[weapon-2].damage)# - target.armor.defense) #les spell ignore l'armure
                self.mana -= self.spells[weapon-2].mana_cost
                target.hp -= damages
                if (self.isPlayer1):
                    if(self.spells[weapon-2].name == 'Tsunami'):
                        Wizard.spell_water_animationP1()
                    elif(self.spells[weapon-2].name == 'Fireball'):
                        Wizard.spell_fire_animationP1()
                    print (self.name + " inflige " + str(damages) + " dégâts magiques! il reste "+ str(target.hp) + " HP à " + target.name)
                else :
                    if(self.spells[weapon-2].name == 'Tsunami'):
                        Wizard.spell_water_animationP2()
                    elif(self.spells[weapon-2].name == 'Fireball'):
                        Wizard.spell_fire_animationP2()
                    print (Character.decal_player2()+self.name + " inflige " + str(damages) + " dégâts magiques! il reste "+ str(target.hp) + " HP à " + target.name)

            else:
                if(self.isPlayer1):
                    print(self.name + " n'a plus de mana.. attaque basique")
                else:
                    print(Character.decal_player2()+self.name + " n'a plus de mana.. attaque basique")
                damages = (2 - target.armor.defense)
                if (damages < 0):
                    damages = 0
                target.hp -= damages
                if(self.isPlayer1):
                    Wizard.dagger_attack_animationP1()
                    print (self.name + " inflige " + str(damages) + " dégâts! il reste "+ str(target.hp) + " HP à " + target.name)
                else:
                    Wizard.dagger_attack_animationP2()
                    print (Character.decal_player2()+self.name + " inflige " + str(damages) + " dégâts! il reste "+ str(target.hp) + " HP à " + target.name)
        else:
            damages = (self.weapon.damage - target.armor.defense)
            if (damages < 0):
                damages = 0
            target.hp -= damages
            if(self.isPlayer1):
                Wizard.dagger_attack_animationP1()
                print (self.name + " inflige " + str(damages) + " dégâts ! il reste "+ str(target.hp) + " HP à " + target.name)
            else:
                Wizard.dagger_attack_animationP2()
                print (Character.decal_player2()+self.name + " inflige " + str(damages) + " dégâts ! il reste "+ str(target.hp) + " HP à " + target.name)
    
    def spell_fire_animationP1():
        frames = [
            "⠀⠀⠀⠀⠀⠀⢱⣆⠀⠀⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠈⣿⣷⡀⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⢸⣿⣿⣷⣧⠀⠀⠀",
            "⠀⠀⠀⡀⢠⣿⡟⣿⣿⣿⡇⠀⠀",
            "⠀⠀⠀⣳⣼⣿⡏⢸⣿⣿⣿⢀⠀",
            "⠀⠀⣰⣿⣿⡿⠁⢸⣿⣿⡟⣼⡆",
            "⢰⢀⣾⣿⣿⠟⡀⠀⣾⢿⣿⣿⣿",
            "⢸⣿⣿⣿⡏⠀⠀⠀⠃⠸⣿⣿⣿⡿",
            "⢳⣿⣿⣿⠀⠀⠀⠀⠀⠀⢹⣿⡿⡁",
            "⠀⠹⣿⣿⡄⠀⠀⠀⠀⠀⢠⣿⡞⠁",
            "⠀⠀⠈⠛⢿⣄⠀⠀⠀⣠⠞⠋⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀"
        ]
        for frame in frames:
            print(frame)
            time.sleep(0.05)

    def dagger_attack_animationP1():
        frames = [
            "                  |",
            "--==/////////////[}}====*",
            "                  |"
        ]

        for frame in frames:
            print(frame)
            time.sleep(0.2)

    def spell_fire_animationP2():
        frames = [
            "⠀⠀⠀⠀⠀⠀⢱⣆⠀⠀⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠈⣿⣷⡀⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⢸⣿⣿⣷⣧⠀⠀⠀",
            "⠀⠀⠀⡀⢠⣿⡟⣿⣿⣿⡇⠀⠀",
            "⠀⠀⠀⣳⣼⣿⡏⢸⣿⣿⣿⢀⠀",
            "⠀⠀⣰⣿⣿⡿⠁⢸⣿⣿⡟⣼⡆",
            "⢰⢀⣾⣿⣿⠟⡀⠀⣾⢿⣿⣿⣿",
            "⢸⣿⣿⣿⡏⠀⠀⠀⠃⠸⣿⣿⣿⡿",
            "⢳⣿⣿⣿⠀⠀⠀⠀⠀⠀⢹⣿⡿⡁",
            "⠀⠹⣿⣿⡄⠀⠀⠀⠀⠀⢠⣿⡞⠁",
            "⠀⠀⠈⠛⢿⣄⠀⠀⠀⣠⠞⠋⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀"
        ]
        for frame in frames:
            print(Character.decal_player2()+frame)
            time.sleep(0.05)

    def dagger_attack_animationP2():
        frames = [
            "                  |",
            "--==/////////////[}}====*",
            "                  |"
        ]

        for frame in frames:
            print(Character.decal_player2()+frame)
            time.sleep(0.2)

    def spell_water_animationP1():
        frames = [
            "                                                                                                                                 ",
            "                   :++=----+=.     ",
            "                .++-         .+:   ",
            "               =+.             ==  ",
            "             :+:             --=+- ",
            "           .+=             ++   :+ ",
            "          ==.             -=       ",
            "       .++                -=       ",
            "     .-+:                  .+.      ",
            ":--:                       :+=     ",
            "                              -+=+=",
        ]

        for frame in frames:
            print(frame)
            time.sleep(0.05)

    def spell_water_animationP2():
        frames = [
            "         .-+++==+=-.                   ",
            "       =+.         .=+-                ",
            "      =:               ==              ",
            "     =+=--.              =.            ",
            "         +-              --            ",
            "           +                =          ",
            "          :=                  +.       ",
            "         =+                     -=:    ",
            "=+++++++=.                         .-=+",
            "                                       "
        ]

        for frame in frames:
            print(Character.decal_player2()+frame)
            time.sleep(0.05)