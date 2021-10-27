"""
Name:Marietou Seck
weighted_average.py

Problem: This program will use numeric data from a text file to
 calculate students grade average.

Certification of Authenticity:
I certify that this assignment is entirely my own work and discussed it with: CSL lab.
"""


def weighted_function(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    for line in in_file:
        name = line.split(':')
        fl_name = name[1].split()
        acc = 0
        for i in range(0, len(fl_name) - 1, 2):
            acc += eval(fl_name[i])

        if acc > 100:
            out_file.write(name[0] + "'s average: Error: The weights are more than 100. " + "\n")

        elif acc < 100:
            out_file.write(name[0] + "'s average:Error: The weights are less than 100." + "\n")

        else:
            accu = 0
            for j in range(0, len(fl_name) - 1, 2):
                accu += eval(fl_name[j]) * eval(fl_name[j + 1])
            accu = accu / 100
            out_file.write(name[0] + "'s average: " + str(round(accu, 1)) + "\n")
    out_file.write("Class average:" + str(round(accu, 1)) + "\n")

    in_file.close()
    out_file.close()


def main():
    weighted_function('grades.txt', 'avg.txt')


main()
