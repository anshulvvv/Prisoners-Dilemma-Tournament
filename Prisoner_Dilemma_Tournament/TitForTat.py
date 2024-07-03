from Prisoner import Prisoner

class TitForTat(Prisoner):
    
  
    def __init__(self):
        self.last_strategy = True
    
    
    def pick_strategy(self):
        return self.last_strategy
    
    
    def process_results(self, my_strategy, other_strategy):
        self.last_strategy = other_strategy
