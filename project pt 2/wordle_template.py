import random

# pick a word from the list; this can be given to the students as starter code
with open('words.txt', 'r') as w:
    wrds = [line.strip() for line in w]

        
def get_word():
    return random.choice(wrds)


