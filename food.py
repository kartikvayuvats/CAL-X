
from validator import get_food_name, get_positive_int, get_positive_float
from storage import load_meals, save_meals


def add_food():
    print("\n--- ADD FOOD ---")

    food_name = get_food_name()

    calories = get_positive_int("Enter calories: ")

    protein = get_positive_float("Enter protein (g): ")

    carbs = get_positive_float("Enter carbohydrates (g): ")

    fat = get_positive_float("Enter fat (g): ")

    food = {
        "name": food_name,
        "calories": calories,
        "protein": protein,
        "carbs": carbs,
        "fat": fat
    }

    meals = load_meals()

    meals.append(food)

    save_meals(meals)

    print("\n✓ Food added and saved successfully!")