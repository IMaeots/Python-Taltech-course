"""File handling."""

import csv
import os
from datetime import datetime


def assign_data_types(lines, data_types):
    """Assign correct data types."""
    for line in lines:
        for key, value in line.items():
            if key not in data_types:
                data_types[key] = infer_data_type(value)
            else:
                if data_types[key] != str:
                    if value == "-":
                        break
                    try:
                        datetime.strptime(value, "%d.%m.%Y").date()
                        data_types[key] = datetime
                    except ValueError:
                        try:
                            int(value)
                            data_types[key] = int
                        except ValueError:
                            data_types[key] = str

    return data_types


def infer_data_type(value):
    """Infer data type based on value."""
    if value == "-":
        return None
    else:
        try:
            value = int(value)
            return int
        except ValueError:
            try:
                datetime.strptime(value, "%d.%m.%Y").date()
                return datetime
            except ValueError:
                return str


def assign_values(lines, data_types, processed_fields):
    """Assign values to the processed field list by using data_types dict."""
    for line in lines:
        processed_row = {}

        for key, value in line.items():
            processed_row[key] = convert_value(value, data_types, key)

        processed_fields.append(processed_row)

    return processed_fields


def convert_value(value, data_types, key):
    """Convert value to the specified data type."""
    if value == '-' or value is None:
        return None
    else:
        if data_types[key] == str:
            return str(value)
        elif data_types[key] == int:
            try:
                return int(value)
            except ValueError:
                data_types[key] = str
                return str(value)
        elif data_types[key] == datetime:
            try:
                return datetime.strptime(value, "%d.%m.%Y").date()
            except ValueError:
                data_types[key] = str
                return str(value)
        else:
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
        lines = list(csv_reader)

        processed_fields = []
        data_types = {}

        data_types = assign_data_types(lines, data_types)  # Assign data types.

        return assign_values(lines, data_types, processed_fields)  # Assign value and return processed fields.


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
            for line in csv_reader:
                person_id = int(line['id'])

                if person_id not in outcome:
                    outcome[person_id] = {"id": int(person_id)}

                for key, the_value in line.items():
                    if the_value == '-':
                        value = None
                    else:
                        try:
                            value = datetime.strptime(the_value, "%d.%m.%Y").date()
                        except ValueError:
                            try:
                                value = int(the_value)
                            except ValueError:
                                value = str(the_value)

                    outcome[person_id][key] = value

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
    """
    # Read data from CSV files
    data = read_people_data(person_data_directory)

    if not data:
        return

    # Calculate age, add "status" and "age" fields, and sort the data
    processed_data = []
    for person in data.values():
        # Calculate age based on birth and death dates
        try:
            birthdate = person['birth']
            deathdate = person['death']
        except KeyError:
            return
        if birthdate is None:
            age = -1
        else:
            birthdate_datetime = datetime.combine(birthdate, datetime.min.time())
            if deathdate is not None:
                deathdate_datetime = datetime.combine(deathdate, datetime.min.time())
                age = (deathdate_datetime - birthdate_datetime).days // 365
            else:
                age = (datetime.now() - birthdate_datetime).days // 365

        # Add "status" and "age" fields
        person["status"] = "alive" if deathdate is None else "dead"
        person["age"] = age

        processed_data.append(person)

    # Sort the data based on specified criteria
    processed_data.sort(key=lambda x: (x["age"], x["birth"], x.get("name", ""), x["id"]))

    # Write the sorted data to a new CSV file
    with open(report_filename, 'w', newline='') as report_file:
        fieldnames = list(data[0].keys()) + ["status", "age"]
        csv_writer = csv.DictWriter(report_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(processed_data)
    """


result = read_csv_file_into_list_of_dicts_using_datatypes("test.csv")

# Print the result for verification
for row in result:
    print(row)

print(read_people_data("data"))
