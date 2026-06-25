# # ====== ENCAPSULATION AND ACCESS CONTROL ======

# TASK 1: SECURE STUDENT RECORD

class Student:

    _count = 0

    def __init__(self, roll_no, marks, grade):
        self.__roll_no = roll_no
        self.__marks = marks
        self._grade = grade
        Student._count += 1

    @property
    def gpa(self):
        return (sum(self.__marks) / len(self.__marks)) / 10

    @property
    def marks(self):
        return self.__marks

    @property
    def roll_no(self):
        return self.__roll_no

    @marks.setter
    def marks(self, new_marks):

        for mark in new_marks:
            if not (0 <= mark <= 100):
                raise ValueError("Marks must be between 0 and 100")

        self.__marks = new_marks

    @classmethod
    def count(cls):
        return cls._count


s1 = Student(141, [80, 82, 73, 95, 58], "B")
s2 = Student(318, [85, 94, 93, 83, 98], "A")

print("Student Count:", Student.count())

print("Roll No:", s2.roll_no)
print("Marks:", s2.marks)
print("Grade:", s2._grade)
print("GPA:", s2.gpa)

s2.marks = [90, 91, 92, 93, 94]
print("New GPA:", s2.gpa)

# s2.marks = [101, 94, -1, 93, 0]
# print("GPA:", s2.gpa)


# TASK 2: LIBRARY BOOK MANAGER


class Book:
    def __init__(self, isbn, title, author, copies):
        self.__isbn = isbn
        self._title = title
        self._author = author
        self.__copies = copies

    def checkout(self, n):
        if n <= 0:
            raise ValueError(
                "No. of copies to checkout must be greater than 0.")
        if n > self.__copies:
            raise ValueError("No. of copies entered are not available.")
        self.__copies -= n
        return f"No. of copies bought: {n}. No. of copies left: {self.__copies}."

    def return_book(self, n):
        if n <= 0:
            raise ValueError(
                "No. of copies to checkout must be greater than 0.")
        if not isinstance(n, int):
            raise ValueError("Invalid number of copies entered.")
        self.__copies += n
        return f"No. of copies returned: {n}. No. of copies left: {self.__copies}."

    @property
    def isbn(self):
        return self.__isbn

    @property
    def copies(self):
        return f"Current number of copies of {self._title}: {self.__copies}"


b1 = Book(1234567891234, "The Book of Minds", "Phillip Ball", 5)
b2 = Book(1234567891234, "The Book of Mindless", "Daksh Dua", 1)


# print(b1._Book__isbn)  # name mangling
print(b1.isbn)  # the correct way to call it by using a getter
print(b1._title)
print(b1._author)
# print(b1._Book__copies)  # name mangling
print(b1.copies)

print(b1.checkout(4))
print(b1.return_book(2))
print(b1.copies)


# TASK 3: ATM MACHINE SIMULATION


class ATM:
    def __init__(self, pin, balance, owner):
        self.__pin = pin
        self.__balance = balance
        self._owner = owner
        self.__authenticated = False

    @property
    def balance(self):
        return f"Balance: {self.__balance}"

    @property
    def mini_statement(self):
        return f"Owner : {self._owner}\nBalance : {self.__balance}"

    def authenticate(self, pin):
        if pin == self.__pin:
            self.__authenticated = True
            print("Access granted")
        else:
            self.__authenticated = False

    def deposit(self, amount):
        if not self.__authenticated:
            raise ValueError("Please authenticate first")

        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        self.__balance += amount
        print(f"{amount} deposited.")

    def withdraw(self, amount):
        if not self.__authenticated:
            raise ValueError("Please authenticate first")

        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        if amount > self.__balance:
            raise ValueError("Not enough balance.")
        if amount > 20000:
            raise ValueError(
                "Withdraws upto 20,000 only allowed per transaction")
        self.__balance -= amount
        print(f"{amount} withdrawn.")


atm = ATM(123690, 5000, "Daksh")


print(atm.balance)
print()

atm.authenticate(123690)
atm.deposit(1000)
atm.withdraw(3000)

print(atm.mini_statement)
