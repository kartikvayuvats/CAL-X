import json


def load_meals():
    with open("data/meals.json", "r") as file:
        return json.load(file)


def save_meals(meals):
    with open("data/meals.json", "w") as file:
        json.dump(meals, file, indent=4)


def load_settings():
    with open("data/settings.json", "r") as file:
        return json.load(file)


def save_settings(settings):
    with open("data/settings.json", "w") as file:
        json.dump(settings, file, indent=4)