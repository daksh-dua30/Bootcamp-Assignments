# ====== UNIT CONVERTER ======


def weight():
    val = int(input("Enter the value: "))
    unit = input("Enter the unit (Kg/g/mg): ")
    new_unit = input("Enter the unit to change to (Kg/g/mg): ")

    unit = unit.lower().strip()
    new_unit = new_unit.lower().strip()

    if unit == new_unit:
        print("You are Retarded! 🫡")
    elif unit == "kg" and new_unit == "g":
        new_val = val*1000
        return f"{new_val} {new_unit}"
    elif unit == "kg" and new_unit == "mg":
        new_val = val*1000000
        return f"{new_val} {new_unit}"
    elif unit == "g" and new_unit == "kg":
        new_val = val/1000
        return f"{new_val} {new_unit}"
    elif unit == "g" and new_unit == "mg":
        new_val = val*1000
        return f"{new_val} {new_unit}"
    elif unit == "mg" and new_unit == "kg":
        new_val = val/1000000
        return f"{new_val} {new_unit}"
    elif unit == "mg" and new_unit == "g":
        new_val = val/1000
        return f"{new_val} {new_unit}"
    else:
        return "Invalid input"


def distance():
    val = int(input("Enter the value: "))
    unit = input("Enter the unit (Km/m): ")
    new_unit = input("Enter the unit to change to (Km/m): ")

    unit = unit.lower().strip()
    new_unit = new_unit.lower().strip()

    if unit == new_unit:
        print("You are Retarded! 🫡")
    elif unit == "km" and new_unit == "m":
        new_val = val*1000
        return f"{new_val} {new_unit}"
    elif unit == "m" and new_unit == "km":
        new_val = val/1000
        return f"{new_val} {new_unit}"
    else:
        return "Invalid input"


def time():
    val = int(input("Enter the value: "))
    unit = input("Enter the unit (Hr/min/sec): ")
    new_unit = input("Enter the unit to change to (Hr/min/sec): ")

    unit = unit.lower().strip()
    new_unit = new_unit.lower().strip()

    if unit == new_unit:
        print("You are Retarded! 🫡")
    elif unit == "hr" and new_unit == "m":
        new_val = val*60
        return f"{new_val} {new_unit}"
    elif unit == "hr" and new_unit == "sec":
        new_val = val*3600
        return f"{new_val} {new_unit}"
    elif unit == "m" and new_unit == "hr":
        new_val = val/60
        return f"{new_val} {new_unit}"
    elif unit == "m" and new_unit == "sec":
        new_val = val*60
        return new_val
    elif unit == "sec" and new_unit == "hr":
        new_val = val/3600
        return f"{new_val} {new_unit}"
    elif unit == "sec" and new_unit == "m":
        new_val = val/60
        return f"{new_val} {new_unit}"
    else:
        return "Invalid input"


while True:
    print("1. Weight\n 2. Distance\n 3. Time\n 4. Exit Program")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(weight())
    elif choice == 2:
        print(distance())
    elif choice == 3:
        print(time())
    elif choice == 4:
        break
    else:
        print("Invalid Choice")
