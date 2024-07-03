from itertools import combinations
import random
from random import shuffle
import plotly.express as px
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

class Tournament():

 
  
  def __init__(self, species, n_rounds, n_repl):
    self.scores = len(species)*[0]
    self.species = species
    self.prisoners = species
    self.n_rounds = n_rounds
    self.counter = 0
    self.alpha = 0.1



  
  def score(self, strategy1, strategy2, ballu):
    # ballu=1
    if (strategy1 and strategy2):
      return (20 + 5*ballu, 20 + 5*ballu)
    elif (not strategy1 and strategy2):
      return (50, -10*ballu)
    elif (strategy1 and not strategy2):
      return (-10*ballu,50)
    else:
      return (-5*ballu, -5*ballu)
  
  # def getballu(self) :
  #   return self.lallu
  




  def play_match(self, prisoner1, prisoner2, n_rounds = None):

    # Create instances of each prisoner

    p1 = prisoner1()
    p2 = prisoner2()

    self.lallu = 0
    p1.lallu = self.lallu
    p2.lallu = self.lallu
    # Initialize scores
    score1 = 0
    score2 = 0
    counter = 0
    # Play all rounds
    if not n_rounds:
      n_rounds = self.n_rounds
    for n in range(n_rounds):
      strategy1 = p1.pick_strategy()
      strategy2 = p2.pick_strategy()
      i = random.randint(0,100)
      if (i <=(10/max(1,math.sqrt(self.lallu)))):
        strategy1 = not(strategy1)
      i = random.randint(0,100)
      if (i <=(10/max(1,math.sqrt(self.lallu)))) :
        strategy2 = not(strategy2)
      if(counter != 0 and counter%4 == 0) :
        self.lallu += 1
        p1.lallu = self.lallu
        p2.lallu = self.lallu
      if (strategy1 == False or strategy2 == False) :
        self.lallu = 0
        p1.lallu = self.lallu
        p2.lallu = self.lallu
        counter = 0
      else :
        counter += 1 

      scores = self.score(strategy1, strategy2,self.lallu)
      #print((scores[0],scores[1]), "\n")
      score1 += scores[0]
      score2 += scores[1]
      p1.process_results(strategy1, strategy2)
      p2.process_results(strategy2, strategy1)

    # Return scores
    return (score1, score2)

  """
  Play a round robin
  """
  def round_robin(self,number):
    for ii in range(number):
      # Create a list of all combinations of prisoners
      matches = list(combinations(range(len(self.prisoners)), 2))
      shuffle(matches)
      # Pay all matches
      for match in matches:
        (score1, score2) = self.play_match(
          self.prisoners[match[0]],
          self.prisoners[match[1]])
        self.scores[match[0]] += score1
        self.scores[match[1]] += score2
    
    self.plot()
    # index = 0
    # for ii in self.scores:
    #   print(index, " ",ii)
    #   index += 1 
    # for ii in range(0,len(self.scores)) :
    #   self.scores[ii] = 0
    # self.alpha += 0.1

  def plot(self):


    # Replace these arrays with your actual data
    speciess = []
    scoress = []
    index = 0
    for ii in self.species :
      speciess.append(ii.__name__)
      index += 1
    for ii in self.scores :
      scoress.append(ii*1)
    # Create a DataFrame for Plotly
    data = pd.DataFrame({
        'Species': speciess,
        'Scores': scoress
    })

    # Create the bar plot
    fig = px.bar(data, x='Species', y='Scores', title='Scores by Species', 
                labels={'Species': 'Species', 'Scores': 'Scores'},
                color='Species', color_discrete_sequence=px.colors.qualitative.Pastel)

    # Customize the layout for better readability
    fig.update_layout(
        title={'x':0.5, 'xanchor': 'center'},
        xaxis_title='Species',
        yaxis_title='Scores',
        yaxis=dict(showgrid=True, gridwidth=1, gridcolor='LightGray'),
        plot_bgcolor='rgba(0,0,0,0)'
    )

    # Show the plot
    fig.show()

