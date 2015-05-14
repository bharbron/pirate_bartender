import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def ask_what_style():
  """Asks questions about what style drink the pirate likes"""
  preferences = {}
  for key in questions:
    answer = raw_input(questions[key] + ' ')
    if (answer.lower() == 'yes') or (answer.lower() == 'y'):
      preferences[key] = True
    else:
      preferences[key] = False
  return preferences

def construct_a_drink(preferences):
  """Constructs a drink based on the given preferences"""
  drink = []
  for style in preferences:
    if preferences[style] is True:
      drink.append(random.choice(ingredients[style]))
  return drink

def print_drink(drink):
  """Print the given drink, pirate style"""
  if drink == []:
    print "Yar! Don't ye like pirate drinks, landlubber?"
  else:
    print "I'll make ye a drink with a " + ", ".join(drink) + ", ye scurvy dog!"
    

if __name__ == '__main__':
  preferences = ask_what_style()
  drink = construct_a_drink(preferences)
  print_drink(drink)
  