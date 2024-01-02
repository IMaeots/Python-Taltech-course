"""Exam0."""
import re
from typing import Optional


def find_capital_letters(s: str) -> str:
    """
    Return only capital letters from the string.

    #1

    If there are no capital letters, return empty string.
    The string contains only latin letters (a-z and A-Z).
    The letters should be in the same order as they appear in the input string.

    find_capital_letters("ABC") => "ABC"
    find_capital_letters("abc") => ""
    find_capital_letters("aAbBc") => "AB"
    """
    capital_letters = ""
    for char in s:
        if char.isupper():
            capital_letters += char

    return capital_letters


def close_far(a: int, b: int, c: int) -> bool:
    """
    Return if one value is "close" and other is "far".

    #2

    Given three ints, a b c, return true if one of b or c is "close" (differing from a by at most 1),
    while the other is "far", differing from both other values by 2 or more.

    close_far(1, 2, 10) => True
    close_far(1, 2, 3) => False
    close_far(4, 1, 3) => True
    """
    if b == a or (b - 1) == a or (b + 1) == a:
        if c != b and c != a and (c - 1) != b and (c + 1) != b and (c - 1) != a and (c + 1) != a:
            return True
    if c == a or (c - 1) == a or (c + 1) == a:
        if b != c and b != a and (b - 1) != c and (b + 1) != c and (b - 1) != a and (b + 1) != a:
            return True

    return False


def get_names_from_results(results_string: str, min_result: int) -> list:
    """
    Given a string of names and scores, return a list of names where the score is higher than or equal to min_result.

    #3

    Results are separated by comma (,). Result contains a score and optionally a name.
    Score is integer, name can have several names separated by single space.
    Name part can also contain numbers and other symbols (except for comma).
    Return only the names which have the score higher or equal than min_result.
    The order of the result should be the same as in input string.

    get_names_from_results("ago 123,peeter 11", 0) => ["ago", "peeter"]
    get_names_from_results("ago 123,peeter 11,33", 10) => ["ago", "peeter"]  # 33 does not have the name
    get_names_from_results("ago 123,peeter 11", 100) => ["ago"]
    get_names_from_results("ago 123,peeter 11,kitty11!! 33", 11) => ["ago", "peeter",  "kitty11!!"]
    get_names_from_results("ago 123,peeter 11,kusti riin 14", 12) => ["ago", "kusti riin"]
    """
    results = results_string.strip().split(',')
    pattern = r"([\s\w]+)\s{1}(\d+)"
    winners = []
    for element in results:
        match = re.search(pattern, element)
        if match and int(match.group(2)) >= min_result:
            winners.append(match.group(1))

    return winners


def tic_tac_toe(game: list) -> int:
    """
    Find game winner.

    #4

    The 3x3 table is represented as a list of 3 rows, each row has 3 element (ints).
    The value can be 1 (player 1), 2 (player 2) or 0 (empty).
    The winner is the player who gets 3 of her pieces in a row, column or diagonal.

    There is only one winner or draw. You don't have to validate whether the game is in correct (possible) state.
    I.e the game could have four 1s and one 0 etc.

    tic_tac_toe([[1, 2, 1], [2, 1, 2], [2, 2, 1]]) => 1
    tic_tac_toe([[1, 0, 1], [2, 1, 2], [2, 2, 0]]) => 0
    tic_tac_toe([[2, 2, 2], [0, 2, 0], [0, 1, 0]]) => 2

    :param game
    :return: winning player id
    """
    if game[0][0] == game[0][1] == game[0][2] != 0:
        return game[0][0]
    elif game[1][0] == game[1][1] == game[1][2] != 0:
        return game[1][0]
    elif game[2][0] == game[2][1] == game[2][2] != 0:
        return game[2][0]
    elif game[0][0] == game[1][0] == game[2][0] != 0:
        return game[0][0]
    elif game[0][1] == game[1][1] == game[2][1] != 0:
        return game[0][1]
    elif game[0][2] == game[1][2] == game[2][2] != 0:
        return game[0][2]
    elif game[0][0] == game[1][1] == game[2][2] != 0:
        return game[0][0]
    elif game[0][2] == game[1][1] == game[2][0] != 0:
        return game[0][2]
    else:
        return 0


def rainbows(field: str, lower=False) -> int:
    """
    Count rainbows.

    #5

    Function has to be recursive.

    assert rainbows("rainbowThisIsJustSomeNoise") == 1  # Lisaks vikerkaarele on veel sümboleid
    assert rainbows("WoBniar") == 1  # Vikerkaar on tagurpidi ja sisaldab suuri tähti
    assert rainbows("rainbowobniar") == 1  # Kaks vikerkaart jagavad tähte seega üks neist ei ole valiidne

    :param lower: if string is already lower or not
    :param field: string to search rainbows from
    :return: number of rainbows in the string
    """
    if not field or len(field) < 7:
        return 0

    if not lower:
        field = field.lower()
        lower = True

    if field[0:7] == "rainbow" or field[6::-1] == "rainbow":
        field = field[7:]
        total = 1
    else:
        field = field[1:]
        total = 0

    return rainbows(field, lower) + total


def longest_substring(text: str) -> str:
    """
    Find the longest substring.

    #6

    Substring may not contain any character twice.
    CAPS and lower case chars are the same (a == A)
    In output, the case (whether lower- or uppercase) should remain.
    If multiple substrings have same length, choose first one.

    aaa -> a
    abc -> abc
    abccba -> abc
    babcdEFghij -> abcdEFghij
    abBcd => Bcd
    '' -> ''
    """
    longest = ""
    current = ""
    for char in text:
        if char.lower() not in current.lower():
            current += char
            if len(current) > len(longest):
                longest = current
        else:
            try:
                old_char_index = current.lower().index(char.lower())
                current = current[old_char_index + 1:] + char
            except ValueError:
                current = char

    return longest


class Student:
    """Student class."""

    def __init__(self, name: str, average_grade: float, credit_points: int):
        """Initialize student."""
        self.credit_points = credit_points
        self.average_grade = average_grade
        self.name = name


def create_student(name: str, grades: list, credit_points: int) -> Student:
    """
    Create a new student where average grade is the average of the grades in the list.

    Round the average grade up to three decimal places.
    If the list of grades is empty, the average grade will be 0.
    """
    if len(grades) < 1:
        avg_grade = 0
    else:
        avg_grade = round(sum(grades) / len(grades), 3)

    return Student(name, avg_grade, credit_points)


def get_top_student_with_credit_points(students: list, min_credit_points: int):
    """
    Return the student with the highest average grade who has enough credit points.

    If there are no students with enough credit points, return None.
    If several students have the same average score, return the first.
    """
    good_students = list(filter(lambda x: x.credit_points >= min_credit_points, students))
    if len(good_students) > 0:
        return max(good_students, key=lambda x: x.average_grade)
    else:
        return None


def add_result_to_student(student: Student, grades_count: int, new_grade: int, credit_points) -> Student:
    """
    Update student average grade and credit points by adding a new grade (result).

    As the student object does not have grades count information, it is provided in this function.
    average grade = sum of grades / count of grades

    With the formula above, we can deduct:
    sum of grades = average grade * count of grades

    The student has the average grade, function parameters give the count of grades.
    If the sum of grades is known, a new grade can be added and a new average can be calculated.
    The new average grade must be rounded to three decimal places.
    Given credits points should be added to old credit points.

    Example1:
        current average (from student object) = 4
        grades_count (from parameter) = 2
        so, the sum is 2 * 4 = 8
        new grade (from parameter) = 5
        new average = (8 + 5) / 3 = 4.333
        The student object has to be updated with the new average

    Example2:
        current average = 0
        grades_count = 0
        calculated sum = 0 * 0 = 0
        new grade = 4
        new average = 4 / 1 = 4

    Return the modified student object.
    """
    sum_of_grades = (student.average_grade * grades_count) + new_grade
    new_avg_grade = round(sum_of_grades / (grades_count + 1), 3)
    student.average_grade = new_avg_grade
    student.credit_points += credit_points

    return student


def get_ordered_students(students: list) -> list:
    """
    Return a new sorted list of students by (down).

    credit points (higher first), average_grade (higher first), name (a to z).
    """
    return sorted(students, key=lambda x: (-x.credit_points, -x.average_grade, x.name))


class Room:
    """Room."""

    def __init__(self, number: int, price: int):
        """Initialize room."""
        self.number = number
        self.price = price
        self.booked = False
        self.features = []

    def add_feature(self, feature: str) -> bool:
        """
        Add a feature to the room.

        Do not add the feature and return False if:
        - the room already has that feature
        - the room is booked.
        Otherwise, add the feature to the room and return True
        """
        if feature in self.features or self.booked:
            return False
        else:
            self.features.append(feature)
            return True

    def get_features(self) -> list:
        """Return all the features of the room."""
        return self.features

    def get_price(self) -> int:
        """Return the price."""
        return self.price

    def get_number(self) -> int:
        """Return the room number."""
        return self.number


class Hotel:
    """Hotel."""

    def __init__(self):
        """Initialize hotel."""
        self.rooms = []
        self.available_rooms = []
        self.booked_rooms = []
        for room in self.rooms:
            if not room.booked:
                self.available_rooms.append(room)
            else:
                self.booked_rooms.append(room)

    def add_room(self, room: Room) -> bool:
        """
        Add room to hotel.

        If a room with the given number already exists, do not add a room and return False.
        Otherwise add the room to hotel and return True.
        """
        for hotel_room in self.rooms:
            if room.number == hotel_room.number:
                return False

        self.rooms.append(room)
        self.available_rooms.append(room)
        return True

    def book_room(self, required_features: list) -> Optional[Room]:
        """
        Book an available room which has the most matching features.

        Find a room which has most of the required features.
        If there are several with the same amount of matching features, return the one with the smallest room number.
        If there is no available rooms, return None
        """
        current_room = None
        features_in_current_room = 0
        for hotel_room in self.available_rooms:
            features_in_hotel_room = sum(1 for feature in hotel_room.features if feature in required_features)
            if not current_room:
                current_room = hotel_room
                features_in_current_room = features_in_hotel_room
            else:
                if features_in_hotel_room > features_in_current_room:
                    current_room = hotel_room
                    features_in_current_room = features_in_hotel_room
                elif features_in_hotel_room == features_in_current_room:
                    if current_room.number > hotel_room.number:
                        current_room = hotel_room
                        features_in_current_room = features_in_hotel_room

        if current_room:
            self.booked_rooms.append(current_room)
            return current_room

        return None

    def get_available_rooms(self) -> list:
        """Return a list of available (not booked) rooms."""
        return self.available_rooms

    def get_rooms(self) -> list:
        """Return all the rooms (both booked and available)."""
        return self.rooms

    def get_booked_rooms(self) -> list:
        """Return all the booked rooms."""
        return self.booked_rooms

    def get_feature_profits(self) -> dict:
        """
        Return a dict where key is a feature and value is the total price for the booked rooms which have the feature.

        Example:
            room1, price=100, features=a, b, c
            room2, price=200, features=b, c, d
            room3, price=400, features=a, c

        all the rooms are booked
        result:
        {
        'a': 500,
        'b': 300,
        'c': 700,
        'd': 200
        }
        """
        profits = {}
        for room in self.rooms:
            for feature in room.features:
                if feature not in profits:
                    profits[feature] = room.price
                else:
                    profits[feature] += room.price

        return profits

    def get_most_profitable_feature(self) -> Optional[str]:
        """
        Return the feature which profits the most.

        Use get_feature_profits() method to get the total price for every feature.
        Return the feature which has the highest value (profit).
        If there are several with the same max value, return the feature which is alphabetically lower (a < z)
        If there are no features booked, return None.
        """
        profits = self.get_feature_profits()
        best = max(profits, key=profits.get)
        if best:
            if len(best) < 2:
                return best
            else:
                return min(best, key=best[0])

        return None


if __name__ == '__main__':
    print()
    """
    hotel = Hotel()
    room1 = Room(1, 100)
    room1.add_feature("tv")
    room1.add_feature("bed")
    room2 = Room(2, 200)
    room2.add_feature("tv")
    room2.add_feature("sauna")
    hotel.add_room(room1)
    hotel.add_room(room2)
    # TODO: try to add room with existing number, try to add existing feature to room
    assert hotel.get_rooms() == [room1, room2]
    assert hotel.get_booked_rooms() == []

    assert hotel.book_room(["tv", "president"]) == room1
    assert hotel.get_available_rooms() == [room2]
    assert hotel.get_booked_rooms() == [room1]

    assert hotel.book_room([]) == room2
    assert hotel.get_available_rooms() == []

    assert hotel.get_feature_profits() == {
        'tv': 300,
        'bed': 100,
        'sauna': 200
    }
    assert hotel.get_most_profitable_feature() == 'tv'

    # TODO: try to add a room so that two or more features have the same profit
    """
