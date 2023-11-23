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

spicy_foods = [
    {"name": "Green Curry", "spiciness": "Medium"},
    {"name": "Buffalo Wings", "spiciness": "Hot"},
    {"name": "Mapo Tofu", "spiciness": "Spicy"}
]

result_names = get_names(spicy_foods)
print(result_names)

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food.get("heat_level", 0) > 5]


spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}
]

result_spiciest = get_spiciest_foods(spicy_foods)
print(result_spiciest)

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get("name", "Unknown")
        cuisine = food.get("cuisine", "Unknown")
        heat_level = food.get("heat_level", 0)
        emojis = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {emojis}")


spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}
]

def get_spicy_food_by_cuisine(spicy_foods, target_cuisine):
    for food in spicy_foods:
        cuisine = food.get("cuisine", "")
        if cuisine == target_cuisine:
            return food
    return None

spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}
]

result_american = get_spicy_food_by_cuisine(spicy_foods, "American")
result_thai = get_spicy_food_by_cuisine(spicy_foods, "Thai")

print(result_american)
print(result_thai)


def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}
]

print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
    """
    Calculates the average heat level of all spicy foods in the list.

    Parameters:
    - spicy_foods (list): List of dictionaries representing spicy foods.

    Returns:
    - float: The average heat level.
    """
    if not spicy_foods:
        return 0  

    total_heat = sum(food["heat_level"] for food in spicy_foods)
    average_heat = total_heat / len(spicy_foods)
    return average_heat


spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}
]

average_heat = get_average_heat_level(spicy_foods)
print(average_heat)



def create_spicy_food(spicy_foods, spicy_food):
    """
    Adds a new spicy food to the original list of spicy foods.

    Parameters:
    - spicy_foods (list): The original list of spicy foods.
    - spicy_food (dict): The new spicy food to be added.

    Returns:
    - list: The updated list of spicy foods.
    """
    return spicy_foods + [spicy_food]


original_spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}
]

new_spicy_food = {"name": "Spicy Ramen", "cuisine": "Japanese", "heat_level": 7}

updated_spicy_foods = create_spicy_food(original_spicy_foods, new_spicy_food)
print(updated_spicy_foods)

