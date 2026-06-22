# -------------Student Performance Analyzer-------------


print("========== Student Performance Analyzer ==========\n")
student_name = input("Enter Student Name: ")
student_marks = int(input("Enter Marks: "))


def student_report(name, marks=0):
    print("Name    :    ", name)
    print("Marks   :    ", marks)


print("\n------ Student Report ------\n")
student_report(student_name, student_marks)
print("\n--------------------------\n")


def add_bonus(marks):
    marks = marks + 5
    print("Inside Function Marks: ", marks)


add_bonus(student_marks)

print("Outside Function Marks:", student_marks)


print()
print("-------- Recursive Sum --------")
print()


def sum_marks(n):
    if n == 0:
        return 0
    elif n > 0:
        return sum_marks(n-1) + n


num = int(input("Enter a number for recursive sum: "))
print("Recursive sum = ", sum_marks(num))

print()
print("-------- Function stored in variable --------")
print()


def square(x):
    return x*x


def cube(x):
    return x**3


print("1 --> Square\n2--> Cube\n")
ch = int(input("Enter Choice(1/2) : "))
num2 = int(input("Enter number: "))

if ch == 1:
    func_var = square
    print("\nfunction stored in variable 'sq'")
elif ch == 2:
    func_var = cube
    print("\nfunction stored in variable 'cb'")
else:
    print("\nInvalid Choice")


def apply_operation(func, value):
    return func(value)


print()
print("Result = ", apply_operation(func_var, num2))
