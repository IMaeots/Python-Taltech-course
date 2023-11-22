"""XP - decorators."""
import inspect
import time


def double(func):
    """
    Double the return value of a function.

    :param func: The decorated function.
    :return: Inner function.
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2

    return wrapper


def stopwatch(func):
    """
    Print the runtime of a function.

    It should be printed out like: "It took [time] seconds for [function_name] to run",
    where [time] is the number of seconds (with the precision of at least 5 decimal places)
    it took for the function to run and [function_name] is the name of the function.
    The function's return value should not be affected.
    :param func: The decorated function.
    :return: Inner function.
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        elapsed_time = end_time - start_time

        print(f"It took {elapsed_time:.5f} seconds for {func.__name__} to run")
        return result

    return wrapper


def memoize(func):
    """
    Cache the return value of a function.

    Memoization is an optimisation technique used primarily to speed up computer programs
    by storing the results of expensive function calls and returning the cached result
    when the same inputs occur again.
    For efficiency purposes, you can assume, that the function only takes one argument,
    and that the argument is an integer.
    :param func: The decorated function.
    :return: Inner function.
    """
    cache = {}

    def wrapper(arg):
        if arg in cache:
            return cache[arg]
        else:
            value = func(arg)
            cache[arg] = value
            return value

    return wrapper


def read_data(func):
    """
    Read the data from the file "data.txt" and pass it to the function.

    The data must be passed as a list of strings, where each string is a line from the file.
    It also must be passed as the first argument to the function, followed by any other given arguments.
    :param func: The decorated function.
    :return: Inner function.
    """

    def wrapper(*args, **kwargs):
        with open('data.txt', 'r') as file:
            data = [line.rstrip('\n') for line in file.readlines()]
            return func(data, *args, **kwargs)

    return wrapper


def catch(*error_classes):
    """
    Catch the specified exceptions.

    If the function raises one of the specified exceptions, return a tuple of (1, exception_class),
    where exception_class is the type of the exception that was raised. Otherwise, return a tuple of (0, result),
    where result is the result of the function.

    This decorator must be able to handle the following cases:
    1. The decorator is used with no arguments, e.g. @catch. Such usage should catch all exceptions.
    2. The decorator is used with one argument, e.g. @catch(ValueError).
    3. The decorator is used with multiple arguments, e.g. @catch(KeyError, TypeError).
    :param error_classes: The exceptions to catch.
    :return: Inner function.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return 0, result  # Return a tuple indicating success (0) and the result.
            except Exception as e:
                if not error_classes or any(isinstance(e, error_class) for error_class in error_classes):
                    return 1, type(e)  # Return a tuple indicating failure (1) and the exception class.
                else:
                    raise  # Re-raise the exception if it doesn't match the specified error classes.

        return wrapper

    return decorator


def enforce_types(func):
    """
    Enforce the types of the function's parameters and return value.

    If the function is called with an argument of the wrong type, raise a TypeError with the message:
    "Argument '[argument_name]' must be of type [expected_type], but was [value] of type [actual_type]".
    If the function returns a value of the wrong type, raise a TypeError with the message:
    "Returned value must be of type [expected_type], but was [value] of type [actual_type]".
    Values should be represented as strings using the repr() function.

    If an argument or the return value can be of multiple types, then the [expected_type]
    in the error message should be "[type_1], [type_2], ..., [type_(n-1)] or [type_n]".
    For example if the type annotation for an argument is int | float | str | bool, then the error message should be
    "Argument '[argument_name]' must be of type int, float, str or bool, but was [value] of type [actual_type]".

    If there's no type annotation for a parameter or the return value, then it can be of any type.

    Using the inspect module to get the function's signature and annotations is recommended.

    Exceptions, that happen during the execution of the function, should still occur normally,
    if the argument types are correct.
    :param func: The decorated function.
    :return: Inner function.
    """
    signature = inspect.signature(func)
    parameters = signature.parameters
    return_annotation = signature.return_annotation

    def wrapper(*args, **kwargs):
        # Validate arguments based on their annotations in parameters.
        bound_arguments = signature.bind(*args, **kwargs)
        bound_arguments.apply_defaults()

        for param_name, param_value in bound_arguments.arguments.items():
            param_annotation = parameters[param_name].annotation
            if param_annotation != inspect.Parameter.empty and not isinstance(param_value, param_annotation):
                raise TypeError(f"Argument '{param_name}' must be of type {param_annotation.__name__}, "
                                f"but was {param_value!r} of type {type(param_value).__name__}")

        # Execute the function.
        result = func(*args, **kwargs)

        # Validate the return value based on the return_annotation.
        if return_annotation != inspect.Signature.empty and not isinstance(result, return_annotation):
            raise TypeError(f"Returned value must be of type {return_annotation.__name__}, "
                            f"but was {result!r} of type {type(result).__name__}")

        return result

    return wrapper


#  Everything below is just for testing purposes, tester does not care what you do with them.
#    |           |           |           |           |           |           |           |
#    V           V           V           V           V           V           V           V


@double
def double_me(element):
    """Test function for @double."""
    return element


@stopwatch
def measure_me():
    """Test function for @stopwatch."""
    time.sleep(0.21)
    return 5


@memoize
def fibonacci(n: int):
    """Test function for @memoize."""
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


@catch(KeyError, ZeroDivisionError)
def error_func(iterable):
    """Test function for @catch."""
    return iterable[2]


@read_data
def process_file_contents(data: list, prefix: str = ""):
    """Test function for @read_data."""
    return [prefix + line for line in data]


@enforce_types
def no_more_duck_typing(num: int | float, g: None) -> str:
    """Test function for @enforce_types."""
    return str(num)


if __name__ == '__main__':
    print(double_me(5))  # 10
    print(double_me("Hello"))  # HelloHello
    print()

    print(measure_me())  # It took 0.21... seconds for measure_me to run
    # 5
    print()

    print(fibonacci(35))  # 9227465
    # Probably takes about 2 seconds without memoization and under 50 microseconds with memoization
    print()

    print(error_func("Hello"))  # (0, 'l')
    print(error_func([5, 6, 7]))  # (0, 7)
    print(error_func({}))  # (1, <class 'KeyError'>)

    try:
        print(error_func([]))
        print("IndexError should not be caught at this situation.")
    except IndexError:
        print("IndexError was thrown (as it should).")

    print()

    print(process_file_contents("hi"))  # This assumes you have a file "data.txt". It should print out the file
    # contents in a list with "hi" in front of each line like ["hiLine 1", "hiLine 2", ...].
    print(process_file_contents())  # This should just print out the file contents in a list.
    print()

    print(no_more_duck_typing(5, None))  # 5

    try:
        print(no_more_duck_typing("5", None))
        print("TypeError should be thrown, but wasn't.")
    except TypeError as e:
        print(e)  # Argument 'num' must be of type int or float, but was '5' of type str

    try:
        print(no_more_duck_typing(5.0, 2))
        print("TypeError should be thrown, but wasn't.")
    except TypeError as e:
        print(e)  # Argument 'g' must be of type NoneType, but was 2 of type int
