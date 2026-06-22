

# # Task 1: LIBRARY BOOK CLASS

print("\n------------- TASK 1: LIBRARY BOOK CLASS -------------\n")


class Book():
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def display_info(self):
        if self.is_borrowed == True:
            print(
                f"The title of the book is {self.title}, it's author is {self.author}, and it is borrowed.")
        else:
            print(
                f"The title of the book is {self.title}, it's author is {self.author}, and it is available.")


book1 = Book("Harry Potter", "J.K. Rowling", True)
book2 = Book("Life not lifing", "D.D.", True)
book3 = Book("I very Happy", "D.D.", False)

book1.display_info()
book2.display_info()
book3.display_info()


# # Task 2: BANK ACCOUNT CLASS WITH A BALANCE METHOD


print("\n------------- TASK 1: BANK ACCOUNT CLASS -------------\n")


class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient balance"):
        super().__init__(message)


class InvalidQuantityError(Exception):
    def __init__(self, message="Amount must be greater than 0"):
        super().__init__(message)


class BankAccount:
    def __init__(self, balance=0):
        if balance < 0:
            raise InvalidQuantityError("Initial balance cannot be negative")
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidQuantityError
        self.balance += amount
        print(f"Deposited: ₹{amount}")
        print(f"Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidQuantityError
        if amount > self.balance:
            raise InsufficientFundsError
        self.balance -= amount
        print(f"Withdrawn: ₹{amount}")
        print(f"Balance: ₹{self.balance}")


try:
    account1 = BankAccount(5000)

    account1.deposit(1000)
    account1.deposit(500)
    account1.withdraw(2000)
    account1.withdraw(1000)

    account2 = BankAccount(10000)

    account2.deposit(500)
    account2.deposit(500)
    account2.withdraw(11000)
    account2.withdraw(100)


except InvalidQuantityError as e:
    print("Error:", e)

except InsufficientFundsError as e:
    print("Error:", e)

finally:
    print("Session ended.")


# # Task 3: RECTANGLE CLASS PERIMETER AND AREA CLASS


print("\n------------- TASK 1: RECTANGLE CLASS -------------\n")


class Rectangle:
    def __init__(self, length=0, breadth=0):
        self.length = length
        self.breadth = breadth

    def perimeter(self):
        perimeter = 2 * (self.length + self.breadth)
        return perimeter

    def area(self):
        area = self.length * self.breadth
        return area


rectangle1 = Rectangle(10, 30)
print("Rectangle #1 area: ", rectangle1.area())
print("Rectangle #1 perimeter: ", rectangle1.perimeter())

print()

rectangle2 = Rectangle(20, 15)
print("Rectangle #2 area: ", rectangle2.area())
print("Rectangle #2 perimeter: ", rectangle2.perimeter())
