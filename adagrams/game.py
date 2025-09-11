from random import randint

def draw_letters():
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
def draw_hand():

  all_letter_occurencies = ""

  hand_of_letters = []

  for letter, frequency in LETTER_POOL.items():
    all_letter_occurencies += letter *frequency
  all_letter_occurencies = list(all_letter_occurencies)  

  while len(hand_of_letters) < 10:
    random_index = randint(0, len(all_letter_occurencies)-1)
    random_letter = all_letter_occurencies[random_index]
    hand_of_letters.append(random_letter)

  return hand_of_letters   

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass