# # ====== If, elif, else ======

# #  Task 1: Temprature advisor
temp = float(input("Enter the current temperature in Celcius: "))

if temp <= 0 and temp >= -50:
    print("Wear a heavy coat")
elif temp <= 15:
    print("Wear a jacket")
elif temp <= 30:
    print("Comfortable Weather")
elif temp > 30 and temp < 60:
    print("Wear light clothing and stay hydrated")
else:
    print("Invalid Input")


# # Task 2: Loan Eligibility Checker

mon_inc = float(input("Enter your monthly income: "))
exis_emi = float(input("Enter your existing EMI: "))

if mon_inc >= 30000 and exis_emi < 0.4*mon_inc:
    print("Eligibile for loan")
elif mon_inc < 30000 and mon_inc > 0:
    print("Income too low")
elif exis_emi >= 0.4*mon_inc:
    print("High debt burden")
else:
    print("Invalid input")


# # Task 3: Number guessing with hint

secret_num = 42
guess = int(input("Guess the secret number: "))

while True:
    if guess < secret_num:
        diff = secret_num - guess
        print(f"Too low. You are {diff} below the number")
    elif guess > secret_num:
        diff = guess - secret_num
        print(f"Too high. You are {diff} above the number")
    elif guess == secret_num:
        print("Correct guess!")

        break
    else:
        print("Invalid Input")
    guess = int(input("Guess the secret number: "))
