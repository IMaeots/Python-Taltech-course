"""Create table from the given string."""
import re


def create_table_string(text: str) -> str:
    """
    Create table string from the given logs.

    Example of logs:

    [10:50 UTC+8] nothing here
    [12:25 UTC-2] error 404

    There are a total of five categories you need to find the items for.
    Here are the rules for finding them:

    1. Time
    - Hour can be one or two characters long (1, 01, and 11)
    - Minute can be one or two characters long (2, 02, 22)
    - UTC offset ranges from -12 to 12
    - Times in the text are formatted in 24 hour time format (https://en.wikipedia.org/wiki/24-hour_clock)
    - Minimum time is 00:00 (0:00 and 0,00 and 00-0 are also valid)
    - Maximum time is 23:59
    - Hour and minute can be separated by any non-numeric character (01:11, 1.2, 6;5 and 1a4 are valid while 12345 is not)
    2. Username starts after "usr:" and contains letters, numbers and underscores ("_")
    3. Error code is a non-negative number up to 3 digits and comes after a case-insensitive form of "error "
    4. IPv4 address is good enough if it's a group of four 1- to 3-digit numbers separated by dots
    5. Endpoint starts with a slash ("/") and contains letters, numbers and "&/=?-_%"

    Each table row consists of a category name and items belonging to that category.
    Categories are named and ordered as follows: "time", "user", "error", "ipv4" and "endpoint".

    Table from the above input example:

    time  | 2.50 AM, 14.25 PM
    error | 404

    The category name and its items are separated by a vertical bar ("|").
    The length between the category name and separator is one whitespace (" ") for the longest category name in the table.
    The length between the separator and items is one whitespace.
    Items for each category are unique and are separated by a comma and a whitespace (", ") and must be sorted in ascending order.
    Times in the table are formatted in 12 hour time format (https://en.wikipedia.org/wiki/12-hour_clock), like "1:12 PM"
    and "12:00 AM".
    Times in the table should be displayed in UTC(https://et.wikipedia.org/wiki/UTC) time.
    """
    try:
        times = get_times(text)
        usernames = get_usernames(text)
        errors = get_errors(text)
        addresses = get_addresses(text)
        endpoints = get_endpoints(text)

        # Format times in UTC in 12-hour format
        formatted_times = [f"{hour % 12}:{minute:02} {'AM' if hour < 12 else 'PM'}" for hour, minute, _ in times]

        # Create the table string
        table = [f"time     | {', '.join(formatted_times)}", f"user     | {', '.join(usernames)}",
                 f"error    | {', '.join(map(str, errors))}", f"ipv4     | {', '.join(addresses)}",
                 f"endpoint | {', '.join(endpoints)}"]
    except AssertionError:
        raise AssertionError('\n'.join(times))

    return '\n'.join(table)


def get_times(text: str) -> list[tuple[int, int, int]]:
    """
    Get times from text using the time pattern.

    The result should be a list of tuples containing the time that's not normalized and UTC offset.

    For example:

    [10:53 UTC+3] -> [(10, 53, 3)]
    [1:43 UTC+0] -> [(1, 43, 0)]
    [14A3 UTC-4] [14:3 UTC-4] -> [(14, 3, -4), (14, 3, -4)]

    :param text: text to search for the times
    :return: list of tuples containing the time and offset
    """
    pattern = r'\[(\d{1,2}[^0-9]\d{1,2})\sUTC([+-]\d{1,2})'
    matches = re.findall(pattern, text)
    times = []

    for match in matches:
        time_str, offset_str = match
        hour, minute = [int(part) for part in re.split(r'[^0-9]', time_str)]
        offset = int(offset_str)
        if hour > 23 or minute > 59:
            continue
        else:
            times.append((hour, minute, offset))

    return times


def get_usernames(text: str) -> list[str]:
    """Get usernames from text."""
    pattern = r'usr:(\w+)'
    matches = re.findall(pattern, text)

    return matches


def get_errors(text: str) -> list[int]:
    """Get errors from text."""
    pattern = r'error (\d{1,3})'
    matches = re.findall(pattern, text, re.IGNORECASE)

    return [int(match) for match in matches]


def get_addresses(text: str) -> list[str]:
    """Get IPv4 addresses from text."""
    pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    matches = re.findall(pattern, text)

    return matches


def get_endpoints(text: str) -> list[str]:
    """Get endpoints from text."""
    pattern = r'(/[\w&/=?-_%]+)'
    matches = re.findall(pattern, text)

    return matches


if __name__ == '__main__':
    logs = """
            [14?36 UTC+9] /tere eRRoR 418 192.168.0.255
            [8B48 UTC-6] usr:kasutaja
            """
    print(create_table_string(logs))
    # time     | 5:36 AM, 2:48 PM
    # user     | kasutaja
    # error    | 418
    # ipv4     | 192.168.0.255
    # endpoint | /tere
