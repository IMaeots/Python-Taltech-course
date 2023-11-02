"""File handling."""
import csv


def read_file_contents(filename: str) -> str:
    """
    Read file contents into a string.

    In this exercise, assume that the file exists.

    :param filename: The name of the file to read.
    :return: The contents of the file as a string.
    """
    with open(filename, "r") as f:
        return f.read()


def read_file_contents_to_list(filename: str) -> list[str]:
    r"""
    Read file contents into a list of lines.

    In this exercise, assume that the file exists.

    Each line from the file is a separate element in the list,
    and the order of the list matches the order in the file.
    Newline characters ('\n') are removed from each line.

    :param filename: The name of the file to read.
    :return: A list of lines without newline characters.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip('\n')

        return lines


def read_csv_file(filename: str, delimiter=',') -> list[list[str]]:
    """
    Read CSV file contents into a list of rows.

    Each row is represented as a list of "columns" or fields.

    Example CSV (Comma-separated values) data:
    name,age
    john,12
    mary,14

    Will return as:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Note: The "csv" module should be used.

    :param delimiter: type of delimiter in csv file.
    :param filename: The name of the file to read.
    :return: A list of lists, where each inner list represents a row of CSV data.
    """
    with open(filename, 'r') as f:
        csv_reader = csv.reader(f, delimiter=delimiter)

        output = []
        for item in csv_reader:
            output.append(item)

        return output


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to a file.

    If the file does not exist, it will be created.
    If the file already exists, its contents will be overwritten.

    :param filename: The name of the file to write to.
    :param contents: The content to write to the file.
    :return: None
    """
    with open(filename, "w") as f:
        f.write(contents)


def write_lines_to_file(filename: str, lines: list[str]) -> None:
    """
    Write lines to a file.

    Each string in the 'lines' list represents a separate line in the file.
    The function ensures that there is no extra newline added at the end of the file,
    unless the last element in the 'lines' list itself ends with a newline.

    :param filename: The name of the file to write to.
    :param lines: A list of strings, each representing a line to write to the file.
    :return: None
    """
    with open(filename, "w") as f:
        if not lines:
            f.write("")
        else:
            f.write(lines[0])
            for line in lines[1:]:
                f.write("\n" + line)


def write_csv_file(filename: str, data: list[list[str]]) -> None:
    """
    Write data into a CSV file.

    The data is a list of lists, where each inner list represents a row,
    and the elements within each inner list represent the columns.

    Example data:
    [["name", "age"], ["john", "11"], ["mary", "15"]]

    Will be written in the .csv file as:
    name,age
    john,11
    mary,15

    Note: The "csv" module should be used.

    :param filename: The name of the file to write to.
    :param data: A list of lists to write to the file, where each list represents a row.
    :return: None
    """
    with open(filename, "w") as f:
        csv_writer = csv.writer(f, delimiter=',')
        csv_writer.writerows(data)


def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    """
    Merge information from two input CSV files into one output CSV file.

    The dates file contains names and dates separated by a colon, and the towns file contains
    names and towns separated by a colon. Both files have no headers.

    Example format of the dates file:
    john:01.01.2001
    mary:06.03.2016

    Example format of the towns file:
    john:london
    mary:new york

    The merging is performed based on the names found in input files.
    The order of the lines in the output file follows the order in the dates input file.
    Names that are missing in the dates input file will follow the order in the towns input file.
    The order of the fields is: name, town, date.

    The resulting CSV file should have the following format:
    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be represented as "-" in the output file.

    Example:
    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Reuse CSV reading and writing functions.
    Note: When reading CSV files, specify the delimiter (improve existing method).

    :param dates_filename: The name of the CSV file with names and dates (name:date).
    :param towns_filename: The name of the CSV file with names and towns (name:town).
    :param csv_output_filename: The name of the CSV file to write to names, towns, and dates.
    :return: None
    """

    class Person:
        def __init__(self, name, date, town):
            self.name = name
            self.date = date
            self.town = town

    dates = read_csv_file(dates_filename, delimiter=':')
    towns = read_csv_file(towns_filename, delimiter=':')
    my_dict = {}

    for date in dates:
        my_dict[date[0]] = Person(date[0], date[1], "-")

    for town in towns:
        if town[0] in my_dict:
            my_dict[town[0]].town = town[1]
        else:
            my_dict[town[0]] = Person(town[0], "-", town[1])

    output_list = [["name", "town", "date\n"]]
    for key, value in my_dict.items():
        output_list.append([value.name, value.town, value.date])

    write_csv_file(csv_output_filename, output_list)


def read_csv_file_into_list_of_dicts(filename: str) -> list[dict[str, str]]:
    """
    Read a CSV file into a list of dictionaries.

    The header line of the CSV file will be used as keys for the dictionaries.
    If there are only headers or no rows in the CSV file, the result is an empty list.
    Each line after the header line will result in a dictionary inside the result list.
    Every line should contain the same number of fields.
    The order of the elements in the list corresponds to the lines in the file
    (the first line becomes the first element, and so on).

    Given a CSV file like this:
    name,age,sex
    John,12,M
    Mary,13,F

    The result will be:
    [
      {"name": "John", "age": "12", "sex": "M"},
      {"name": "Mary", "age": "13", "sex": "F"},
    ]

    :param filename: The name of the CSV file to read.
    :return: A list of dictionaries where keys are taken from the header and values are strings.
    """
    pass


def write_list_of_dicts_to_csv_file(filename: str, data: list[dict]) -> None:
    """
    Write a list of dictionaries to a CSV file.

    Each dictionary in the 'data' list represents a row in the CSV file,
    with dictionary keys representing the fields of a header.
    Fields missing in certain rows will be empty in these rows.
    The order of rows in the file matches the order of elements in the list.

    Example data:
    [
      {"name": "john", "age": "12"},
      {"name": "mary", "town": "London"}
    ]

    This data will be written to the CSV file as:
    name,age,town
    john,12,
    mary,,London

    :param filename: The name of the file to write to.
    :param data: List of dictionaries to write to the file.
    :return: None
    """
    pass
