
# ------Safe Input Validator------
import csv
print("======== Safe Input Validator ========\n")


class NegativeNumberError(Exception):
    def __init__(self, message="Number must be positive"):
        self.message = message
        super().__init__(self.message)


def get_positive_int():
    while True:
        try:
            num = int(input("Enter a positive integer: "))
            if num < 0:
                raise NegativeNumberError
            return num
        except ValueError:
            print("Invalid input! Please enter an integer.")
        except NegativeNumberError as e:
            print(e)


number = get_positive_int()
print("You entered:", number)


# ------Robust File Processor------
print("======== Robust File Processor ========\n")


def process_csv(filepath):
    file = None

    try:
        file = open(filepath, "r")
        reader = csv.reader(file)
        data = []

        for row in reader:
            numbers = [float(value) for value in row]
            data.append(numbers)

        num_cols = len(data[0])
        print("Column Averages:")

        for col in range(num_cols):
            total = 0
            for row in data:
                total += row[col]

            average = total / len(data)
            print(f"Column {col + 1}: {average:.2f}")

    except FileNotFoundError:
        print("Error: File not found.")
    except csv.Error:
        print("Error: Malformed CSV data.")
    except ValueError:
        print("Error: CSV contains non-numeric data.")
    finally:
        if file:
            file.close()
            print("File closed.")


process_csv("marks.csv")


# ------Bank Acdount Simmulator------
print("======== Bank Acdount Simmulator ========\n")


class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient balance"):
        super().__init__(message)


class InvalidAmountError(Exception):
    def __init__(self, message="Amount must be greater than 0"):
        super().__init__(message)


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError

        self.balance += amount
        print(f"Deposited ₹{amount}")
        print(f"Current Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError

        if amount > self.balance:
            raise InsufficientFundsError

        self.balance -= amount
        print(f"Withdrawn ₹{amount}")
        print(f"Current Balance: ₹{self.balance}")


account = BankAccount(5000)
try:
    account.deposit(2000)
    account.withdraw(1500)
    account.deposit(1000)
    account.withdraw(3000)
except InvalidAmountError as e:
    print("Invalid Amount Error:", e)
except InsufficientFundsError as e:
    print("Insufficient Funds Error:", e)
finally:
    print("Transaction session ended.")
