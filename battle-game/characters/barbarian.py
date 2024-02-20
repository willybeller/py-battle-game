from arena import Arena
import string
from characters.character import Character
import keyboard
import time
import random

class Barbarian(Character):
    def attack(self, target):
        # Implement special attack logic for Barbarian
        if(self.isPlayer1):
            print("Premier coup de "+self.name+" :")
            Barbarian.sword_attack_animationP1()
            print(super().attack(target))
        else:
            print(Character.decal_player2()+"Premier coup de "+self.name+" :")
            Barbarian.sword_attack_animationP2()
            print(Character.decal_player2()+super().attack(target))
        if(self.isPlayer1):
            if Barbarian.qce():
                print("Second coup de "+self.name+" :")
                Barbarian.sword_attack_animationP1()
                print(super().attack(target))
            else :
                print("La seconde attaque a échouée..")
        else:
            success = random.randint(1,2) #Randomisation du succès du 2nd coup du bot, ici 1 chance sur 2
            if success>1:
                print(Character.decal_player2()+"Second coup de "+self.name+" :")
                Barbarian.sword_attack_animationP2()
                print(Character.decal_player2()+super().attack(target))
            else :
                print(Character.decal_player2()+"La seconde attaque a échouée..")

    def qce():
        touche_a_activer = random.choice(string.ascii_lowercase)  # Choix aléatoire parmi ces touches
        print(f"Appuyez sur la touche '{touche_a_activer}' !")
        time.sleep(1)#random.uniform(1, 3))  # Délai aléatoire entre 1 et 3 secondes
        start_time = time.time()

        # Attends que la touche soit pressée ou que le délai soit écoulé
        while time.time() - start_time < 1:
            if keyboard.is_pressed(touche_a_activer):
                print("Bien joué !")
                return True
        print("Temps écoulé")
        return False
    
    def sword_attack_animationP1():
        frames = [
        r"      /|  ________________",
        r" O|===|* >________________>",
        r"      \|",
        ]
        for frame in frames:
            print(frame)
            time.sleep(0.15)

    def sword_attack_animationP2():
        frames = [
        r"      /|  ________________",
        r" O|===|* >________________>",
        r"      \|",
        ]
        for frame in frames:
            print(Character.decal_player2()+frame)
            time.sleep(0.15)
