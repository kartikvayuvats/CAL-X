from storage import load_meals, load_settings


def calculate_daily_calories():
    meals = load_meals()

    total_calories = 0

    for meal in meals:
        total_calories += meal["calories"]

    return total_calories


def get_calorie_summary():
    meals = load_meals()
    settings = load_settings()

    total_calories = 0

    for meal in meals:
        total_calories += meal["calories"]

    daily_goal = settings["daily_calorie_goal"]
    remaining = daily_goal - total_calories

    return total_calories, daily_goal, remaining


def get_nutrition_summary():
    meals = load_meals()

    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0

    for meal in meals:
        total_calories += meal["calories"]
        total_protein += meal["protein"]
        total_carbs += meal["carbs"]
        total_fat += meal["fat"]

    return total_calories, total_protein, total_carbs, total_fat