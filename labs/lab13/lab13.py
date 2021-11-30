"""
Name: Marietou Seck
lab13.py

Problem: This program demonstrates solving real world problems with the knowledge learned throughout the semester.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def trade_alert(filename):
    in_file = open(filename, 'r')
    numbers = in_file.read()
    line = numbers.split()
    time = 0
    for i in line:
        time = time + 1
        i = eval(i)
        if i > 830:
            print("Warning: The trade volume at " + str(time) + " seconds is more than 830")
        elif i == 500:
            print("Pay Attention!: The trade volume at " + str(time) + " seconds is equal to 500")
    in_file.close()


def main():
    trade_alert('trades.txt')
    pass


main()
