
from dice import Dice

"Base class for each Adventurer created"
class Adventurer:
    def __init__(self,name,level,ac,hp,ability_scores,attacks):
        self.name = name
        self.level = level
        self.ac = ac
        self.hp = hp
        self.max_hp = hp
        self.ability_scores = ability_scores
        self.attacks = attacks

    def __str__(self):
        return '"{}": Level {}, AC {}, {} Hit Points'.format(self.name, self.level, self.ac, self.hp) 

    def level_up(self):
        self.level += 1
    
    "Returns the modifier for the ability (based on the ability score)"
    def get_modifier(self,ability):
        "If the character does not have the ability in their self.ability_scores dictionary, a KeyError is raised with an informative message"
        try:
            self.ability = ability
            ability_score = self.ability_scores[self.ability]
            modifier = (ability_score - 10) // 2
        except KeyError:
            print('{} does not have this {}'.format(self.name,self.ability))
        return modifier
    
    "Returns the proficiency bonus based on their level"
    def get_proficiency_bonus(self):
        if (self.level < 1) or (self.level > 20):
            raise ValueError('Invalid level.')
        else:
            if (self.level >= 1) and (self.level <= 4):
                proficiency_bonus = 2
            elif (self.level >= 5) and (self.level <= 8):
                proficiency_bonus = 3
            elif (self.level >= 9) and (self.level <= 12):
                proficiency_bonus = 4
            elif (self.level >= 13) and (self.level <= 16):
                proficiency_bonus = 5
            elif (self.level >= 17) and (self.level <= 20):
                proficiency_bonus = 6
        return proficiency_bonus
    
    "Returns a tuple of the (attack roll, total damage) when the character attacks with the input weapon"
    def attack(self,weapon):
        "Determines whether or not the attack hits the opponent"
        attack_die = Dice.interpret('d20')
        attack = attack_die.roll()
        for key,value in self.attacks.items():
            if '{}'.format(weapon) == key:
                damage_dice = self.attacks[key][0]
                ability = self.attacks[key][1]
                proficient = self.attacks[key][2]
        total_damage = 0
        "Damage roll determines how much damage is dealt to the opponent"
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
        return (attack,total_damage)
    
        
