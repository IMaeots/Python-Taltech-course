"""Create table from the given string."""
import re


def format_table(formatted_times, usernames, errors, addresses, endpoints):
    """Format the table."""
    # Create a dictionary to map column names to their data
    data_dict = {
        "time": formatted_times,
        "user": usernames,
        "error": errors,
        "ipv4": addresses,
        "endpoint": endpoints,
    }

    # Determine the maximum width among columns with data
    if endpoints:
        width = 9
    elif errors:
        width = 6
    else:
        width = 5

    table = []
    for col in data_dict:
        if data_dict[col]:
            table.append(f"{col:<{width}}| {', '.join(map(str, data_dict[col]))}")

    return '\n'.join(table)


def sort_and_format_times(times: list[tuple[int, int, int]]) -> list:
    """Sort and format times to correct format."""

    def custom_sort(item):
        """Define custom sort method."""
        hours, minutes, offsets = item
        h = (hours - offsets) % 24
        if h < 0:
            h = 24 + h

        return h * 60 + minutes

    sorted_times = sorted(times, key=custom_sort)
    formatted_times = []
    for hour, minute, offset in sorted_times:
        real_hour = (hour - offset) % 24
        adjusted_hour = (24 + real_hour) % 12 if real_hour < 0 else real_hour % 12
        period = 'AM' if real_hour < 12 else 'PM'
        formatted_time = f"{adjusted_hour if adjusted_hour != 0 else 12}:{minute:02} {period}"
        if formatted_time not in formatted_times:
            formatted_times.append(formatted_time)

    return formatted_times


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
    times = get_times(text)
    usernames = get_usernames(text)
    errors = get_errors(text)
    addresses = get_addresses(text)
    endpoints = get_endpoints(text)

    sorted_and_formatted_times = sort_and_format_times(times)

    # Create the table string
    return format_table(sorted_and_formatted_times, sorted(usernames),
                        sorted(errors), sorted(addresses), sorted(endpoints))


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
    pattern = r'\[(\d{1,2}[^0-9]\d{1,2})\sUTC([+-]{0,1}\d{1,2})'
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
    matches = re.finditer(pattern, text)

    usernames = []
    for match in matches:
        if match.group(1) not in usernames:
            usernames.append(match.group(1))

    return usernames


def get_errors(text: str) -> list[int]:
    """Get errors from text."""
    pattern = r'error (\d{1,3}(?!\d))'
    matches = re.finditer(pattern, text, re.IGNORECASE)

    unique_list = []
    for match in matches:
        if int(match.group(1)) not in unique_list:
            unique_list.append(int(match.group(1)))

    return unique_list


def get_addresses(text: str) -> list[str]:
    """Get IPv4 addresses from text."""
    pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    matches = re.finditer(pattern, text)

    unique_list = []
    for match in matches:
        if match.group() not in unique_list:
            unique_list.append(match.group())

    return unique_list


def get_endpoints(text: str) -> list[str]:
    """Get endpoints from text."""
    pattern = r'(/[\w&/=?\-_%]+)'
    matches = re.finditer(pattern, text)

    unique_list = []
    for match in matches:
        if match.group() not in unique_list:
            unique_list.append(match.group())

    return unique_list


if __name__ == '__main__':
    logs = """
            [14?36 UTC+9] /tere eRRoR 418 192.168.0.255
            [8B48 UTC-6] usr:kasutaja
            """
    print(create_table_string(logs))
    print()
    # time     | 5:36 AM, 2:48 PM
    # user     | kasutaja
    # error    | 418
    # ipv4     | 192.168.0.255
    # endpoint | /tere

    logs1 = """
                [24?36 UTC+9] /tere3 eRRoR 418 192.168.0.255
                [13B48 UTC0] usr:ja_jaJa
                """
    print(create_table_string(logs1))
    print()

    logs2 = """
                [14?36 UTC+9] /tere eRRoR 418 192.168.0.255
                [13B8 UTC+1] usr:kasutaja
                """
    print(create_table_string(logs2))
    print()

    logs3 = """
                [12?05 UTC0] /tere eRRoR 41 eRROR 23 error 22 error 1000 192.168.0.255
                [12B4 UTC-6] usr:kasutaja
                """
    print(create_table_string(logs3))
    print()

    logs4 = """
    [-1b35 UTC-4] errOR 741
    [24a48 UTC+0] 776.330.579.818
    [02:53 UTC+5] usr:96NC9yqb /aA?Y4pK
    [5b05 UTC+5] ERrOr 700 268.495.856.225
    [24-09 UTC+10] usr:uJV5sf82_ eRrOR 844 715.545.485.989
    [04=54 UTC+3] eRROR 452
    [11=57 UTC-6] 15.822.272.473 error 9
    [15=53 UTC+7] /NBYFaC0 468.793.214.681
    [23-7 UTC+12] /1slr8I
    [07.46 UTC+4] usr:B3HIyLm 119.892.677.533
    [0:60 UTC+0] bad
    [0?0 UTC+0] ok
    [0.0 UTC+0] also ok
    [0.0 UTC+0] eRROR 452
    [0.0 UTC+0] eRROR 452
    [0.0 UTC+0] eRROR 452
    """
    print(create_table_string(logs4))
    # time     | 12:00 AM, 12:05 AM, 1:54 AM, 3:46 AM, 8:53 AM, 11:07 AM, 5:57 PM, 9:53 PM
    # user     | 96NC9yqb, B3HIyLm, uJV5sf82_
    # error    | 9, 452, 700, 741, 844
    # ipv4     | 119.892.677.533, 15.822.272.473, 268.495.856.225, 468.793.214.681, 715.545.485.989, 776.330.579.818
    # endpoint | /1slr8I, /NBYFaC0, /aA?Y4pK
    print()
    print(create_table_string("[0.0 UTC+0]"))
    print()
    print(create_table_string(" usr:B3HIyLm usr:uJV5sf82_ "))
    print()
    print(create_table_string(" 634.865.217.415 959.675.203.100 "))
    print()
    print(create_table_string("/aA?Y4pK //aA?Y4pK"))
    print()
    print(create_table_string("/zYZ_n-NMj"))
