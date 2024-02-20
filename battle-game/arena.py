import time
import os
class Arena:
    def __init__(self, first_character, second_character):
        self.first_character = first_character
        self.second_character = second_character

    def fight(self):
        # Implement combat logic here
        while(self.first_character.hp>0 and self.second_character.hp>0):
            if (str(type(self.first_character)) == "<class 'characters.wizard.Wizard'>"):
                if (self.first_character.mana>0):
                    
                    self.first_character.attack(self.second_character,True)
                else:
                    self.first_character.attack(self.second_character,True)
            else:
                self.first_character.attack(self.second_character)
            
            if (str(type(self.second_character)) == "<class 'characters.wizard.Wizard'>"):
                if (self.second_character.mana>0):
                    self.second_character.attack(self.first_character)
                else:
                    self.second_character.attack(self.first_character)
            else:
                self.second_character.attack(self.first_character)
                #print(type(self.second_character))
            
        if(self.first_character.hp<0):
            print("GAME OVER, le vainqueur est "+self.second_character.name) 
        else:
            print("Victoire "+self.first_character.name+", vous avez vaincu "+self.second_character.name) 

    
    
