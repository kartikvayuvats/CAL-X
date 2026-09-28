from storage import load_meals


def view_meals():
    print("\n--- TODAY'S MEALS ---")

    meals = load_meals()

    if len(meals) == 0:
        print("No meals added yet.")
        return

    for i, meal in enumerate(meals, start=1):

        print(f"\nMeal {i}")
        print("----------------------")

        print("Food     :", meal["name"])
        print("Calories :", meal["calories"], "kcal")
        print("Protein  :", meal["protein"], "g")
        print("Carbs    :", meal["carbs"], "g")
        print("Fat      :", meal["fat"], "g")