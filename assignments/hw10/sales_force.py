"""
Name:Marietou Seck
sales_force.py

Problem: This program demonstrates the use of objects with a list and list of objects.

Certification of Authenticity:
I certify that this assignment is entirely my own work and discussed with: csl lab.
"""
from sales_person import *


class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        in_file = open(file_name, 'r')
        person_line = in_file.readlines()
        for i in range(len(person_line)):
            data = person_line[i].split(",")
            person = SalesPerson(data[0], data[1])
            sales = data[2].split()
            for sale in sales:
                person.enter_sale(sale)
            self.sales_people.append(person)

    def quota_report(self, quota):
        report = []
        for i in range(len(self.sales_people)):
            report.append([self.sales_people[i].get_id(), self.sales_people[i].get_name(),
                           self.sales_people[i].total_sales(),
                           self.sales_people[i].total_sales() > quota])
        return report

    def top_seller(self):
        seller = self.sales_people[0]
        list_seller = []
        for i in range(1, len(self.sales_people)):
            if self.sales_people[i].compare_to(seller) == 1:
                seller = self.sales_people[i]
                list_seller = []
        for i in range(len(self.sales_people)):
            if self.sales_people[i].compare_to(seller) == 0:
                list_seller.append(self.sales_people[i])
        return list_seller

    def individual_sales(self, employee_id):
        for i in range(len(self.sales_people)):
            if self.sales_people[i].get_id() == employee_id:
                return self.sales_people[i]
        return None


def main():
    sales = SalesForce()
    sales.add_data("salesData.txt")
    quota_sales = sales.quota_report(900)
    print(quota_sales)
    print("top seller(s): ")
    seller_list = sales.top_seller()
    for i in seller_list:
        print(i)
    sales.individual_sales(123)


main()
