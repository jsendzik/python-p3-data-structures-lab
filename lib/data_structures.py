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
    names = []
    for food in spicy_foods:
        names.append(food["name"])
    return names
        

def get_spiciest_foods(spicy_foods):
    spicy = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spicy.append(food)
    return spicy

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {(food["heat_level"]) * "🌶"}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine == food["cuisine"]:
            return food

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    total = 0
    for food in spicy_foods:
        total += food["heat_level"]
    return total / (len(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    foods = spicy_foods
    new_foods = foods + [spicy_food]
    return new_foods
