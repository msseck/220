"""
Name:Marietou Seck
sales_person.py

Problem: This program demonstrates the use of objects with a list and list of objects.

Certification of Authenticity:
I certify that this assignment is entirely my own work and discussed with: csl lab.
"""


class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(float(sale))

    def total_sales(self):
        total = 0
        for i in self.sales:
            total = total + i
        return total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        return False

    def compare_to(self, other):
        if other.total_sales() > self.total_sales():
            return -1
        elif self.total_sales() > other.total_sales():
            return 1
        else:
            return 0

    def __str__(self):
        return "{0}-{1}: {2}".format(self.employee_id, self.name, self.total_sales())


def main():
    sales = SalesPerson(10, "bob")
    print(sales.get_id())
    print(sales.get_name())
    sales.set_name("billy")
    print(sales.get_name())
    sales.enter_sale(2.75)
    sales.enter_sale(309.21)
    sales.enter_sale(42.37)
    print(sales.total_sales())
    print(sales.get_sales())
    print(sales.met_quota(396.7))
    sales1 = SalesPerson(14, "holly")
    sales1.enter_sale(2.03)
    sales1.enter_sale(305.21)
    sales1.enter_sale(57.37)
    print(sales.compare_to(sales1))
    print(sales)

main()
