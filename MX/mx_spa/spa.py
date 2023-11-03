"""Spa."""
import random


# Exercise 1: Generate Spa Menu Prices
def generate_menu_prices(services: list) -> list:
    """
    Generate random prices for spa services.

    Prices have to be between 30 and 150.

    The result list should be in format [[service name, random price], ..].

    :param services: list of spa service names
    :return: list of service prices
    """
    return [[service, str("{:.2f}".format(random.uniform(30, 150)))] for service in services]


# Exercise 2: Create Spa Appointment Slots
def create_appointment_slots(hours: list, duration: int, date: str) -> list:
    """
    Generate available appointment slots for a specific date.

    The result for every hour in hours list should be in the format: "{date} {start time} - {end time}"
    Time is in format {hour}:00 (for example 1:00 or 15:00).
    The start and end times for every appointment are between 00:00 (inclusive) and 24:00 (exclusive).
    You don't have to validate the date.
    An example of on element: "2023-06-23 10:00 - 14:00".


    :param hours: list of spa working hours
    :param duration: duration of each appointment
    :param date: appointment date
    :return: list of available slots
    """
    return [f"{date} {hour}:00 - {hour + duration}:00" for hour in hours]


# Exercise 3: Discounted Spa Packages
def generate_package_names(adjectives: list) -> list:
    """
    Generate spa package names using given adjectives.

    The result list should have elements in the format: "{adjective} Spa Package"

    :param adjectives: list of adjectives to use in package names
    :return: list of spa package names
    """
    return [f"{adjective} Spa Package" for adjective in adjectives]


# Exercise 4: Customer Feedback
def filter_positive_feedback(feedback_data: list) -> list:
    """
    Filter positive feedback comments (rated 3 or better).

    :param feedback_data: list of feedback comments with grades (e.g., [["Excellent", 5], ["Bad", 1], ["OK", 3]])
    :return: list of positive feedback comments (e.g. ["Excellent", "OK"]
    """
    return [feedback[0] for feedback in feedback_data if feedback[1] >= 3]


# Exercise 5: Spa Employee Schedules
def generate_employee_schedules(employees: list, working_hours: list) -> list:
    """
    Generate schedules for spa employees.

    employees list contains a list of names (string).
    working_hours list contains a list of working times (string).
    Generate a list for every employee in the format:
    [name, working hour1, working hour2, working hour3, working hour4, working hour5]
    Working hours should be taken from the working hours list randomly.

    Each employee should have 5 working hours in his schedule.

    For example:
    With the input
    employees ["Mary", "John"]
    working_hours ["10:00 AM - 2:00 PM", "12:00 AM - 6:00 PM"]
    we can get:
    [
    ["Mary", "10:00 AM - 2:00 PM", "10:00 AM - 2:00 PM",
        "12:00 AM - 6:00 PM", "12:00 AM - 6:00 PM", "10:00 AM - 2:00 PM"],
    ["John", "10:00 AM - 2:00 PM", "10:00 AM - 2:00 PM",
        "12:00 AM - 6:00 PM", "12:00 AM - 6:00 PM", "12:00 AM - 6:00 PM"]
    ]

    :param employees: list of employee names
    :param working_hours: list of working hours for each day
    :return: list of employee schedules
    """
    return [[employee] + [random.choice(working_hours) for _ in range(5)] for employee in employees]


# Exercise 6: Spa Product Inventory
def generate_product_inventory(products: list, initial_quantity: int) -> list:
    """
    Generate spa product names and quantities in stock.

    You have to update initial quantity of the product by using calculate_product_quantity method.

    The result list should have elements in format [name, quantity].
    Name is taken from the products list, quantity is calculated using the function below.

    :param products: list of product names
    :param initial_quantity: initial quantity in stock
    :return: list of product names and quantities
    """
    return [[name] + [calculate_product_quantity(initial_quantity, name)] for name in products]


def calculate_product_quantity(initial_quantity: int, product: str) -> int:
    """
    Calculate the updated quantity of a product.

    Do not change this method!

    :param initial_quantity: initial quantity of the product
    :return: updated quantity
    """
    updated_quantity = len(product) * initial_quantity
    return updated_quantity


# Exercise 7: Spa Product Pairing
def generate_product_scents(product_types: list, scents: list) -> list:
    """
    Generate pairings of spa product types and scents.

    The result is a list of combinations. Each combination is a list of one product type and one scent.

    For example:
    product_types ["Lotion", "Shampoo"]
    scents ["Lavender", "Eucalyptus"]

    The result:
    [
        ["Lotion", "Lavender"],
        ["Lotion", "Eucalyptus"],
        ["Shampoo", "Lavender"],
        ["Shampoo", "Eucalyptus"]
    ]

    The order of the combinations is important: first loop over types, then over scents.

    :param product_types: list of spa product types (e.g., "Lotion", "Shampoo")
    :param scents: list of scents (e.g., "Lavender", "Eucalyptus")
    :return: list of paired product and scent combinations
    """
    return [[p_type] + [scent] for p_type in product_types for scent in scents]


# Exercise 8: Identify VIP Customers
def identify_vip_customers(customer_names: list) -> list:
    """
    Identify VIP customers and replace their names with "vip".

    Customer is "vip" if his name starts with uppercase.

    For example:
    customer_names = ["Mary", "john", "John"]
    result: ["vip", "john", "vip"]

    :param customer_names: list of customer names
    :return: list of customer names with VIPs marked as "vip"
    """
    return ["vip" if customer[0].isupper() else customer for customer in customer_names]


# Exercise 9: Spa Service Availability Checker
def check_service_availability(service_schedules: dict, date: str) -> list:
    """
    Check the availability of spa services for a given date.

    service_schedules is a dictionary, where the key is the name of the service (string)
    and the value is a list of dates when it is available (list of string).
    date is a string.
    The function should return all the services which are available for the given date.

    For example:

    service_schedules = {
        "Massage": ["2023-09-15", "2023-09-16"],
        "Facial": ["2023-09-15"],
        "Manicure": ["2023-09-14", "2023-10-15"],
        "Pedicure": [],
        "Sauna": ["2023-09-11", "2023-09-15"]
    }
    date = "2023-09-15"

    The result: ['Massage', 'Facial', 'Sauna']

    :param service_schedules: list of service schedules with dates
    :param date: date for which availability is checked
    :return: list of available spa services
    """
    return [service for service, times in service_schedules.items() if date in times]


if __name__ == '__main__':
    print("Exercise 1: Generate Spa Menu Prices")
    services = ["Massage", "Facial", "Manicure", "Pedicure", "Sauna"]
    prices = generate_menu_prices(services)
    print(prices)  # prices can differ, but it should look like this
    # [['Massage', 95.66], ['Facial', 62.72], ['Manicure', 97.96], ['Pedicure', 135.33], ['Sauna', 69.99]]

    print("\nExercise 2: Create Spa Appointment Slots")
    hours = [10, 11, 12, 14, 15, 16]
    duration = 2
    date = "2023-09-20"
    slots = create_appointment_slots(hours, duration, date)
    print(slots)  # ['2023-09-20 10:00 - 12:00', '2023-09-20 11:00 - 13:00', '2023-09-20 12:00 - 14:00',
    # '2023-09-20 14:00 - 16:00', '2023-09-20 15:00 - 17:00', '2023-09-20 16:00 - 18:00']

    print("\nExercise 3: Discounted Spa Packages")
    adjectives = ["Relaxing", "Pampering", "Ultimate", "Luxury", "Tranquil"]
    packages = generate_package_names(adjectives)
    print(packages)  # ['Relaxing Spa Package', 'Pampering Spa Package', 'Ultimate Spa Package',
    # 'Luxury Spa Package', 'Tranquil Spa Package']

    print("\nExercise 4: Customer Feedback")
    feedback_data = [["Good", 4], ["Poor", 2], ["Excellent", 5], ["Bad", 1], ["Average", 3]]
    positive_feedback = filter_positive_feedback(feedback_data)
    print(positive_feedback)  # ['Good', 'Excellent', 'Average']

    print("\nExercise 5: Spa Employee Schedules")
    employees = ["Therapist A", "Therapist B", "Receptionist"]
    working_hours = ["10:00 AM - 2:00 PM", "2:00 PM - 6:00 PM", "10:00 AM - 6:00 PM"]
    schedules = generate_employee_schedules(employees, working_hours)
    for schedule in schedules:
        print(schedule)
        # schedules can differ, but should look like this:
        # ['Therapist A', '10:00 AM - 2:00 PM', '10:00 AM - 6:00 PM', '2:00 PM - 6:00 PM', '2:00 PM - 6:00 PM',
        #   '10:00 AM - 2:00 PM']
        # ['Therapist B', '10:00 AM - 2:00 PM', '2:00 PM - 6:00 PM', '2:00 PM - 6:00 PM', '2:00 PM - 6:00 PM',
        #   '2:00 PM - 6:00 PM']
        # ['Receptionist', '10:00 AM - 2:00 PM', '10:00 AM - 2:00 PM', '10:00 AM - 2:00 PM', '10:00 AM - 2:00 PM',
        #   '2:00 PM - 6:00 PM']

    print("\nExercise 6: Spa Product Inventory")
    products = ["Lotion", "Shampoo", "Candles", "Robes"]
    initial_quantity = 1
    product_inventory = generate_product_inventory(products, initial_quantity)
    for product_info in product_inventory:
        print(f"{product_info[0]}: {product_info[1]} in stock")
        # Lotion: 6 in stock
        # Shampoo: 7 in stock
        # Candles: 7 in stock
        # Robes: 5 in stock

    print("\nExercise 7: Spa Product Pairing")
    product_types = ["Lotion", "Shampoo", "Candles"]
    scents = ["Lavender", "Eucalyptus", "Citrus"]

    product_scents_pairings = generate_product_scents(product_types, scents)
    for pairing in product_scents_pairings:
        print(f"Product: {pairing[0]}, Scent: {pairing[1]}")
        # Product: Lotion, Scent: Lavender
        # Product: Lotion, Scent: Eucalyptus
        # Product: Lotion, Scent: Citrus
        # Product: Shampoo, Scent: Lavender
        # Product: Shampoo, Scent: Eucalyptus
        # Product: Shampoo, Scent: Citrus
        # Product: Candles, Scent: Lavender
        # Product: Candles, Scent: Eucalyptus
        # Product: Candles, Scent: Citrus

    print("\nExercise 8: Identify VIP Customers")
    customer_names = ["Alice", "bob", "Charlie", "David", "eve"]
    vip_customer_names = identify_vip_customers(customer_names)
    print(vip_customer_names)  # ['vip', 'bob', 'vip', 'vip', 'eve']

    print("\nExercise 9: Spa Service Availability Checker")
    service_schedules = {
        "Massage": ["2023-09-15", "2023-09-16"],
        "Facial": ["2023-09-15"],
        "Manicure": ["2023-09-14", "2023-10-15"],
        "Pedicure": [],
        "Sauna": ["2023-09-11", "2023-09-15"]
    }
    date = "2023-09-15"

    available_services = check_service_availability(service_schedules, date)
    print(f"Available services at {date}: {available_services}")
    # Available services at 2023-09-15: ['Massage', 'Facial', 'Sauna']
