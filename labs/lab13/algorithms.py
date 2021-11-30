"""
Name:Marietou Seck
algorithm.py

Problem: This program demonstrates the use of binary search on data and the compare search/sort on algorithms

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import*


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


def is_in_binary(search_val, values):
    high = len(values)-1
    low = 0
    while low <= high:
        middle = (high + low)//2
        if values[middle] == search_val:
            return True
        elif values[middle] > search_val:
            high = middle - 1

        else:
            low = middle + 1
    return False


def selection_sort(values):
    length = len(values)
    for position in range(length-1):
        number = position
        for i in range(position + 1, length):
            if values[i] < values[number]:
                number = i
        values[position], values[number] = values[number], values[position]


def calc_area(rect):
    point1 = rect.getP1()
    point2 = rect.getP2()
    p1x = point1.getX()
    p2x = point2.getX()
    p1y = point1.getY()
    p2y = point2.getY()
    width = abs(p1x - p2x)
    length = abs(p1y - p2y)
    area = width * length
    return area


def rect_sort(rectangles):
    areas = len(rectangles)
    for small in range(areas - 1):
        num = small
        for i in range(small + 1, areas):
            if calc_area(rectangles[i]) < calc_area(rectangles[num]):
                num = i
        rectangles[small], rectangles[num] = rectangles[num], rectangles[small]


def main():
    area1 = Rectangle(Point(5, 5), Point(7, 8))
    area2 = Rectangle(Point(10, 10), Point(10, 10))
    area3 = Rectangle(Point(1, 2), Point(3, 4))
    rect_list = [area1, area2, area3]
    rect_sort(rect_list)
    for i in rect_list:
        print(calc_area(i), end=", ")

    pass


main()
