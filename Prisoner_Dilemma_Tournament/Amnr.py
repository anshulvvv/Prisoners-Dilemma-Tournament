from Prisoner import Prisoner
from Tournament import Tournament
import random


class Amnesiacr(Prisoner):
    
    def __init__(self):
        self.hist = []
        self.strat = True
    
    def pick_strategy(self):
        return self.strat
    
    def process_results(self, my_strategy, other_strategy):
        if other_strategy:
            self.hist.append(1)
        else:
            self.hist.append(-1)
        i = random.randint(6,25)
        while(len(self.hist) >= i):
            self.hist.pop(0)
        total = sum(self.hist)
        if total>=0:
            self.strat = True
        else:
            self.strat = False