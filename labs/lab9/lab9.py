"""
Name:Marietou Seck
lab9.py

Problem: This program demonstrates accumulations and the use of conditional control structures.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def addTen(nums):
    for i in range(len(nums)):
        nums[i] += 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2


def sumList(nums):
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    return sum


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = eval(strList[i])


def writeSumOfSquares():
    in_file = input('What is the name of the input file? in .txt form:')
    in_file = open(in_file, 'r')
    out_file = open("sum_out.txt", 'w')
    for line in in_file:
        lines = line.split()
        toNumbers(lines)
        squareEach(lines)
        add_num = sumList(lines)
        print("Sum of Squares = " + str(add_num), file=out_file)
    in_file.close()
    out_file.close()


def starter():
    weight = float(input("Enter the player's weight:"))
    numWins = int(input("Enter the player's number of wins:"))
    if weight >= 150 and weight < 160 and numWins >= 5:
        print("Player can start")
    elif weight > 199 or numWins > 20:
        print("Player can start")
    else:
        print("Player cannot start")


def leapYear(year):
    num = year
    if (num % 4 == 0 and num % 100 != 0) or num % 400 == 0:
        return True
    return False


def main():
    strList = ["3", "5.7", "2"]
    print(strList)
    toNumbers(strList)
    print(strList)

    # writeSumOfSquares()

    # starter()
    year = 2000
    out = leapYear(year)
    print(out)
    pass


main()
