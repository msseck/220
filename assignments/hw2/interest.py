"""
Name: Marietou Seck
interest.py

Problem: <This program is meant to calculate the monthly interest charge on a credit account .>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    print("This program calculates the monthly interest charge of a credit card.")
    rate = eval(input("Enter the annual interest rate of the account: "))
    num_days = eval(input("Enter the number of days in the billing cycle: "))
    net = eval(input("Enter the previous (net) balance of the account: "))
    payment = eval(input("Enter the net payment amount received: "))
    payday = eval(input("Enter the day of payment: "))


    for i in range(12):
        end = num_days - payday
        monthly_charge = rate / 12
        bal_day = net * num_days
        pay_day = payment * end
        res = + bal_day - pay_day
        avg_bal = res / num_days
        monthly_charge = avg_bal * monthly_charge
    print("Your total is ", round(monthly_charge,2))
    print(round(934.65))


if __name__ == "__main__":
        main()

