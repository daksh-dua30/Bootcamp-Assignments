
# # Task 1: MOVIE TICKET BOOKING WITH CONSTRUCTOR VALIDATION

print("\n------------- TASK 1: MOVIE TICKET BOOKING -------------\n")


class Ticket():
    def __init__(self, movie, seats_available, seats_requested, message=None):
        self.movie = movie
        self.seats_available = seats_available
        self.seats_requested = seats_requested
        self.message = message

    def display(self):
        if self.seats_requested <= self.seats_available:
            self.message = "Request fully met."
        else:
            self.message = "Invalid Request!"

        if self.seats_available <= self.seats_requested:
            confirmed_seats = self.seats_available
        else:
            confirmed_seats = self.seats_requested

        self.confirmed_seats = confirmed_seats

        return f"Movie Name: {self.movie}\nTickets confirmed: {self.confirmed_seats}\n{self.message}"


ticket1 = Ticket("Hello.", 7, 5)
ticket2 = Ticket("Hw r u?", 10, 6)
ticket3 = Ticket("Bye.", 5, 6)

print(ticket1.display())
print(ticket2.display())
print(ticket3.display())


# # Task 2: EMPLOYEE OBJECTS WITH DEFAULT CONSTRUCTOR VALUES

print("\n------------- TASK 2: EMPLOYEE OBJECT -------------\n")


class Employee():
    def __init__(self, name, department="General", bonus=0):
        self.name = name
        self.department = department
        self.bonus = bonus

    def annual_summary(self):
        total_pay = 30000 + self.bonus

        return f"Name: {self.name}\nDepartment: {self.department}\nTotal pay: {total_pay}\n"


emp1 = Employee('Daksh1', 'SOET', 5000)
emp2 = Employee('Daksh2', 'SOET')
emp3 = Employee('Daksh3')

print(emp1.annual_summary())
print(emp2.annual_summary())
print(emp3.annual_summary())


# # Task 3: SIMPLE INVENTORY SYSTEM WITH OBJECT LISTS

print("\n------------- TASK 3: SIMPLE INVENTORY SYSTEM -------------\n")


class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity


products = [Product(n, p, q) for n, p, q in [
    ("Ice Cream", 40, 2), ("Keventer Shake", 240, 2), ("Mixed fruit juice", 50, 2)]]


pr1 = products[0]
pr2 = products[1]
pr3 = products[2]


grand_total = 0

for product in products:
    value = product.total_value()

    print(f"Product: {product.name}")
    print(f"Total Value: {value}\n")

    grand_total += value

print("\nGrand Total:", grand_total)
print()
