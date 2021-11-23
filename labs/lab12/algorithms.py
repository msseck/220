"""
Name:Marietou Seck
algorithm.py

Problem: This program demonstrates the use of while loops, list methods, and performance of linear search on data
to make a game of hangman.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def read_data(filename):
    in_file = open(filename, 'r')
    i = in_file.read()
    list_split = i.split()
    print(list_split)
    x = 0
    while x < len(list_split):
        list_split[x] = eval(list_split[x])
    in_file.close()
    return list_split


def is_in_linear(search_val, values):
    i = 0
    while i < len(search_val):
        if search_val[i] == values:
            return True
        else:
            i = i + 1
    return False


def main():
    pass


main()
