"""Plants."""
import random


# Exercise 1: Create Plant Care Reminders
def create_care_reminders(plants: list, care_info: dict) -> dict:
    """Create care reminders for garden plants.

    Given a list of plant names and a dictionary containing care information for each plant
    (key is plant name and value is care info).
    Care reminders should be added to new dictionary, there key is plant from 'plants' list
    and value is care reminder in format "Don't forget to {care reminder}".


    :param plants: list of plant names
    :param care_info: dictionary with plant care information
    :return: dictionary with plants as keys and care reminders as values
    """
    return {plant: f"Don't forget to {reminder}" for plant, reminder in care_info.items() if plant in plants}


# Exercise 2: Identify Low-Cost Garden Plants
def identify_low_cost_plants(plant_prices: dict, max_price: float) -> dict:
    """
    Identify garden plants that are priced below a given threshold.

    Given a dictionary of plant prices (key is plant and value is price).
    You need create and return dictionary containing only plants with prices, that are below a max_price value.
    In the new dictionary, the key should represent a plant, and the corresponding value is the difference between
    the max_price and the price of that specific plant (i.e., max_price - price)

    :param plant_prices: dictionary of plant prices
    :param max_price: maximum price threshold
    :return: dictionary of low-cost garden plants
    """
    return {plant: max_price - price for plant, price in plant_prices.items() if price < max_price}


# Exercise 3: Calculate Garden Watering Schedule
def calculate_watering_schedule(plants: list, watering_frequency: int) -> dict:
    """
    Calculate the watering schedule for garden plants.

    Given a list of plants and an integer value representing the watering frequency.
    You need to create a dictionary where the key is the plant, and the value is the result of multiplying
    the watering frequency by the number of letters in the plant's name, divided by the plant's index in the list
    (to avoid division by zero, in this exercise, indexing starts from 1, not from 0).
    The resulting value is rounded to two decimal places.

    :param plants: list of plant names
    :param watering_frequency: frequency of watering in days
    :return: dictionary with plants as keys and watering days as values
    """
    return {name: round((len(name.strip()) * watering_frequency) / (plants.index(name) + 1), 2) for name in plants}


# Exercise 4: Calculate Total Garden Plant Costs
def calculate_total_plant_costs(plant_prices: dict, plant_inventory: dict) -> dict:
    """
    Calculate the total cost of garden plants.

    Given dictionary plant_prices, key is plant and value is it`s price. And dictionary plant_inventory,
    where key is plant and value is amount of this plant.
    Return dictionary where key will be plant and value total cost of this plant (price * amount).

    :param plant_prices: dictionary of plant prices
    :param plant_inventory: dictionary with amount of plants
    :return: dictionary with plants as keys and total cost as values
    """
    return {plant1: price * amount for plant1, price in plant_prices.items() for plant2, amount in
            plant_inventory.items() if plant1 == plant2}


# Exercise 5: Calculate Garden Space Requirements
def calculate_space_requirements(space_per_plant: dict, space_threshold: float) -> dict:
    """
    Calculate the space requirements for each garden plant and categorize them based on the space threshold.

    Given a dictionary with plants as keys and their required space in square feet as values,
    this function categorizes the plants into "High Space" or "Low Space" based on a specified
    space threshold.
    If plant space requirement is bigger than space_threshold, it is in "High Space" category,
    if plant space requirement is smaller or equal to space_threshold, it is in "Low Space" category.

    :param space_per_plant: dictionary with plants as keys and required space in square feet as values
    :param space_threshold: minimum space requirement threshold used to categorize plants
    :return: dictionary with plants as keys and "High Space" or "Low Space" as values
    """
    return {plant: ("High Space" if space > space_threshold else "Low Space")
            for plant, space in space_per_plant.items()}


# Exercise 6: Group Plants by Growth Type
def group_plants_by_growth_type(growth_type: dict) -> dict:
    """
    Group garden plants by their growth type.

    Given is dictionary with plants as keys and growth type as values.
    Create and return dictionary, where keys are growth types and values are lists with plants with that growth type.

    :param growth_type: dictionary with plants as keys and growth type as values
    :return: dictionary with growth types as keys and a list of plants with that growth type as values
    """
    return {growth: [plant for plant, g_type in growth_type.items() if g_type == growth]
            for growth in set(growth_type.values())}


# Exercise 7: Generate Garden Layout
def generate_garden_layout(rows: int, columns: int, plant_varieties: list, exclusion_list: list) -> dict:
    """
    Generate a garden layout with rows and columns, assigning random plant varieties to each location.

    Create and return dictionary, where keys are tuples (row, column) and value is random plant
    from plant_varieties in each location.
    Skip locations specified in the exclusion list.

    To create locations use rows and columns variables, for example rows = 2 and columns = 3, then locations are:
    (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)

    :param rows: number of rows in the garden
    :param columns: number of columns in the garden
    :param plant_varieties: available plants for layout
    :param exclusion_list: locations to be skipped
    :return: dictionary representing the garden layout
    """
    return {(r, c): random.choice(plant_varieties)
            for r in range(1, rows + 1)
            for c in range(1, columns + 1)
            if (r, c) not in exclusion_list}


# Exercise 8: Calculate Sunlight Requirements
def calculate_sunlight_requirements(plant_types: dict, sunlight_needs: dict, weather_condition: str) -> dict:
    """
    Calculate the sunlight requirements for each garden plant based on their type and current weather conditions.

    Create a dictionary with plants as keys and adjusted sunlight requirements as values based on their type
    and weather conditions. Only plants with type "Sun-Loving" are added to dictionary.
    If weather is 'sunny', sunlight value should be multiplied by 1.2. If weather is not 'sunny', sunlight value
    should be multiplied by 0.8.
    The adjusted sunlight requirements are rounded to two decimal places.

    :param plant_types: dictionary with plants as keys and their types (e.g., "Sun-Loving," "Shade-Loving") as values
    :param sunlight_needs: dictionary with plants as keys and sunlight needs in hours per day as values
    :return: dictionary with plants as keys and sunlight requirements as values
    """
    return {
        plant: round(sunlight_needs[plant] * 1.2 if weather_condition == 'sunny' else sunlight_needs[plant] * 0.8, 2)
        for plant, plant_type in plant_types.items() if plant_type == 'Sun-Loving'}


# Exercise 9: Count Plant Types
def count_plant_types(plants: list) -> dict:
    """
    Count the occurrence of each plant type in the garden.

    Create and return dictionary, where key is plant and value is amount of occurrences in the given list.

    :param plants: list of plant names
    :return: dictionary with plant types as keys and their counts as values
    """
    return {plant: plants.count(plant) for plant in set(plants)}


# Exercise 10: Determine Garden Plant Health
def determine_plant_health(plants: list, watering_frequency: dict, sunlight_hours: dict,
                           pest_infestation: dict) -> dict:
    """
    Exercise 10: Determine Garden Plant Health.

    Determine the health status of garden plants based on multiple factors such as watering frequency, sunlight hours,
    and pest infestation.

    Given list of all plants, and three dictionaries , where key is plant and value is corresponding
    information about plant.

    In this method You just need to create and return dictionary, where key is plant and value is it`s health status.
    Health status is based on health score of the plant.
    Calculations of health score have to be done in separate method (calculate_health_score())
    If plant score is bigger than 8, health status is 'Healthy'.
    If plant score is bigger than 5, health status is 'Needs Attention'.
    If plant score is smaller or equal 5, health status is 'Unhealthy'.

    :param plants: list of plant names
    :param watering_frequency: dict with plant names as keys and the number of times each plant is watered per week
    as values
    :param sunlight_hours: dict with plant names as keys and the number of hours of sunlight each plant receives
    per day as values
    :param pest_infestation: dict with plant names as keys and a boolean indicating whether each plant is
     affected by pest infestation
    :return: dict, where keys are plants and values are their health status
    """
    return {plant: 'Healthy' if calculate_health_score(plant,
                                                       watering_frequency.get(plant, 0),
                                                       sunlight_hours.get(plant, 0),
                                                       pest_infestation.get(plant, False)) > 8
    else 'Needs Attention' if calculate_health_score(plant,
                                                     watering_frequency.get(plant, 0),
                                                     sunlight_hours.get(plant, 0),
                                                     pest_infestation.get(plant, False)) > 5
    else 'Unhealthy' for plant in plants}


def calculate_health_score(plant: str, watering_frequency: int, sunlight_hours: float, pest_infestation: bool) -> float:
    """
    Calculate the health score of a plant based on watering frequency, sunlight hours, and pest infestation.

    The health score is determined by combining multiple factors related to the plant's care conditions:

    **Base Score:** The base score is calculated as the length of the plant's name.
    **Watering Score:** The watering score is derived by subtracting the watering frequency from 7, dividing the result
    by 2, taking the integer part and taking the maximum of 0 => (max(0, x)).
    **Sunlight Score:** The sunlight score is determined by dividing the number of sunlight hours by 4, taking the integer part,
       and capping the result at a minimum of 2 => (min(2, x)).
    **Pest Score:** The pest score is -3 if the plant is affected by pest infestation; otherwise, it is 0.

    The final health score is the sum of the base score, watering score, sunlight score, and pest score.

    :param plant: str, the name of the plant
    :param watering_frequency: int, the number of times the plant is watered per week
    :param sunlight_hours: float, the number of hours of sunlight the plant receives per day
    :param pest_infestation: bool, indicates whether the plant is affected by pest infestation
    :return: float, health score of the plant
    """
    base_score = len(plant)
    watering_score = max(0, (7 - watering_frequency) // 2)
    sunlight_score = min(2, int(sunlight_hours) // 4)
    pest_score = -3 if pest_infestation else 0

    health_score = base_score + watering_score + sunlight_score + pest_score
    return health_score


if __name__ == '__main__':
    # Define flower types
    plants = ["Rose", "Tulip", "Lily", "Daisy", "Sunflower", "Orchid"]

    # Exercise 1: Create Plant Care Reminders
    care_info = {
        "Rose": "Water daily",
        "Tulip": "Water every other day",
        "Lily": "Water twice a week",
        "Daisy": "Water every three days",
        "Sunflower": "Water every four days",
        "Orchid": "Mist every day",
    }
    care_reminders = create_care_reminders(plants, care_info)
    print("\nExercise 1: Create Plant Care Reminders")
    print(care_reminders)  # {'Rose': "Don't forget to Water daily",
    # 'Tulip': "Don't forget to Water every other day", 'Lily': "Don't forget to Water twice a week",
    # 'Daisy': "Don't forget to Water every three days", 'Sunflower': "Don't forget to Water every four days",
    # 'Orchid': "Don't forget to Mist every day"}

    # Exercise 2: Identify Low-Cost Garden Plants
    max_price = 5
    plant_prices = {"Rose": 5, "Tulip": 3, "Lily": 4, "Daisy": 2, "Sunflower": 6, "Orchid": 8}
    low_cost_plants = identify_low_cost_plants(plant_prices, max_price)
    print("\nExercise 2: Identify Low-Cost Garden Plants")
    print(low_cost_plants)  # {'Tulip': 2, 'Lily': 1, 'Daisy': 3}

    # Exercise 3: Calculate Garden Watering Schedule
    watering_schedule = calculate_watering_schedule(plants, 2)
    print("\nExercise 3: Calculate Garden Watering Schedule")
    print(watering_schedule)  # {'Rose': 8.0, 'Tulip': 5.0, 'Lily': 2.67, 'Daisy': 2.5, 'Sunflower': 3.6, 'Orchid': 2.0}

    # Exercise 4: Calculate Total Garden Plant Costs
    plant_prices = {"Rose": 5, "Tulip": 3, "Lily": 4, "Daisy": 2, "Sunflower": 6, "Orchid": 8}
    plant_inventory = {"Rose": 10, "Tulip": 20, "Lily": 15, "Daisy": 25, "Sunflower": 30, "Orchid": 5}
    total_plant_costs = calculate_total_plant_costs(plant_prices, plant_inventory)
    print("\nExercise 4: Calculate Total Garden Plant Costs")
    print(total_plant_costs)  # {'Rose': 50, 'Tulip': 60, 'Lily': 60, 'Daisy': 50, 'Sunflower': 180, 'Orchid': 40}

    # Exercise 5: Calculate Garden Space Requirements
    space_per_plant = {"Rose": 2, "Tulip": 1, "Lily": 4, "Daisy": 3, "Sunflower": 4, "Orchid": 10}
    space_requirements = calculate_space_requirements(space_per_plant, 3)
    print("\nExercise 5: Calculate Garden Space Requirements")
    print(space_requirements)
    # {'Rose': 'Low Space', 'Tulip': 'Low Space', 'Lily': 'High Space', 'Daisy': 'Low Space',
    # 'Sunflower': 'High Space', 'Orchid': 'High Space'}

    # Exercise 6: Group Plants by Growth Type
    growth_type = {
        "Rose": "Perennial",
        "Tulip": "Annual",
        "Lily": "Perennial",
        "Daisy": "Annual",
        "Sunflower": "Annual",
        "Orchid": "Perennial",
    }
    grouped_plants = group_plants_by_growth_type(growth_type)
    print("\nExercise 6: Group Plants by Growth Type")
    print(grouped_plants)  # {'Perennial': ['Rose', 'Lily', 'Orchid'], 'Annual': ['Tulip', 'Daisy', 'Sunflower']}

    # Exercise 7: Generate Garden Layout
    exclusion_list = [(1, 2), (2, 3), (3, 1)]
    garden_layout = generate_garden_layout(3, 4, plants, exclusion_list)
    print("\nExercise 7: Generate Garden Layout")
    print(garden_layout)  # (example layout, flowers can be in different positions)
    # {(1, 1): 'Sunflower', (1, 3): 'Sunflower', (1, 4): 'Sunflower', (2, 1): 'Sunflower', (2, 2): 'Tulip',
    # (2, 4): 'Orchid', (3, 2): 'Lily', (3, 3): 'Daisy', (3, 4): 'Sunflower'}

    # Exercise 8: Calculate Sunlight Requirements
    plant_types = {"Rose": "Sun-Loving", "Tulip": "Sun-Loving", "Lily": "Shade-Loving", "Daisy": "Mixed",
                   "Sunflower": "Sun-Loving"}
    sunlight_needs = {"Rose": 6, "Tulip": 4, "Lily": 5, "Daisy": 3, "Sunflower": 6, "Orchid": 5}
    weather_condition = 'sunny'
    sunlight_requirements = calculate_sunlight_requirements(plant_types, sunlight_needs, weather_condition)
    print("\nExercise 8: Calculate Sunlight Requirements")
    print(sunlight_requirements)  # {'Rose': 7.2, 'Tulip': 4.8, 'Sunflower': 7.2}

    # Exercise 9: Count Plant Types
    plants2 = ["Rose", "Tulip", "Lily", "Daisy", "Sunflower", "Orchid", "Daisy", "Sunflower", "Orchid",
               "Tulip", "Lily", "Daisy", "Sunflower", "Daisy", "Sunflower", "Orchid", "Orchid", "Orchid"]
    plant_types_count = count_plant_types(plants2)
    print("\nExercise 9: Count Plant Types")
    print(plant_types_count)  # {'Tulip': 2, 'Lily': 2, 'Daisy': 4, 'Sunflower': 4, 'Rose': 1, 'Orchid': 5}

    # Exercise 10: Determine Garden Plant Health
    watering_frequency = {"Rose": 3, "Tulip": 2, "Lily": 4, "Daisy": 3, "Sunflower": 2, "Orchid": 1}
    sunlight_hours = {"Rose": 6, "Tulip": 4, "Lily": 7, "Daisy": 5, "Sunflower": 6, "Orchid": 8}
    pest_infestation = {"Rose": False, "Tulip": True, "Lily": False, "Daisy": True, "Sunflower": False, "Orchid": False}
    plant_health = determine_plant_health(plants, watering_frequency, sunlight_hours, pest_infestation)
    print("\nExercise 10: Determine Garden Plant Health")
    print(plant_health)
    # {'Rose': 'Needs Attention', 'Tulip': 'Unhealthy', 'Lily': 'Needs Attention', 'Daisy': 'Unhealthy',
    # 'Sunflower': 'Healthy', 'Orchid': 'Healthy'}
