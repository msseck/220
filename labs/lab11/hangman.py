"""
Name:Marietou Seck
hangman.py

Problem: This program demonstrates the use of functions, decision, and repetition structures
to make a game of hangman.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import random


# function to read wordlist.txt into a list
def read():
    in_file = open("wordlist.txt", "r")
    word_list = in_file.readlines()
    in_file.close()
    return word_list


# function to pick a random word into a string
def random_word(word_list):
    word = random.randint(0, len(word_list)-1)
    return word_list[word]


# function to return guessed word into a string
def guessed_word(word, past_guess):
    out_word = word
    for i in word:
        if i not in past_guess:
            out_word = out_word.replace(i, "_")
    return out_word


# function to see if all letters have been guessed
def all_guessed(word):
    for i in word:
        if i == "_":
            return False
    return True


def main():
    list_word = read()
    game_word = random_word(list_word)
    wrong_guess = []
    correct_guess = []
    guesses = 7
    guessed = guessed_word(game_word, "!")
    while not all_guessed(guessed) and guesses > 0:
        print("Guesses left:", guesses)
        print("Incorrect guesses:", wrong_guess)
        print(guessed)
        user_input = input("Enter a letter:")
        if user_input not in game_word:
            wrong_guess.append(user_input)
            if user_input in wrong_guess:
                guesses -= 1
        else:
            correct_guess.append(user_input)
        guessed = guessed_word(game_word, correct_guess)
    if all_guessed(guessed):
        print("You got it!")
    else:
        print("You lost")


main()
