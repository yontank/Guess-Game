import requests
import json, sys, readchar
import random


banner = """
         
                                                                                            
 (_____)          ____  ____  ____    (__ _ __)(_)      ____    (_)  _  (_)        _       (_)
(_)  ___  _   _  (____)(____)(____)      (_)   (_)__   (____)   (_) (_) (_)  ___  (_)__  __(_)
(_) (___)(_) (_)(_)_(_)(_)__ (_)__       (_)   (____) (_)_(_)   (_) (_) (_) (___) (____)(____)
(_)___(_)(_)_(_)(__)__  _(__) _(__)      (_)   (_) (_)(__)__    (_)_(_)_(_)(_)_(_)(_)  (_)_(_)
 (_____)  (___)  (____)(____)(____)      (_)   (_) (_) (____)    (__) (__)  (___) (_)   (____)
                                                                                              
                                                                                              
"""



# Getting The Word
lines = open('./words.txt').read().splitlines()
word =random.choice(lines)

word = word.lower()


guessed_letters = []

print(banner)



def censored_word():
    return ''.join(c if c in guessed_letters else '_' for c in word)
print(censored_word())


def is_game_over():
    
    unique_letters_in_answer = ''.join(set(word))
    # Winning
    if (len(unique_letters_in_answer) == len(guessed_letters)):
        print("Congrats, You won!")
        return True
    
    # Losing
    if (attempts == 0):
        print("You lost, womp womp :(, the word was " + word)
        return True
    
    return False


attempts = 10

while(not is_game_over()):
    letter =  repr(readchar.readchar())[1]
 
    
    #Kill Switch
    if (letter == '\\'):
        exit(0)
    
    print(letter)
    if (letter in word and not (letter in guessed_letters)):
        print("Correct!")
        guessed_letters.append(letter)
    else:
        attempts-=1
        print("No no :(, attempts left " + str(attempts))
        
        
    guessed_word = censored_word()
    print(guessed_word)
    
    


