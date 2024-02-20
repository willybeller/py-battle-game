class Character:
    def __init__(self, name, hp, weapon, armor, isPlayer1):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.armor = armor
        self.isPlayer1 = isPlayer1

    def attack(self, target):
        # Implement attack logic here
        damages = (self.weapon.damage - target.armor.defense)
        if (damages < 0):
            damages = 0

        target.hp -= damages

        return (self.name + " inflige " + str(damages) + " dégâts ! il reste "+ str(target.hp) + " HP à " + target.name)

    def decal_player2():
        maxLen = "willy subit 10 dégâts magiques! il lui reste 100 HP      "
        spaces = ""
        for char in maxLen:
            spaces+=" "
        return spaces
