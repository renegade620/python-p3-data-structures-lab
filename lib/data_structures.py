spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]


print(get_names(spicy_foods))


def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]


print(get_spiciest_foods(spicy_foods))
print()


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        level_of_heat = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {level_of_heat}")


print(print_spicy_foods(spicy_foods))


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return


print(get_spicy_food_by_cuisine(spicy_foods, "Sichuan"))
print()


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        level_of_heat = "🌶" * food["heat_level"]
        if level_of_heat > "🌶🌶🌶🌶🌶":
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {level_of_heat}")
    return "Success"


print(print_spiciest_foods(spicy_foods))
print()


def get_average_heat_level(spicy_foods):
    return sum(food["heat_level"] for food in spicy_foods) / len(spicy_foods)


print(get_average_heat_level(spicy_foods))


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

spicy_food = {
    "name": "Griot",
    "cuisine": "Haitian",
    "heat_level": 10,
}
print(create_spicy_food(spicy_foods, spicy_food))
