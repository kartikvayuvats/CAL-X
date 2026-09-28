def get_food_name():
    while True:
        name = input("Enter food name: ").strip()

        if name:
            return name

        print("Food name cannot be empty.")


def get_positive_int(message):
    while True:
        try:
            value = int(input(message))

            if value < 0:
                print("Value cannot be negative.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def get_positive_float(message):
    while True:
        try:
            value = float(input(message))

            if value < 0:
                print("Value cannot be negative.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")