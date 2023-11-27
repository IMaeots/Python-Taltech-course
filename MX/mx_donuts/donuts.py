"""Mama's donuteria."""
import math


class Donut:
    """Donut class."""

    def __init__(self, name: str, price: float, ingredients: list, allergies: list):
        """
        Initialize a donut object.

        :param name: The name of the donut.
        :param price: The price of the donut.
        :param ingredients: Ingredients.
        :param allergies: Allergies.
        """
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.allergies = allergies

    def __repr__(self):
        """Return a string representation of the Donut object."""
        return f"{self.name}, {self.price}, {self.ingredients}, {self.allergies}"


def sort_donuts_by_price(donut_list: list[Donut]) -> list[str]:
    """
    Sort donuts by their price in ascending order.

    :param donut_list: List of Donut objects.
    :return: List of Donut names sorted by price.
    """
    return list(map(lambda x: x.name, sorted(donut_list, key=lambda x: x.price)))


def find_most_expensive_donut(donut_list: list[Donut]) -> str:
    """
    Find the name of the most expensive donut.

    :param donut_list: List of Donut objects.
    :return: Name of the most expensive donut.
    """
    return max(donut_list, key=lambda x: x.price).name


def find_donuts_with_ingredient(donut_list: list[Donut], ingredient: str) -> list[str]:
    """
    Find donuts that contain a specific ingredient.

    :param donut_list: List of Donut objects.
    :param ingredient: Ingredient that_ donut must contain.
    :return: List of Donut names containing the specified ingredient.
    """
    return list(map(lambda x: x.name, filter(lambda x: ingredient in x.ingredients, donut_list)))


def list_donut_names_and_prices(donut_list: list[Donut]) -> list[tuple]:
    """
    Create a list containing the names and prices of donuts.

    :param donut_list: List of donut objects.
    :return: List of tuples containing donut names and prices.
    """
    return list(map(lambda x: (x.name, x.price), donut_list))


def list_donuts_starting_with(donut_list: list[Donut], letter: str) -> list[str]:
    """
    Find donuts whose names start with a specific letter and sort them alphabetically.

    :param donut_list: List of Donut objects.
    :param letter: The starting letter to filter donut names by.
    :return: List of Donut names sorted alphabetically.
    """
    return list(map(lambda x: x.name, sorted(filter(lambda x: x.name[0] == letter, donut_list), key=lambda x: x.name)))


def find_flour_needed_for_baking(donut_list: list[Donut], quantity: int) -> int:
    """
    Calculate the amount of flour needed to bake a certain quantity of each donut.

    Bakery needs 80 grams of flour multiply by donut price to bake one.

    :param donut_list: List of Donut objects.
    :param quantity: The quantity of each donut to be baked.
    :return: Total amount of flour needed in grams rounded up.
    """
    return math.ceil((sum(map(lambda x: ((x.price * 80) * quantity), donut_list))))


def calculate_tip(donut_list: list[Donut], customers: int) -> int:
    """
    Calculate the tip amount that will be left.

    Every customer visiting bakery will buy one of each sugar containing donuts and leave 20% tip.

    :param donut_list: List of Donut objects.
    :param customers: Number of customers visiting bakery.
    :return: Tip amount.
    """
    return int((sum(map(lambda x: ((x.price * 0.2 if 'sugar' in x.ingredients else 0) * customers), donut_list))))


def sort_donuts_by_allergies(donut_list: list[Donut]) -> list[str]:
    """
    Sort donuts by the number of allergies they contain.

    The more allergies the higher on the list.
    In case of a tie sort alphabetically by donut name.

    :param donut_list: List of Donut objects.
    :return: List of Donut names sorted by allergies and then alphabetically.
    """
    return list(map(lambda x: x.name, sorted(donut_list, key=lambda x: (-len(x.allergies), x.name))))


def calculate_profit_per_day(donut_list: list[Donut], quantity_per_day: int, cost_per_donut: float) -> int:
    """
    Calculate profit per day for selling a certain quantity of each donut.

    :param donut_list: List of Donut objects.
    :param quantity_per_day: The quantity of each donut sold per day.
    :param cost_per_donut: The cost to make each donut.
    :return: Profit per day rounded down.
    """
    return sum(map(lambda x: ((x.price - cost_per_donut) * quantity_per_day), donut_list))


def find_most_popular_donut(donut_list: list[Donut]) -> str:
    """
    Find the most popular donut based on the number of allergies (fewer allergies are more popular).

    In case of a tie the most popular donut is with lower price.

    :param donut_list: List of Donut objects.
    :return: The name of the most popular donut.
    """
    return sorted(donut_list, key=lambda x: (len(x.allergies), x.price))[0].name


def sort_donuts_alphabetically_by_name(donut_list: list[Donut]) -> list[str]:
    """
    Sort donuts alphabetically by name.

    :param donut_list: List of Donut objects.
    :return: List of Donut names sorted alphabetically.
    """
    return list(map(lambda x: x.name, sorted(donut_list, key=lambda x: x.name)))


def find_donuts_costing_more_than(donut_list: list[Donut], price_threshold: float) -> list[str]:
    """
    Find donuts that cost more than a specified price.

    :param donut_list: List of Donut objects.
    :param price_threshold: The minimum price threshold.
    :return: List of Donut names that cost more than the specified threshold.
    """
    return list(map(lambda x: x.name, filter(lambda x: x.price > price_threshold, donut_list)))


def find_donuts_with_no_allergy(donut_list: list[Donut], allergy: str) -> list[str]:
    """
    Find donuts with no occurrence of a specific allergy.

    :param donut_list: List of Donut objects.
    :param allergy: The allergy to exclude.
    :return: List of Donut names with no occurrence of the specified allergy.
    """
    return list(map(lambda x: x.name, filter(lambda x: allergy not in x.allergies, donut_list)))


if __name__ == '__main__':
    donut1 = Donut("Chocolate Glazed Donut", 1.99, ["chocolate", "sugar"], ["dairy", "nuts", "chocolate"])
    donut2 = Donut("Strawberry Sprinkle Donut", 1.49, ["strawberry", "sprinkles"], ["gluten"])
    donut3 = Donut("Vanilla Cream-Filled Donut", 2.29, ["vanilla", "sugar"], ["dairy"])
    donut4 = Donut("Cinnamon Sugar Donut", 1.29, ["cinnamon", "sugar"], ["dairy", "gluten"])
    donut5 = Donut("Special Donut", 2.90, ["sugar", "vanilla", "sprinkles", "chocolate"], ["dairy"])
    donut6 = Donut("Chocolate Donut", 1.79, ["chocolate", "sprinkles"], ["nuts", "chocolate"])
    donut7 = Donut("Plain Glazed Donut", 0.99, ["sugar"], ["dairy"])

    donut_list = [donut1, donut2, donut3, donut4, donut5, donut6, donut7]

    print("\nSorted by price: \n" + str(sort_donuts_by_price(donut_list)) + "\n")
    # ['Plain Glazed Donut', 'Cinnamon Sugar Donut', 'Strawberry Sprinkle Donut',
    # 'Chocolate Donut', 'Chocolate Glazed Donut', 'Vanilla Cream-Filled Donut', 'Special Donut']

    print("Most expensive: \n" + str(find_most_expensive_donut(donut_list)) + "\n")
    # Special Donut

    print(
        "Donuts with chocolate as an ingredient: \n" + str(find_donuts_with_ingredient(donut_list, "chocolate")) + "\n")
    # ['Chocolate Glazed Donut', 'Special Donut', 'Chocolate Donut']

    print("Donuts names and prices: \n" + str(list_donut_names_and_prices(donut_list)) + "\n")
    # [('Chocolate Glazed Donut', 1.99), ('Strawberry Sprinkle Donut', 1.49),
    # ('Vanilla Cream-Filled Donut', 2.29), ('Cinnamon Sugar Donut', 1.29),
    # ('Special Donut', 2.9), ('Chocolate Donut', 1.79), ('Plain Glazed Donut', 0.99)]

    print("Donuts names starting with S: \n" + str(list_donuts_starting_with(donut_list, "S")) + "\n")
    # ['Special Donut', 'Strawberry Sprinkle Donut']

    print("Flour amount needed: \n" + str(find_flour_needed_for_baking(donut_list, 68)) + "\n")
    # 69306

    print("Tip: \n" + str(calculate_tip(donut_list, 75)) + "\n")
    # 141

    print("Sorted by allergies: \n" + str(sort_donuts_by_allergies(donut_list)) + "\n")
    # ['Chocolate Glazed Donut', 'Chocolate Donut', 'Cinnamon Sugar Donut', 'Plain Glazed Donut',
    # 'Special Donut', 'Strawberry Sprinkle Donut', 'Vanilla Cream-Filled Donut']

    print("Profit per day: \n" + str(calculate_profit_per_day(donut_list, 125, 0.5)) + "\n")
    # 1155

    print("Most popular donut: \n" + str(find_most_popular_donut(donut_list)) + "\n")
    # 'Plain Glazed Donut'

    print("Alphabetically sorted: \n" + str(sort_donuts_alphabetically_by_name(donut_list)) + "\n")
    # ['Chocolate Donut', 'Chocolate Glazed Donut', 'Cinnamon Sugar Donut', 'Plain Glazed Donut', 'Special Donut',
    # 'Strawberry Sprinkle Donut', 'Vanilla Cream-Filled Donut']

    print("Price more than 2.0: \n" + str(find_donuts_costing_more_than(donut_list, 2.0)) + "\n")
    # ['Vanilla Cream-Filled Donut', 'Special Donut']

    print("Donuts without gluten: \n" + str(find_donuts_with_no_allergy(donut_list, "gluten")) + "\n")
    # ['Chocolate Glazed Donut', 'Vanilla Cream-Filled Donut', 'Special Donut', 'Chocolate Donut', 'Plain Glazed Donut']
