from Prisoner import Prisoner


class Umesh(Prisoner):
    
    
    def __init__(self):
        self.last_strategy = True
        self.count = 0
    
    
    def pick_strategy(self):
        return self.last_strategy
    
    
    def process_results(self, my_strategy, other_strategy):
        if(other_strategy == False):
            self.count +=1
        else :
            self.count = 0
        if(self.count >= 2):
            self.last_strategy = other_strategy
        else : 
            self.last_strategy = True
