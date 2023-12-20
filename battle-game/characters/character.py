class Character:
    def __init__(self, name, hp, weapon, armor):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.armor = armor

    def attack(self, target):
        # Implement attack logic here
        damages = (self.weapon.damage - target.armor.defense)
        if (damages < 0):
            damages = 0

        target.hp -= damages

        print (target.name + " subit " + str(damages) + " dégâts ! il lui reste "+ str(target.hp) + " HP")
