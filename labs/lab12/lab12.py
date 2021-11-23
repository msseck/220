"""
Name:Marietou Seck
lab12.py

Problem: This program demonstrates the use of while loops, list methods, and performance of linear search on data
to make a game of hangman.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import random


def find_and_remove_first(list, value):
    i = 0

    x = "Marietou"
    while i < len(list) and x not in list:
        if list[i] == value:
            list.insert(i, x)
            list.pop(i + 1)
        i = i + 1


def good_input():
    right_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    i = 0
    while i not in right_input:
        user_input = eval(input("Enter a number 1-10:"))
        if user_input > 10:
            print("number is too big")
        elif user_input < 1:
            print("number is too small")
        if user_input in right_input:
            return user_input


def num_digits():
    user_input = eval(input("Enter any number:"))
    while user_input > 0:
        i = 0
        number = user_input
        while number > 0:
            i = i + 1
            number //= 10
        print(i, "digits in number")
        user_input = eval(input("Enter any number:"))


def hi_lo_game():
    user_input = eval(input("Enter a random number in the range of 1-100:"))
    random_num = random.randint(1, 100)
    guesses = 7
    num_guesses = 0
    while num_guesses < 8:
        num_guesses = num_guesses + 1
        if user_input == random_num:
            print("you win in", num_guesses, "guesses")
            num_guesses = 10
        else:
            if user_input > random_num:
                print("number is too big")
            else:
                if user_input < random_num:
                    print("number is too small")
    if num_guesses == 8:
        print("You lost because you exceeded your amount of guesses")


def main():
    hi_lo_game()
    pass


main()
