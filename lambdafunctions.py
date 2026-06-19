# ------Custom Sorter------

from functools import reduce
students = [{"name": "Daksh", "gpa": 8.7}, {"name": "Disha", "gpa": 9.1}, {
    "name": "Star", "gpa": 8.5}, {"name": "Doggo", "gpa": 9.4}, {"name": "Alice", "gpa": 8.9}]

sorted_students = sorted(
    students, key=lambda student: student["gpa"], reverse=True)

top_3_students = sorted_students[:3]
for student in top_3_students:
    print(student["name"], ":", student["gpa"])


# ------Data Pipeline------


numbers = list(range(1, 21))
result = reduce(lambda x, y: x + y, map(lambda x: x**2,
                filter(lambda x: x % 2 != 0, numbers)))
print(result)


# ------Mini Calculator Factory------

def make_operator(op):
    if op == "+":
        return lambda x, y: x + y
    elif op == "-":
        return lambda x, y: x - y
    elif op == "*":
        return lambda x, y: x * y
    elif op == "/":
        return lambda x, y: x / y
    else:
        return None


add = make_operator("+")
subtract = make_operator("-")
multiply = make_operator("*")
divide = make_operator("/")

a = float(input("Enter number #1: "))
b = float(input("Enter number #2: "))

print("\nAddition:", add(a, b))
print("\nSubtraction:", subtract(a, b))
print("\nMultiplication:", multiply(a, b))
print("\nDivision:", divide(a, b))
