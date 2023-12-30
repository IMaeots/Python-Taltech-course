"""Library API."""
import re


class Person:
    """Person that has data about books borrowed and so-on."""

    def __init__(self):
        """Construct a person."""


class LibraryStats:
    """LibraryStats is important for saving data and requesting them."""

    def __init__(self, filename):
        """Construct the object by reading the file.

        file format: kuupäev;raamatu nimi;laenutaja nimi;tegevus
        """
        self.user_transactions = {}
        self.book_transactions = {}

        with open(filename, 'r') as f:
            lines = f.readlines()

            for line in lines:
                parts = line.strip().split(';')
                date, book, borrower, action = parts

                if borrower not in self.user_transactions:
                    self.user_transactions[borrower] = []
                self.user_transactions[borrower].append(book)

                if book not in self.book_transactions:
                    self.book_transactions[book] = []
                self.book_transactions[book].append((action, date))

    def get_borrower_names(self) -> list[str]:
        """Return a list of borrowers' names."""
        return list(self.user_transactions.keys())

    def get_book_titles(self) -> list[str]:
        """Return a list of book titles."""
        return list(self.book_transactions.keys())

    def get_total_transactions(self) -> int:
        """Return the sum of total transactions."""
        return sum(len(value) for value in self.book_transactions.values())

    def get_total_borrows_of_book(self, book_name: str) -> int:
        """Return the num of times a book has been borrowed."""
        if book_name in self.book_transactions:
            return sum(1 for action, date in self.book_transactions[book_name] if action == "laenutus")
        else:
            return 0

    def get_total_borrows_by(self, borrower_name: str) -> int:
        """Return the num of times the person has borrowed books."""
        return len(self.user_transactions[borrower_name])

    def get_favourite_book(self, borrower_name: str) -> str:
        """Return the most borrowed book by the person."""
        my_list = self.user_transactions[borrower_name]
        return max(my_list, key=my_list.count)

    def get_borrow_history(self, borrower_name: str) -> list[str]:
        """Return a list of books borrowed by person."""
        return self.user_transactions[borrower_name]

    def get_most_frequent_borrower(self, book_name: str) -> str:
        """Return the person with the most borrows."""
        return max(self.user_transactions, key=lambda x: len(self.user_transactions[x]))

    def get_borrow_dates(self, book_name: str) -> list[str]:
        """Return a list of dates when book was borrowed."""
        return [date for action, date in self.book_transactions[book_name]]

    def get_current_status(self, book_name: str) -> str:
        """Return the status of book - 'laenutatud' or 'tagastatud'."""
        if book_name in self.book_transactions:
            return self.book_transactions[book_name][-1]
        else:
            return "tagastus"


class Controller:
    """Communicate with LibraryStats functionality."""

    def __init__(self, library_stats: LibraryStats):
        """Construct the controller that has all necessary information."""
        self.library_stats = library_stats
        self.path_function_map = {
            r'/book/([^/]+)/borrows': self.library_stats.get_total_borrows_of_book,
            r'/book/([^/]+)/most-frequent-borrower': self.library_stats.get_most_frequent_borrower,
            r'/book/([^/]+)/borrow-dates': self.library_stats.get_borrow_dates,
            r'/book/([^/]+)/current-status': self.library_stats.get_current_status,
            r'/book/([^/]+)/total-borrows': self.library_stats.get_total_borrows_by,
            r'/book/([^/]+)/favourite-book': self.library_stats.get_favourite_book,
            r'/book/([^/]+)/borrow-history': self.library_stats.get_borrow_history,
        }

    def get(self, path: str):
        """Get request."""
        if path == '/books':
            return self.library_stats.get_book_titles()
        elif path == '/borrowers':
            return self.library_stats.get_borrower_names()
        elif path == '/total':
            return self.library_stats.get_total_transactions()

        match = None
        for pattern, func in self.path_function_map.items():
            match = re.match(pattern, path)
        if match:
            name = match.group(1)
            return func(name)

        # Handle cases where no match was found
        return "No matching route found"


"""        
        match = re.match(r'/book/([^/]+)/borrows', path)
        if match:
            name = match.group(1)
            return self.library_stats.get_total_borrows_of_book(name)

        match = re.match(r'/book/([^/]+)/most-frequent-borrower', path)
        if match:
            name = match.group(1)
            return self.library_stats.get_most_frequent_borrower(name)

        match = re.match(r'/book/([^/]+)/borrow-dates', path)
        if match:
            name = match.group(1)
            return self.library_stats.get_borrow_dates(name)

        match = re.match(r'/book/([^/]+)/current-status', path)
        if match:
            name = match.group(1)
            return self.library_stats.get_current_status(name)

        match = re.match(r'/book/([^/]+)/total-borrows', path)
        if match:
            name = match.group(1)
            return self.library_stats.get_total_borrows_by(name)

        match = re.match(r'/book/([^/]+)/favourite-book', path)
        if match:
            name = match.group(1)
            return self.library_stats.get_favourite_book(name)

        match = re.match(r'/book/([^/]+)/borrow-history', path)
        if match:
            name = match.group(1)
            return self.library_stats.get_borrow_history(name)
"""

if __name__ == "__main__":
    library_stats = LibraryStats('data.txt')
    controller = Controller(library_stats)

    pass
