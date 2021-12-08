import random

class Dice:
    def __init__(self, faces):
        self.itsNumFaces = faces
        
    def roll(self):
        return random.randrange(1, self.itsNumFaces, 1)

class DiceRoller:
    # all valid poly dice
    _d4   = Dice(4)
    _d6   = Dice(6)
    _d8   = Dice(8)
    _d10  = Dice(10)
    _d12  = Dice(12)
    _d20  = Dice(20)
    _d100 = Dice(100)
    
    def roll(self, whatKind):
        if whatKind == 4:
            return self._d4.roll()
        elif whatKind == 6:
            return self._d6.roll()
        elif whatKind == 8:
            return self._d8.roll()
        elif whatKind == 10:
            return self._d10.roll()
        elif whatKind == 12:
            return self._d12.roll()
        elif whatKind == 20:
            return self._d20.roll()
        elif whatKind == 100:
            return self._d100.roll()
        else:
            print("Invalid dice type...")
            return 0
    
