from random import shuffle
import string

class Hanged_Man:

    def __init__(self):

        self.words = []

        with open('words.txt' , 'r') as f:
            words = f.readlines()
        
        for word in words:

            temp_word = ''

            for char in word:
                if char == '\n':
                    break
                temp_word += char
            
            self.words.append(temp_word)
        
        self.letters = list(string.ascii_lowercase)

    def pick_word(self):
        shuffle(self.words)
        self.random_word = self.words[0]
    def word_encryption(self):
        self.secret_word = ['?' for i in range(len(self.random_word))]

    def turns(self):
        self.num_turns = len(self.random_word) + (4 - self.level)
    
    def difficulty_level(self):
        self.level = int(input('Difficulty LeveL :\n* Easy : 1\n* Medium : 2\n* Hard : 3'))
    
    def update_secret_world(self):

        chosen_char = input('Guess a letter : ').lower()

        if chosen_char in self.letters:

            if chosen_char in self.random_word:
                for index , char in enumerate(self.random_word):
                    if char == chosen_char:
                        self.secret_word[index] = chosen_char
            else:
                self.num_turns -= 1

            self.letters.pop(self.letters.index(chosen_char))
            
        else:
            print('You already chose this letter!')
    
    def game_state(self):
        if self.num_turns == 0 or '?' not in self.secret_word:
            return True
        return False
    
    def display(self):
        print(f'You have {self.num_turns} turn to guess the word and save your friend')
        print(self.secret_word)
        print('_______________________________________________________________________')

