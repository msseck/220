"""
Name:Marietou Seck
mean.py

Problem: This program is meant to output the RMS (root-mean-square) average
the harmonic mean, and the geometric mean.

Certification of Authenticity:
I certify that this assignment is entirely my own work,
 but I discussed it with: Angela Nganga and the CSL lab
"""

import math


def main():
    rms_average = 0
    harm_mean = 0
    geo_mean = 1
    value = eval(input("Enter the values to be entered:"))
    for _ in range(value):
        values_needed = eval(input("Enter the value:"))
        rms_average = rms_average + values_needed ** 2
        harm_mean = harm_mean + (1/values_needed)
        geo_mean = geo_mean * values_needed
    rms_average_total = math.sqrt(rms_average / value)
    harm_mean_total = value/harm_mean
    geo_mean_total = geo_mean**(1/value)
    print(round(rms_average_total, 3))
    print(round(harm_mean_total, 3))
    print(round(geo_mean_total, 3))


if __name__ == "__main__":
    main()
