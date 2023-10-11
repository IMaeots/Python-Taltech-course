"""Air traffic planning."""


def update_delayed_flight(schedule: dict[str, tuple[str, str]], delayed_flight_number: str, new_departure_time: str) -> \
dict[str, tuple[str, str]]:
    """
    Update the departure time of a delayed flight in the flight schedule.

    Return a dictionary where the time of the specified flight is modified.
    This means that the result dictionary should not contain the old time,
    instead a new departure time points to the specified flight.
    The input schedule cannot be changed.

    :param schedule: Dictionary of flights ({time string: (destination, flight number)})
    :param delayed_flight_number: Flight number of the delayed flight
    :param new_departure_time: New departure time for the delayed flight
    :return: Updated flight schedule with the delayed flight's departure time changed
    """
    updated_schedule = {}
    for key, values in schedule.items():
        if values[1] == delayed_flight_number:
            updated_schedule[new_departure_time] = (values[0], delayed_flight_number)
        else:
            updated_schedule[key] = values

    return updated_schedule


def cancel_flight(schedule: dict[str, tuple[str, str]], cancelled_flight_number: str) -> dict[str, tuple[str, str]]:
    """
    Create a new schedule where the specified flight is cancelled.

    The function cannot modify the existing schedule parameter.
    Instead, create a new dictionary where the cancelled flight is not added.

    :param schedule: Dictionary of flights ({time: (destination, flight number)})
    :param cancelled_flight_number: Flight number of the cancelled flight
    :return: New flight schedule with the cancelled flight removed
    """
    updated_schedule = {}
    for key, values in schedule.items():
        if values[1] == cancelled_flight_number:
            continue
        else:
            updated_schedule[key] = values

    return updated_schedule



def busiest_time(schedule: dict[str, tuple[str, str]]) -> list[str]:
    """
    Find the busiest hour(s) at the airport based on the flight schedule.

    Finds the busiest hour(s) at the airport based on the flight schedule. The busiest hour(s)
    is/are determined by counting the number of flights departing in each hour of the day.
    All flights departing with the same hour in their departure time, are counted into the same hour.

    The function returns a list of strings of the busiest hours, sorted in ascending order, such as ["08", "21"].

    :param schedule: Dictionary containing the flight schedule, where keys are departure times
                     in the format "HH:mm" and values are tuples containing destination and flight number.
    :return: List of strings representing the busiest hour(s) in 24-hour format, such as ["08", "21"].
    """
    time_dict = {}

    for time in schedule:
        hour = time.strip().split(":")[0]
        if hour in time_dict:
            time_dict[hour] += 1
        else:
            time_dict[hour] = 1

    max_busy_value = max(time_dict.values())

    busiest_hours = [time for time, count in time_dict.items() if count == max_busy_value]

    return sorted(busiest_hours)


def convert_time_to_minutes(time_string: str) -> int:
    """Helper function: Convert a string in format HH:mm to time in minutes."""
    time = time_string.strip().split(":")
    return int(time[0]) * 60 + int(time[1])


def connecting_flights(schedule: dict[str, tuple[str, str]], arrival: tuple[str, str]) -> list[tuple[str, str]]:
    """
    Find connecting flights based on the provided arrival information and flight schedule.

    The function takes a flight schedule and the arrival time and location of a flight,
    and returns a list of available connecting flights. A connecting flight is considered
    available if its departure time is at least 45 minutes after the arrival time, but less
    than 4 hours after the arrival time. Additionally, a connecting flight must not go back
    to the same place the arriving flight came from.

    :param schedule: Dictionary containing the flight schedule, where keys are departure
                     times in the format "HH:mm" and values are tuples containing
                     destination and flight number. For example:
                     {
                         "14:00": ("Paris", "FL123"),
                         "15:00": ("Berlin", "FL456")
                     }

    :param arrival: Tuple containing the arrival time and the location the flight is
                    arriving from. For example:
                    ("11:05", "Tallinn")

    :return: A list of tuples containing the departure time and destination of the
             available connecting flights, sorted by departure time. For example:
             [
                 ("14:00", "Paris"),
                 ("15:00", "Berlin")
             ]
             If no connecting flights are available, the function returns an empty list.
    """
    arrival_time_in_minutes = convert_time_to_minutes(arrival[0])
    available_flights = []

    for key, value in schedule.items():
        time_in_minutes = convert_time_to_minutes(key)

        if ((arrival_time_in_minutes + 45) <= time_in_minutes < (arrival_time_in_minutes + 240)
                and value[0] != arrival[1]):
            data = (key, value[0])
            available_flights.append(data)

    if len(available_flights) < 1:
        return []
    else:
        available_flights.sort(key=lambda x: x[0])
        return available_flights


def busiest_hour(schedule: dict[str, tuple[str, str]]) -> list[str]:
    """
    Find the busiest hour-long slot(s) in the schedule.

    One hour slot duration is 60 minutes (or the diff of two times is less than 60).
    So, 15:00 and 16:00 are not in the same slot.

    :param schedule: Dictionary containing the flight schedule, where keys are departure
                     times in the format "HH:mm" and values are tuples containing
                     destination and flight number. For example:
                     {
                         "14:00": ("Paris", "FL123"),
                         "15:00": ("Berlin", "FL456")
                     }

    :return: A list of strings representing the starting time(s) of the busiest hour-long
             slot(s) in ascending order. For example:
             ["08:00", "15:20"]
             If the schedule is empty, returns an empty list.
    """
    hour_slot_count = {}

    for time in schedule:
        time_in_minutes = convert_time_to_minutes(time)
        hour_slot_start = (time_in_minutes // 60) * 60

        if hour_slot_start not in hour_slot_count:
            hour_slot_count[hour_slot_start] = 0
        hour_slot_count[hour_slot_start] += 1

    max_count = max(hour_slot_count.values(), default=0)

    busiest_slots = [hour for hour, count in hour_slot_count.items() if count == max_count]
    busiest_slots.sort()
    busiest_slots_formatted = [f"{hour // 60:02d}:{hour % 60:02d}" for hour in busiest_slots]

    return busiest_slots_formatted


def create_destination_popularity_dictionary(schedule: dict[str, tuple[str, str]], passenger_count: dict[str, int]) -> dict:
    """Helper function: Return dictionary of destinations based on popularity."""
    destination_dict = {}

    for destinations in schedule.values():
        destination = destinations[0]
        destination_number = destinations[1]

        for flight_number, count in passenger_count.items():
            if destination_number == flight_number:
                if destination in destination_dict:
                    destination_dict[destination] += count
                else:
                    destination_dict[destination] = count

    return destination_dict


def most_popular_destination(schedule: dict[str, tuple[str, str]], passenger_count: dict[str, int]) -> str:
    """
    Find the destination where the most passengers are going.

    :param schedule: A dictionary representing the flight schedule.
                     The keys are departure times and the values are tuples
                     containing destination and flight number.
    :param passenger_count: A dictionary with flight numbers as keys and
                            the number of passengers as values.
    :return: A string representing the most popular destination.
    """
    destination_dict = create_destination_popularity_dictionary(schedule, passenger_count)

    return max(destination_dict, key=destination_dict.get)

def least_popular_destination(schedule: dict[str, tuple[str, str]], passenger_count: dict[str, int]) -> str:
    """
    Find the destination where the fewest passengers are going.

    :param schedule: A dictionary representing the flight schedule.
                     The keys are departure times and the values are tuples
                     containing destination and flight number.
    :param passenger_count: A dictionary with flight numbers as keys and
                            the number of passengers as values.
    :return: A string representing the least popular destination.
    """
    destination_dict = create_destination_popularity_dictionary(schedule, passenger_count)

    return min(destination_dict, key=destination_dict.get)


if __name__ == '__main__':
    schedule = {
        "06:15": ("Tallinn", "OWL6754"),
        "11:35": ("Helsinki", "BHM2345")
    }
    new_schedule = update_delayed_flight(schedule, "OWL6754", "09:00")
    print(schedule)
    # {'06:15': ('Tallinn', 'OWL6754'), '11:35': ('Helsinki', 'BHM2345')}
    print(new_schedule)
    # {'09:00': ('Tallinn', 'OWL6754'), '11:35': ('Helsinki', 'BHM2345')}

    new_schedule = cancel_flight(schedule, "OWL6754")
    print(schedule)
    # {'06:15': ('Tallinn', 'OWL6754'), '11:35': ('Helsinki', 'BHM2345')}
    print(new_schedule)
    # {'11:35': ('Helsinki', 'BHM2345')}

    schedule = {
        "04:35": ("Maardu", "MWL6754"),
        "06:15": ("Tallinn", "OWL6754"),
        "06:30": ("Paris", "OWL6751"),
        "07:29": ("London", "OWL6756"),
        "08:00": ("New York", "OWL6759"),
        "11:30": ("Tokyo", "OWL6752"),
        "11:35": ("Helsinki", "BHM2345"),
        "19:35": ("Paris", "BHM2346"),
        "20:35": ("Helsinki", "BHM2347"),
        "22:35": ("Tallinn", "TLN1001"),
    }
    print(busiest_time(schedule))
    # ['06', '11']

    print(connecting_flights(schedule, ("04:00", "Tallinn")))
    # [('06:30', 'Paris'), ('07:29', 'London')]

    print(busiest_hour(schedule))
    # ['06:15', '06:30', '07:29', '11:30']
    # 19:35 does not match because 20:35 is not in the same slot

    # flight number: number of passengers
    passengers = {
        "MWL6754": 100,
        "OWL6754": 85,
        "OWL6751": 103,
        "OWL6756": 87,
        "OWL6759": 118,
        "OWL6752": 90,
        "BHM2345": 111,
        "BHM2346": 102,
        "BHM2347": 94,
        "TLN1001": 1
    }
    print(most_popular_destination(schedule, passengers))
    # Paris

    print(least_popular_destination(schedule, passengers))
    # Tallinn
