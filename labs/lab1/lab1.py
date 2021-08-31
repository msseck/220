""""
Name:<Marietou Seck>
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area=", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    total_shots = eval(input("Total shots: "))
    total_shots_made = eval(input("Total shots made: "))
    shooting_percent = total_shots_made / total_shots * 100
    print("Percentage =", shooting_percent)


def coffee():
    coffee_cost = 10.50
    coffee_lbs = eval(input("Number of pounds of Coffee purchased: "))
    shipping_cost = 0.86
    fixed_cost = 1.50
    total_cost = (coffee_cost + shipping_cost) * coffee_lbs
    total_cost = total_cost + fixed_cost
    print("Total_cost =", total_cost)


def kilometers_to_miles():
    kilometer = eval(input("Number of Kilometers drove: "))
    km_in_a_mile = 1.61
    total_miles_drove = kilometer / km_in_a_mile
    print("total_miles_drove =", total_miles_drove)
