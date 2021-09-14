"""
Name:Marietou Seck
lab3.py
Problem: This program will do input, output, and arithmetic problems using for loops.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    total_grades = eval(input("How many grades do you have?:"))
    sum = 0
    for i in range(total_grades):
        message = "What is your grade for HW" + str(i+1) + ":"
        hwgrade = eval(input(message))
        sum = hwgrade + sum
    average_grade = sum / total_grades
    print("The average is:", average_grade)


average()


def tip_jar():
    sum = 0
    for i in range(5):
       jar_pass = "How much did you donate?:"
       donation = eval(input(jar_pass))
       sum = donation + sum
    total = sum
    print("The total amount of the tip jar is:", total)

tip_jar()

def newton():
    number_x = eval(input("What is the number x?: "))
    approximation_time = eval(input("How many times to improve the approximation?: "))
    first_approximation = number_x / 2
    for i in range(approximation_time):
        first_approximation = (first_approximation + number_x / first_approximation) / 2
    print("The final value of approximation is:", first_approximation)


newton()

def sequence():
    num_of_terms = eval(input("What is the number of terms in a series?:"))
    denom = 1
    for i in range(num_of_terms):
        denom = i % 2 * 2 + denom
        print(denom, end="  ")





sequence()

def pi():
    num_of_terms = eval(input("What is the number of terms in a series?:"))
    denom = 1
    total = 1
    for i in range(num_of_terms):
        denom = i % 2 * 2 + denom
        print(denom, end="  ")

        numer = (i + 1) % 2 + i + 1
        print(numer)

        total = total * numer / denom
    #total *
    print("Your approximation of pi is:", total *2 )

pi()



