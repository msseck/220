"""
Name:Marietou Seck
Partner:Angela NgaNga
lab7.py

Problem: This program demonstrates writing functions that accept arguments,
return values, and modify an object in a parameter.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def cash_conversion():
    money = eval(input("Enter a number:"))
    print('You have: ${:.2f}'.format(money))


def encode():
    message = input('Enter a message to be encoded:')
    key_value = eval(input("Enter an integer key value:"))
    empty = ""
    for ch in message:
        letter = ord(ch)+key_value
        empty += chr(letter)
    print("Your encoded message is", empty)


def sphere_area(radius):
    new_radius = (4 * math.pi * radius**2)
    return new_radius


def sphere_volume(radius):
    new_radius = (4/3 * math.pi * radius**3)
    return new_radius


def sum_n(n):
    new_n = 0
    for i in range(n):
        new_n += 1 + i
    return new_n


def sum_n_cubes(n):
    new_n = 0
    for i in range(n):
        new_n += (1 + i)**3
    return new_n


def encode_better():
    message = input("Enter your original message to encode:")
    cipher_key = input("Enter your cipher key:")
    empty = ""
    for i in range(len(message)):
        letter = ord(message[i]) + ord(cipher_key[i]) - 97
        empty += chr(letter)
    print("Your encoded message is", empty)


def main():
    cash_conversion()
    encode()
    print(sphere_area(4))
    print(sphere_volume(4))
    print(sum_n(3))
    print(sum_n_cubes(3))
    encode_better()


pass


main()
