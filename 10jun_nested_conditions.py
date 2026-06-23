
# # Task 1: Student Performance Classification

marks = float(input("Enter your marks: "))

if marks >= 40:
    print("Pass")
    if marks >= 90:
        print("Distinction")
    elif marks >= 75:
        print("First Division")
    elif marks >= 60:
        print("Second Division")

else:
    print("Third Division")


# # Task 2: Job Application Screener

age = int(input("Enter your age"))

degree = input("Degree (B.Tech/MCA): ").lower().strip()

cgpa = float(input("CGPA: "))

if age <= 40 and age >= 21:
    if degree == "b.tech" or degree == "mca":
        if cgpa >= 7.0:
            print("Interview shortlisted")
        else:
            print("cgpa is lower than 7.0")
    else:
        print("degree listed is not B.Tech or MCA")
else:
    print("Your age is not between 21 and 40")


# # Task 3: E-Commerce Discount Calculator

cart_total = float(input("Cart Total (in rupees): "))
premium_member = input("Are you a premium member (yes/no): ").lower().split()

if cart_total >= 5000:
    discount = cart_total*0.15
    print(discount)
    discounted_total = cart_total - discount
    print(discounted_total)
    if premium_member[0] == 'yes':
        discount_new = discounted_total*0.05

        discounted_total = discounted_total - discount_new

        print(
            f"originial price: {cart_total}\nDiscount: {discount_new + discount}\nFinal Price: {discounted_total}")
    else:
        print(
            f"originial price: {cart_total}\nDiscount: {discount}\nFinal Price: {discounted_total}")
elif cart_total < 5000:
    discount = cart_total*0.05
    discounted_total = cart_total - discount
    print(
        f"originial price: {cart_total}\nDiscount: {discount}\nFinal Price: {discounted_total}")
else:
    print("invalid total")
