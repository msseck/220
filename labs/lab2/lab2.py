import math
"""
Name: Marietou Seck
lab2.py
Problem: This program will do input, output, and arithmetic problems.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def sum_of_three():
    x = eval(input("Enter the upper bound: "))
    sum_total = 0
    for three in range(0, x+1, 3):
        sum_total = sum_total+three
    print(sum)


sum_of_three()


def multiplication_table():
    for i in range(1, 11):
        print(i, end=": ")
        for num in range(1, 11):
            print(num*i, end=" ")
        print()
# end of loop


multiplication_table()


def triangle_area():
    a = eval(input("Enter the length of a:"))
    b = eval(input("Enter the length of b:"))
    c = eval(input("Enter the length of c:"))
    s = (a + b + c) / 2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area of the triangle=", area)
# end of loop


triangle_area()


def sumSquares():
    start = eval(input("Enter your starting number:"))
    end = eval(input("Enter your ending number:"))
    sum_total = 0
    for sum_s in range(start, end + 1):
        sum_total = sum_s**2 + sum_total
    print("The sum of the function is:", sum_total)
# end of loop


sumSquares()


def power():
    base = eval(input("Enter your base:"))
    exponent = eval(input("Enter your exponent:"))
    var = 1
    for num_total in range(exponent):
        var = var * base
    print("The total is:", var)
# end of loop


power()
