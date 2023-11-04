"""File handling."""

import csv
import os
from datetime import datetime


def cast_value(value, data_type):
    """Cast value to the appropriate data type based on the column's data_type."""
    if value == "-":
        return None
    if data_type == int:
        return int(value)
    if data_type == datetime:
        return datetime.strptime(value, "%d.%m.%Y").date()
    return str(value)


def read_csv_file_into_list_of_dicts_using_datatypes(filename: str) -> list[dict]:
    """
    Read data from a CSV file and cast values into different data types based on their content.

    Fields containing only numbers are cast into integers.
    Fields containing dates (in the format dd.mm.yyyy) are cast into date.
    Otherwise, the data type remains string (default by csv reader).
    The order of elements in the list matches the lines in the file.
    None values don't affect the data type (the column will have the type based on the existing values).

    Hint: For date parsing, you can use the strptime method. See examples here:
    https://docs.python.org/3/library/datetime.html#examples-of-usage-date

    If a field contains only numbers, it's cast to int:
    name,age
    john,11
    mary,14

    Will become ('age' is int):
    [
      {'name': 'john', 'age': 11},
      {'name': 'mary', 'age': 14}
    ]

    If a field contains text or mixed content, it remains as a string:
    name,age
    john,11
    mary,14
    ago,unknown

    Will become ('age' cannot be cast to int because of "ago"):
    [
      {'name': 'john', 'age': '11'},
      {'name': 'mary', 'age': '14'},
      {'name': 'ago', 'age': 'unknown'}
    ]

    If a field contains only dates, it's cast to date:
    name,date
    john,01.01.2022
    mary,07.09.2023

    Will become:
    [
      {'name': 'john', 'date': datetime.date(2022, 1, 1)},
      {'name': 'mary', 'date': datetime.date(2023, 9, 7)},
    ]

    Example:
    name,date
    john,01.01.2022
    mary,late 2023

    Will become:
    [
      {'name': 'john', 'date': "01.01.2022"},
      {'name': 'mary', 'date': "late 2023"},
    ]

    A missing value "-" is interpreted as None (data type is not affected):
    name,date
    john,-
    mary,07.09.2023

    Will become:
    [
      {'name': 'john', 'date': None},
      {'name': 'mary', 'date': datetime.date(2023, 9, 7)},
    ]

    :param filename: The name of the CSV file to read.
    :return: A list of dictionaries containing processed field values.
    """
    with open(filename, 'r', newline='') as f:
        csv_reader = csv.DictReader(f)
        data_types = {}

        # Determine data types for each column based on all values in the file.
        for line in csv_reader:
            for key, value in line.items():
                if key not in data_types:
                    if key == 'id':
                        data_types[key] = int
                    if value.isdigit():
                        data_types[key] = int
                    else:
                        try:
                            datetime.strptime(value, "%d.%m.%Y")
                            data_types[key] = datetime
                        except ValueError:
                            data_types[key] = str
                else:
                    if data_types[key] != str:
                        try:
                            datetime.strptime(value, "%d.%m.%Y")
                            data_types[key] = datetime
                        except ValueError:
                            if value is not None:
                                if value.isdigit():
                                    data_types[key] = int
                                else:
                                    data_types[key] = str

        f.seek(0)
        csv_reader = csv.DictReader(f)

        processed_fields = []
        for line in csv_reader:
            processed_row = {key: cast_value(value, data_types[key]) for key, value in line.items()}
            processed_fields.append(processed_row)

    return processed_fields


def read_people_data(directory: str) -> dict[int, dict]:
    """
    Read people data from CSV files and merge information.

    This function reads CSV files located inside the specified directory, and all *.csv files are read.
    Each file is expected to have an integer field "id" which is used to merge information.
    The result is a single dictionary where the keys are "id" and the values are
    dictionaries containing all the different values across the files.
    Missing keys are included in every dictionary with None as the value.

    File: a.csv
    id,name
    1,john
    2,mary
    3,john

    File: births.csv
    id,birth
    1,01.01.2001
    2,05.06.1990

    File: deaths.csv
    id,death
    2,01.02.2022
    1,-

    Will become:
    {
        1: {"id": 1, "name": "john", "birth": datetime.date(2001, 1, 1), "death": None},
        2: {"id": 2, "name": "mary", "birth": datetime.date(1990, 6, 5),
            "death": datetime.date(2022, 2, 1)},
        3: {"id": 3, "name": "john", "birth": None, "death": None},
    }

    :param directory: The directory containing CSV files.
    :return: A dictionary with "id" as keys and data dictionaries as values.
    """
    outcome = {}

    csv_files = [file for file in os.listdir(directory) if file.endswith(".csv")]

    for csv_file in csv_files:
        file_path = os.path.join(directory, csv_file)

        with open(file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                person_id = int(row['id'])

                if person_id not in outcome:
                    outcome[person_id] = {"id": person_id}

                for key, the_value in row.items():
                    outcome[person_id][key] = the_value

    return outcome


def generate_people_report(person_data_directory: str, report_filename: str) -> None:
    """
    Generate a report about people data from CSV files.

    Note: Use the read_people_data() function to read the data from CSV files.

    Input files should contain fields "birth" and "death," which are dates in the format "dd.mm.yyyy".
    There are no duplicate headers in the files except for the "id" field.

    The report is a CSV file that includes all fields from the input data along with two fields:
    - "status": Either "dead" or "alive" based on the presence of a death date;
    - "age": The current age or the age of death, calculated in full years.
      If there is no birthdate, the age is set to -1.

    Example:
    - Birth 01.01.1940, death 01.01.2022 => age: 80
    - Birth 02.01.1940, death 01.01.2022 => age: 79

    Hint: You can compare dates directly when calculating age.

    The lines in the report are ordered based on the following criteria:
    - Age ascending (younger before older); lines with incalculable age come last;
    - If the age is the same, birthdate descending (newer birth before older birth);
    - If both the age and birthdate are the same, sorted by name ascending (a before b);
      If a name is not available, use "" (people with missing names should come before people with name);
    - If names are the same or the name field is missing, ordered by id ascending.

    :param person_data_directory: The directory containing CSV files.
    :param report_filename: The name of the file to write to.
    :return: None
    """


result = read_csv_file_into_list_of_dicts_using_datatypes("test.csv")

# Print the result for verification
for row in result:
    print(row)

print(read_people_data("data"))
