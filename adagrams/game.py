from random import randint

import random

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2,
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():

  all_letter_occurencies = ""

  hand_of_letters = []

  for letter, frequency in LETTER_POOL.items():
    all_letter_occurencies += letter *frequency

  all_letter_occurencies = list(all_letter_occurencies)  

  while len(hand_of_letters) < 10:
    random_index = random.randint(0, len(all_letter_occurencies)-1)
    random_letter = all_letter_occurencies[random_index]
    hand_of_letters.append(random_letter)
    all_letter_occurencies.pop(random_index)

  return hand_of_letters   



def uses_available_letters(word, letter_bank):
  word = word.upper()
  letter_bank = [letter.upper() for letter in letter_bank]

  word_dict ={}
  letter_bank_dict={}

  for letter in word:
    word_dict[letter] = word_dict.get(letter, 0)+1
  print(word_dict)

  for letter in letter_bank:
    letter_bank_dict[letter] = letter_bank_dict.get(letter, 0)+1
  print(letter_bank_dict)

  for letter, count in word_dict.items():
    if (letter not in letter_bank_dict 
        or count > letter_bank_dict[letter]):
      return False
  return True

score_chart = {
    ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"): 1,
    ("D", "G"): 2,
    ("B", "C", "M", "P"): 3,
    ("F", "H", "V", "W", "Y"): 4,
    ("K",): 5,
    ("J", "X"): 8,
    ("Q", "Z"): 10
}
def score_word(word):
  word = word.upper()
  if word == "":
    return 0

  score = 0
  for letter in word:
      for tuple_of_letters, score_of_letter in score_chart.items():
        if letter in tuple_of_letters:
         score += score_of_letter
  
  if 7 <= len(word) <=10:
    score += 8  
  return score  

def get_highest_word_score(word_list):
  word_list = [word.upper() for word in word_list]
  if not word_list:
    return None

  # Build list of (word, score) tuples
  list_of_tuples = []
  for word in word_list:
    score = score_word(word)
    list_of_tuples.append((word, score))

  # Find max score
  max_score = 0
  for tpl in list_of_tuples:
    if tpl[1] > max_score:
      max_score = tpl[1]

  # Collect all tuples with max score
  list_of_tuples_tie = []
  for tpl in list_of_tuples:
    if tpl[1] == max_score:
      list_of_tuples_tie.append(tpl)

  # Tie-breaker: prefer 10-letter words, else shortest word
  length_shortest_word = 11
  tuple_with_shortest_word = None
  for tpl in list_of_tuples_tie:
    if len(tpl[0]) == 10:
      return tpl
    elif len(tpl[0]) < length_shortest_word:
      length_shortest_word = len(tpl[0])
      tuple_with_shortest_word = tpl

  return tuple_with_shortest_word