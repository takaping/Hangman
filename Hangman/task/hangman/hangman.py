# Write your code here
import random


word_list = ['python', 'java', 'kotlin', 'javascript']

print('H A N G M A N')
while input('Type "play" to play the game, "exit" to quit: ') == 'play':
    correct_word = random.choice(word_list)
    input_letters = set()
    mistakes = 0

    while mistakes < 8:
        answer_word = ''.join([c if c in input_letters else '-'
                               for c in correct_word])
        print('\n' + answer_word)
        if '-' not in answer_word:
            print('You guessed the word!\nYou survived!')
            break

        letter = input('Input a letter: ')

        if len(letter) != 1:
            print('You should print a single letter')
            continue
        if not letter.isalpha() or not letter.islower():
            print('It is not an ASCII lowercase letter')
            continue
        if letter in input_letters:
            print('You already typed this letter')
            continue
        if letter not in correct_word:
            mistakes += 1
            print('No such letter in the word')
        input_letters.add(letter)
    else:
        print('You are hanged!')
    print()
