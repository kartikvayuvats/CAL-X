from food import add_food
from calorie_tracker import view_meals
from nutrition import (
    get_calorie_summary,
    get_nutrition_summary
)
from storage import (
    load_settings,
    save_settings,
    load_meals,
    save_meals
)
from logger import log_activity


while True:

    print("\n========================================")
    print("           CALORIE TRACKER")
    print("========================================")

    print("1. Add Food")
    print("2. View Today's Meals")
    print("3. View Daily Calorie Summary")
    print("4. View Nutrition Summary")
    print("5. Set Calorie Goal")
    print("6. Delete Meal")
    print("7. Edit Meal")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    # ADD FOOD
    if choice == "1":
        add_food()

    # VIEW MEALS
    elif choice == "2":
        view_meals()
        log_activity("Meals viewed")

    # CALORIES
    elif choice == "3":

        total, goal, remaining = get_calorie_summary()

        print("\n--- DAILY CALORIE SUMMARY ---")
        print("Calories consumed :", total, "kcal")
        print("Daily goal        :", goal, "kcal")

        if remaining >= 0:
            print(
                "Calories remaining :",
                remaining,
                "kcal"
            )
        else:
            print(
                "Calories exceeded  :",
                abs(remaining),
                "kcal"
            )

        log_activity(
            "Daily calorie summary viewed"
        )

    # NUTRITION
    elif choice == "4":

        total, protein, carbs, fat = \
            get_nutrition_summary()

        print("\n--- NUTRITION SUMMARY ---")

        print(
            "Calories :",
            total,
            "kcal"
        )

        print(
            "Protein  :",
            round(protein, 2),
            "g"
        )

        print(
            "Carbs    :",
            round(carbs, 2),
            "g"
        )

        print(
            "Fat      :",
            round(fat, 2),
            "g"
        )

        log_activity(
            "Nutrition summary viewed"
        )

    # SET CALORIE GOAL
    elif choice == "5":

        settings = load_settings()

        try:

            goal = float(
                input(
                    "\nEnter your daily calorie goal: "
                )
            )

            if goal <= 0:
                print(
                    "Calorie goal must be greater than 0."
                )
                continue

            settings["daily_calorie_goal"] = goal

            save_settings(settings)

            print(
                "\n✓ Daily calorie goal "
                "updated successfully!"
            )

            log_activity(
                "Daily calorie goal updated"
            )

        except ValueError:

            print(
                "Please enter a valid number."
            )

    # DELETE MEAL
    elif choice == "6":

        meals = load_meals()

        if len(meals) == 0:
            print(
                "\nNo meals available to delete."
            )
            continue

        print("\n--- DELETE MEAL ---")

        for i, meal in enumerate(
            meals,
            start=1
        ):
            print(
                f"{i}. {meal['name']} - "
                f"{meal['calories']} kcal"
            )

        try:

            meal_number = int(
                input(
                    "\nEnter meal number to delete: "
                )
            )

            if (
                meal_number < 1
                or meal_number > len(meals)
            ):
                print("Invalid meal number.")
                continue

            deleted_meal = meals.pop(
                meal_number - 1
            )

            save_meals(meals)

            print(
                f"\n✓ {deleted_meal['name']} "
                "deleted successfully!"
            )

            log_activity(
                f"Meal deleted: "
                f"{deleted_meal['name']}"
            )

        except ValueError:

            print(
                "Please enter a valid number."
            )

    # EDIT MEAL
    elif choice == "7":

        meals = load_meals()

        if len(meals) == 0:
            print(
                "\nNo meals available to edit."
            )
            continue

        print("\n--- EDIT MEAL ---")

        for i, meal in enumerate(
            meals,
            start=1
        ):
            print(
                f"{i}. {meal['name']} - "
                f"{meal['calories']} kcal"
            )

        try:

            meal_number = int(
                input(
                    "\nEnter meal number to edit: "
                )
            )

            if (
                meal_number < 1
                or meal_number > len(meals)
            ):
                print("Invalid meal number.")
                continue

            meal = meals[
                meal_number - 1
            ]

            print("\nCurrent details:")
            print(
                "Food     :",
                meal["name"]
            )
            print(
                "Calories :",
                meal["calories"]
            )
            print(
                "Protein  :",
                meal["protein"]
            )
            print(
                "Carbs    :",
                meal["carbs"]
            )
            print(
                "Fat      :",
                meal["fat"]
            )

            print("\nEnter new details")

            name = input(
                "Food name: "
            ).strip()

            if name:
                meal["name"] = name

            calories = float(
                input("Calories: ")
            )

            protein = float(
                input("Protein (g): ")
            )

            carbs = float(
                input("Carbs (g): ")
            )

            fat = float(
                input("Fat (g): ")
            )

            if (
                calories < 0
                or protein < 0
                or carbs < 0
                or fat < 0
            ):
                print(
                    "Values cannot be negative."
                )
                continue

            meal["calories"] = calories
            meal["protein"] = protein
            meal["carbs"] = carbs
            meal["fat"] = fat

            save_meals(meals)

            print(
                "\n✓ Meal updated successfully!"
            )

            log_activity(
                f"Meal edited: "
                f"{meal['name']}"
            )

        except ValueError:

            print(
                "Please enter valid numbers."
            )

    # EXIT
    elif choice == "8":

        print(
            "\nThank you for using "
            "Calorie Tracker!"
        )

        log_activity(
            "Program exited"
        )

        break

    else:

        print(
            "\nInvalid choice. "
            "Please try again."
        )