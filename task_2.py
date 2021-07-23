import random
from cprint import *

lives = 10

words_list = ('love', 'death', 'python', 'robot', 'fantasy', 'blizzard', 
              'storm', 'paradise', 'hell', 'heart', 'space', 'loyalty')

selected_word = random.choice(words_list)

active_word = len(selected_word) * '_'

while (lives > 0) and ('_' in active_word):
    print('Current progress:', active_word, '\nLives left:', lives, '\n!BloodTrail')
    letter = input('Input a letter:')

    if letter in selected_word:
        cprint.info('There is the letter in the word !SeemsGood')
        index = -1

        while active_word.count(letter) != selected_word.count(letter):
            index = selected_word.find(letter, index + 1)
            active_word = active_word[:index] + letter + active_word[index + 1:]

    else:
        cprint.warn('There is no the letter in the word !SMOrc')
        lives -= 1
    
    cprint.ok('=' * 42)

if lives > 0:
    cprint.info('Congratulations, you won! !PogChamp')

else:
    cprint.warn('Unfortunately, you lost. !BibleThump\nBetter luck next time')
    cprint.warn('The word was:', selected_word)