from adventurer import Adventurer

class Monk(Adventurer):
    
    def __str__(self):
        return 'Monk ' + super().__str__()

    def level_up(self):
        super().level_up()
        self.max_hp = self.hp + 5
        self.hp = self.max_hp
    
    "Returns the maximum number of Ki (magic energy) points that the character can have"
    def get_ki_points(self):
        if self.level == 1:
            ki_points = 0
        elif self.level >= 2:
            ki_points = self.level
        return ki_points
    
