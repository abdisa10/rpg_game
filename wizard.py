from adventurer import Adventurer
from dice import Dice

class Wizard(Adventurer):
    def __init__(self,name,level,ac,hp,ability_scores,attacks,cantrips):
        super().__init__(name,level,ac,hp,ability_scores,attacks)
        self.cantrips = cantrips

    def __str__(self):
        return 'Wizard ' + super().__str__()

    def level_up(self):
        super().level_up()
        self.max_hp = self.hp + 4
        self.hp = self.max_hp

    "Rolls the damage dice from the cantrip and returns their result"
    def cast_cantrip(self,cantrip):
        "If the character does not have the cantrip in their self.cantrips dictionary, a KeyError is raised with an informative message"
        try:
            self.cantrip = cantrip
            cantrip_dice = self.cantrips[self.cantrip]
            damage = cantrip_dice.roll()
        except KeyError:
            print('{} does not have cantrip {}'.format(self.name,self.cantrip))
        return damage
