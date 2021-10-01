"""
Name:Marietou Seck
traffic.py

Problem: This program will calculate traffic patterns.

Certification of Authenticity:
I certify that this assignment is entirely my own work,
 but I discussed it with: the CSL lab.
"""


def main():
    car_total = 0
    number_road = eval(input("How many roads were surveyed?"))
    for i in range(number_road):
        road_num = str(i+1)
        days = eval(input("How many days was road "+road_num + " surveyed?"))
        daily_total = 0
        for day in range(days):
            str_day = str(day+1)
            number_cars = eval(input("How many cars traveled on day " + str_day + "?"))
            daily_total = daily_total + number_cars
        car_avg = daily_total/days
        print("Road " + road_num + " average vehicles per day:", car_avg)
        car_total = car_total + daily_total
    print("The total number of vehicles traveled on all roads:", car_total)
    total_avg = car_total/number_road
    print("The average number of vehicles per road:", round(total_avg, 2))


if __name__ == "__main__":
    main()
