import random

class Dice:
    def __init__(self,how_many,sides,modifier=0):
        self.how_many = how_many
        self.sides = sides
        self.modifier = modifier        "The value added to the roll labeled as modifier"

    def __str__(self):
        return str(self.how_many) + 'd' + str(self.sides) + '+' + str(self.modifier)
    
    def roll(self):
        value = 0
        for roll in range(self.how_many):
            value += random.randint(1,self.sides)
        value += self.modifier
        return value

    @staticmethod
    "Interprets and returns a string notation in a more cleaned up dice notation"
    def interpret(notation):        
        "Parses through the string to find how many dice there's being rolled"
        for element in range(len(notation)):
            if notation[element] == 'd':
                if notation[0:element] == '':
                    how_many = 1
                else:
                    how_many = int(notation[0:element])
                notation = notation[element + 1:]
                break
        "Parses through the next part of string notation to find how many sides the dice have"
        "Also looks to see what the modifier is"
        if '+' in notation:
            for element in range(len(notation)):
                if notation[element] == '+':
                    sides = notation[0:element]
                    modifier = notation[element+1:]
                    break
        else:
            sides = notation
            modifier = 0
        return Dice(int(how_many),int(sides),int(modifier))
