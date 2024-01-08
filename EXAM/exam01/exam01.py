"""Exam 1 (2024-01-05)."""


def replace_occurrences(text: str) -> str:
    """
    Replace all occurrences of the first character in the given text with '@', except for the first character itself.

    Examples:
    replace_occurrences("Banana")  -> Banana
    replace_occurrences("rear")  -> Rea@
    replace_occurrences("11a")  -> 1@a
    replace_occurrences("Aardvark")  -> A@rdv@rk

    :param text: The input text in which replacements will be made.
    :return string of the input text in which replacements will be made. Please note that the result always starts with
    capital letter and the rest are small letters.
    """
    text = text.strip()
    if len(text) <= 1:
        return text.capitalize()

    first_char_lower = text[0].lower()
    new_text = text[0]
    for char in text[1:]:
        if char.lower() == first_char_lower:
            new_text += '@'
        else:
            new_text += char

    return new_text.capitalize()


def swap_case_string(text: str) -> str:
    """
    Take a string and swap its uppercase and lowercase letters.

    Other symbols remain the same.

    :param text: Input text that you want to process.
    :return: Text where uppercase and lowercase letters are swapped.
    """
    return text.swapcase()


def sum_of_multipliers(first_num: int, second_num: int, limit: int) -> int:
    """
    Sum all unique multipliers for two numbers.

    The task is to find all the multipliers of two given numbers within the limit.
    Then, find the sum of those multipliers where duplicates are removed.

    All the numbers are positive integers.

    sum_of_multipliers(3, 5, 20) => 98
    We get: [3, 6, 9, 12, 15, 18] (21 is over the limit)
    and [5, 10, 15, 20]
    15 is in both lists, we only use it once, sum is 98

    sum_of_multipliers(3, 3, 20) => 63
    sum_of_multipliers(3, 1, 20) => 210

    :param first_num: first number
    :param second_num: second number
    :param limit: limit
    :return: sum of multiplies
    """
    nums = []
    x = 1
    while limit >= (x * first_num):
        nums.append(x * first_num)
        x += 1

    x = 1
    while limit >= (x * second_num):
        nums.append(x * second_num)
        x += 1

    return sum(set(nums))


def analyze_products(product_data: dict) -> dict:
    """
    Analyze product data and calculate statistics for each category.

    The function receives the input of the dictionary, where the keys are category names (strings),
    and the values are lists of dictionaries representing products.
    Each product dictionary have keys 'name' (string) and 'price' (float).
    Product prices are always greater than zero.

    Return:
        dict: A dictionary containing analysis results for each category.
        Each category is represented by a key, and the corresponding value is a dictionary
        with the following keys:
        - 'average price': The average price of products in the category, rounded to two decimal places.
        - 'products above average': A list of product names with prices above the category average.
        - 'products below average': A list of product names with prices below or equal to the category average.

    Example:
        product_data = {
            "Electronics": [
                {"name": "Laptop", "price": 1200},
                {"name": "Smartphone", "price": 800},
            ],
            "Clothing": [
                {"name": "T-shirt", "price": 20},
                {"name": "Jeans", "price": 50},
            ],
        }
        Output:
            {
                "Electronics": {
                    "average price": 1000.0,
                    "products above average": ["Laptop"],
                    "products below average": ["Smartphone"],
                },
                "Clothing": {
                    "average price": 35.0,
                    "products above average": ["Jeans"],
                    "products below average": ["T-shirt"],
                },
            }
    """
    if not product_data:
        return {}

    stats = {}
    for category, products in product_data.items():
        total_cost = 0
        for item in products:
            total_cost += item['price']

        current_average = round(total_cost / len(products), 2)
        products_above = []
        products_below = []
        for item in products:
            price = item['price']
            name = item['name']
            if price > current_average:
                products_above.append(name)
            else:
                products_below.append(name)

        stats[category] = {
            "average price": current_average,
            "products above average": products_above,
            "products below average": products_below
        }

    return stats


def revert_factorial(factorial, n=1) -> int:
    """
    Find the reverted factorial of a number.

    Input is a factorial result, find the original number.
    If the given number is not a factorial of any number return -1.
    Must be recursive!

    revert_factorial(0) => -1
    revert_factorial(120) => 5
    revert_factorial(121) => -1
    revert_factorial(39916800) => 11
    revert_factorial(51090942171709440000) => 21
    """
    if factorial == 1:
        return n
    elif factorial < 1:
        return -1

    new_fac = factorial / n
    if 0.999999999 < new_fac <= 1.000000001:
        return n

    return revert_factorial(new_fac, n + 1)


def matrix_correct_structure(matrix):
    """Verify that matrix has the correct structure or make it."""
    for row in matrix:
        if len(row) < len(matrix):
            total = 0
            for num1 in range(len(row)):
                total += row[num1]

            row.append(total)

    row_length = len(matrix[0])
    mat_length = len(matrix)
    if row_length > mat_length:
        matrix.append([])
        for num1 in range(row_length):
            total = 0
            for num2 in range(mat_length):
                total += matrix[num2][num1]

            matrix[mat_length].append(total)

    return matrix, row_length


def matrix_transpose(matrix: list) -> list:
    """
    Transpose the given matrix.

    If matrix is squared, then you can transpose this given matrix.
    Non-squared matrix should be modified to a square one.
    You can add column or row to the matrix by adding all values in the corresponding row or column.

    In this exercise you will need to add maximum one row or one column to matrix to make it squared.

    Examples:
    1)
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    matrix_transpose(matrix) => [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    2)
    matrix_non-squared = [[1, 2, 3],
                          [4, 5, 0]]
    you need to make from this matrix squared matrix
    add one more row to matrix:
    1  2  3
    +  +  +
    4  5  0
    5  7  3 => new row
    matrix after adding row:
    [[1, 2, 3],
     [4, 5, 0],
     [5, 7, 3]]

     matrix_transpose(matrix_non-squared) => [[1, 4, 5], [2, 5, 7], [3, 0, 3]]

     3)
     matrix_non-squared2 = [[1, 1],
                            [4, 6],
                            [3, 2]]

    to make new columns add all values in corresponding row:
    matrix after adding third column:
    1 + 1 = 2, 4 + 6 = 10, 3 + 2 = 5
    [[1, 1, 2],
     [4, 6, 10],
     [3, 2, 5]]

    matrix_transpose(matrix_non-squared2) => [[1, 4, 3], [1, 6, 2], [2, 10, 5]]

    4)
    matrix_empty = []
    matrix_transpose(matrix_empty) => []

    :param matrix:  The input matrix.
    :return: list of lists: The transposed matrix.
    """
    if not matrix:
        return []

    matrix, matrix_row_length = matrix_correct_structure(matrix)

    # Transpose.
    new_matrix = []
    for num1 in range(matrix_row_length):
        for num2 in range(matrix_row_length):
            if len(new_matrix) < (num1 + 1):
                new_matrix.append([])
            new_matrix[num1].append(matrix[num2][num1])

    return new_matrix


# Simple OOP


class Book:
    """Book class."""

    def __init__(self, title: str, author: str, isbn: str, pages: int):
        """
        Initialize Book.

        :param title: title of the book, use title case.
        :param author: author of the book, use title case.
        :param isbn: ISBN code of the book
        :param pages: number of pages in the book
        """
        self.title = title.title()
        self.author = author.title()
        self.isbn = isbn
        self.pages = pages

    def __repr__(self):
        """Represent Book."""
        return f'"{self.title}" by {self.author}'


class Library:
    """Library class."""

    def __init__(self):
        """Initialize Library."""
        self.books = []
        self.unique_books = []
        self.find_unique_books()

    def find_unique_books(self):
        """Assign all unique books."""
        isbns = []
        self.unique_books = []
        for book in self.books:
            if book.isbn not in isbns:
                self.unique_books.append(book)
                isbns.append(book.isbn)

    def get_books(self) -> list[Book]:
        """Return all books in the Library."""
        return self.books

    def add_book(self, book: Book):
        """
        Add a book to the Library.

        :param book: Book object to add
        """
        self.books.append(book)

    def remove_book(self, book: Book):
        """
        Remove a book if it exists in the Library.

        :param book: Book object to remove.
        """
        self.books.remove(book)

    def find_books_by_title(self, title: str) -> list[Book]:
        """
        Find all books by a given title.

        The search is case-insensitive.

        :param title: title of the book
        :return: books with the given title
        """
        return [book for book in self.books if book.title == title.title()]

    def find_books_by_author(self, author: str) -> list[Book]:
        """
        Find all books by a given author.

        The search is case-insensitive.

        :param author: author of the books
        :return: books by the given author
        """
        return [book for book in self.books if book.author == author.title()]

    def get_number_of_books(self) -> int:
        """Get the total number of books in the Library."""
        return len(self.books)

    def get_number_of_unique_books(self) -> int:
        """Get the number of unique books in the Library, determined by ISBN."""
        self.find_unique_books()
        return len(self.unique_books)

    def sort_books_alphabetically(self) -> list[Book]:
        """
        Sort the Library books alphabetically by title.

        :return: sorted books
        """
        return sorted(self.books, key=lambda x: x.title)

    def get_book_with_most_pages(self) -> Book:
        """
        Get the book from the Library that has the most pages.

        If multiple books have the same maximum number of pages, return the first book.
        """
        return max(self.books, key=lambda x: x.pages)

    def get_unique_books(self) -> list[Book]:
        """
        Return all unique books in the Library, determined by ISBN.

        If multiple books are with the same ISBN, first book must be included.
        """
        self.find_unique_books()
        return self.unique_books


# Complex OOP

class Topping:
    """Ice cream Topping."""

    def __init__(self, name: str, price: int):
        """Initialize topping."""
        self.name = name
        self.price = price


class IceCream:
    """Ice Cream."""

    def __init__(self, flavour: str, price: int):
        """Initialize ice cream."""
        self.flavour = flavour
        self.price = price
        self.toppings = []

    def add_topping(self, topping: Topping):
        """Add a topping to ice cream."""
        self.toppings.append(topping)
        self.price += topping.price

    def get_toppings(self) -> list[Topping]:
        """Return a list of toppings."""
        return self.toppings

    def __eq__(self, other):
        """Two IceCreams are equals, if they have the same flavour and the same toppings."""
        if self.flavour.lower() == other.flavour.lower() and set(self.toppings) == set(other.toppings):
            return True
        else:
            return False


class Customer:
    """Customer."""

    def __init__(self, name: str, money: int):
        """Initialize customer."""
        self.name = name
        self.money = money


class Kiosk:
    """Kiosk."""

    def __init__(self):
        """Initialize kiosk."""
        self.ice_cream_price = 250
        self.flavours = []
        self.toppings = []
        self.orders = []
        self.customer: Customer = None
        self.order: [IceCream] = None

    def change_default_ice_cream_price(self, new_price: int):
        """Change the default price for ice cream (the price without any toppings)."""
        if new_price > 0:
            self.ice_cream_price = new_price

    def add_ice_cream_flavour_to_kiosk(self, flavour: str):
        """Add new ice cream flavour to kiosk, 'chocolate' is the same as 'CHOCOLATE'. No duplicates."""
        if flavour.lower() not in self.flavours:
            self.flavours.append(flavour.lower())

    def add_topping_to_kiosk(self, topping: Topping):
        """Add new topping to the kiosk, if kiosk didn't already have that topping."""
        if topping not in self.toppings:
            self.toppings.append(topping)

    def get_all_ice_cream_flavours(self) -> list[str]:
        """Return all available ice cream flavours as lowercase strings, in the same order they were added."""
        return self.flavours

    def get_all_toppings(self) -> list[Topping]:
        """Return all available toppings in this kiosk, in the same order they were added."""
        return self.toppings

    def get_all_topping_names_sorted(self) -> list:
        """Return a list of toppings names, sorted by topping prices in decreasing order."""
        return list(map(lambda x: x.name, sorted(self.toppings, key=lambda x: -x.price)))

    def start_new_order(self, customer: Customer):
        """
        Open order for this customer.

        Can now start adding ice creams and toppings to order.
        """
        if self.order is None:
            self.customer = customer
            self.order = []

    def add_to_order_ice_cream(self, flavour: str):
        """Add ice cream to order, but only, if there is an order started."""
        if self.order is not None:
            if flavour.lower() in self.flavours:
                self.order.append(IceCream(flavour, self.ice_cream_price))

    def add_to_order_topping(self, topping: Topping):
        """Check if there is an order started and an ice cream ordered, then add topping to this ice cream."""
        if self.order is not None and len(self.order) > 0:
            ordered_ice_cream = self.order[-1]
            if topping in self.toppings:
                ordered_ice_cream.add_topping(topping)

    def pay_for_order(self):
        """Finish order."""
        if self.order is not None and len(self.order) > 0 and self.customer:
            total_price = self.__get_order_price()
            client = self.customer
            if client.money >= total_price:
                client.money = client.money - total_price
                self.orders.append(self.order)
                self.order = None
                return self.orders[-1]
            else:
                self.order = None
                return 'not enough money'

        self.order = None
        return None

    def get_all_orders(self) -> list:
        """Return all orders, in the same order they were ordered from the kiosk."""
        return self.orders

    def __discount_ice_cream(self, ice_cream: IceCream):
        """Ice cream is in the third order, add discount (cheapest topping for free)."""
        lowest_price_topping = None
        for top in ice_cream.toppings:
            if lowest_price_topping is None:
                lowest_price_topping = top.price
            else:
                if top.price < lowest_price_topping:
                    lowest_price_topping = top.price

        if lowest_price_topping is not None:
            ice_cream.price = ice_cream.price - lowest_price_topping
        return ice_cream

    def __get_order_price(self) -> int:
        """Calculate the price for the whole order."""
        if len(self.orders) % 3 == 2:
            order = []
            for ice in self.order:
                order.append(self.__discount_ice_cream(ice))
                self.order = order

        return sum(ice.price for ice in self.order)

    def get_all_orders_sorted(self) -> list:
        """
        Return all the orders sorted by the following criteria.

        Get all orders, but sorted by the amount of ice creams. (More ice creams per order, first).
        If multiple orders have the same amount of ice creams, sort those by price (more expensive order first).
        If multiple orders have the same amount of ice creams and same price, leave them in the order they were added.
        """
        return sorted(self.orders, key=lambda x: (-len(x), -sum(y.price for y in x)))

    def get_all_ordered_flavours(self) -> list:
        """Get a list of all the flavours of ice creams that were ordered, sorted alphabetically."""
        flavs = []
        for order in self.orders:
            for ice in order:
                flavour = ice.flavour.lower()
                if flavour not in flavs:
                    flavs.append(flavour)

        return sorted(flavs)
