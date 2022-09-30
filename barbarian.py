from adventurer import Adventurer
from dice import Dice

class Barbarian(Adventurer):
    "Returns the maximum rages the character has based on their level"
    def get_max_rages(self):
        if (self.level >= 1) and (self.level <= 2):
            self.max_rages = 2
        elif (self.level >= 3) and (self.level <= 5):
            self.max_rages = 3
        elif (self.level >= 6) and (self.level <= 11):
            self.max_rages = 4
        elif (self.level >= 12) and (self.level <= 16):
            self.max_rages = 5
        elif (self.level >= 17) and (self.level <= 19):
            self.max_rages = 6
        elif (self.level == 20):
            self.max_rages = float('inf')
        return self.max_rages
    
    def __init__(self,name,level,ac,hp,ability_scores,attacks):
        super().__init__(name,level,ac,hp,ability_scores,attacks)
        self.rages = self.get_max_rages()
        self.raging = False

    def __str__(self):
        if self.raging:
            return 'Barbarian ' + super().__str__() + ' (Raging)'
        else:
            return 'Barbarian ' + super().__str__()

    def level_up(self):
        super().level_up()
        self.max_hp = self.hp + 7
        self.hp = self.max_hp
        self.rages = self.max_rages

    "Returns the rage damage based on the character's level"
    def get_rage_damage(self):
        if (self.level < 1) or (self.level > 20):
            raise ValueError('Invalid level.')
        else:
            if (self.level >= 1) and (self.level <= 8):
                self.rage_damage = 2
            elif (self.level >= 9) and (self.level <= 15):
                self.rage_damage = 3
            elif (self.level >= 16) and (self.level <= 20):
                self.rage_damage = 4
        return self.rage_damage

    def attack(self,weapon):
        super().attack(weapon)
        attack_die = Dice.interpret('d20')
        attack = attack_die.roll()
        for key,value in self.attacks.items():
            if '{}'.format(weapon) == key:
                damage_dice = self.attacks[key][0]
                ability = self.attacks[key][1]
                proficient = self.attacks[key][2]
        total_damage = 0
        roll = damage_dice.roll()
        if roll >= 20:
            total_damage += roll
            total_damage += damage_dice.roll()
        else:
            total_damage += roll
        if proficient:
            attack += self.get_proficiency_bonus()
        attack += self.get_modifier(ability)
        total_damage += self.get_modifier(ability)
        "Adds rage damage if the character is currently raging"
        if self.raging == True:
            total_damage += self.get_rage_damage()
        return (attack,total_damage)

        
    def enter_rage(self):
        if self.rages != 0:
            self.raging = True

    def exit_rage(self):
        self.raging = False
        self.rages -= 1
