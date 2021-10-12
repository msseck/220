"""
Name:Marietou Seck
lab6.py

Problem: This program is meant to use python strings and lists.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name_input = input("Enter a person's name in first-last order:")
    name1, name2 = name_input.split()
    first_name = name1
    last_name = name2
    print(last_name + "," + first_name)


def company_name():
    company = input("Enter a three part internet domain:")
    comp_name = company.split(".")
    name = comp_name[1]
    print(name)


def initial():
    total_students = eval(input("How many names will be input?:"))
    for i in range(total_students):
        str_name = str(i + 1)
        first_name = input("Enter the first name of student " + str_name + ":")
        last_name = input("Enter " + first_name + "'s last name:")
        full_initial = first_name[0] + last_name[0]
        print(first_name + "'s initials are:", full_initial)


def names():
    first_last = input("Enter people's names, separated by commas:")
    name = first_last.split(",")
    print("The initials are ", end="")
    for i in range(len(name)):
        single_name = name[i].split()
        first_name = single_name[0]
        last_name = single_name[1]
        full_initial = first_name[0] + last_name[0]
        print(full_initial + " ", end="")


def thirds():
    total = eval(input("How many sentences will be input?:"))
    for i in range(total):
        str_name = str(i + 1)
        sentence = input("Enter sentence  " + str_name + ":")
        third_ch = ""
        for j in range(2, len(sentence), 3):
            third_ch = third_ch + sentence[j]
        print("Every third character of sentence " + str_name + " is:", third_ch)


def word_average():
    total_sentences = eval(input("How many sentences will be input?:"))
    for i in range(total_sentences):
        str_name = str(i + 1)
        sentence = input("Enter sentence  " + str_name + ":")
        for j in range(len(sentence)):
            total_length = len(sentence)
            word_sent = total_length.split()
            words = len(word_sent)
            avg = words / len(word_sent)
            print("The average word length for sentence" + str_name + "is:", avg)


def main():
    name_reverse()
    company_name()
    initial()
    names()
    thirds()
    word_average()


main()
