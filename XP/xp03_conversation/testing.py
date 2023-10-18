"""Testing file for conversation."""
import re

regex_a = r'([-+]?\s*\d*)x2'  # Leiab ruutliikme kordaja
regex_b = r'([-+]?\s*\d*)x(?![\d])'  # Leiab lineaarliikme kordaja
regex_c = r'(?<!x)([-+]?\s*\d+)(?![\dx])'  # Leiab vabaliikme

if __name__ == '__main__':

    def print_regex_results(regex, f1):
        """Print regex results to display."""
        for match in re.finditer(regex, f1):
            print(match.group(1))

    f = "3x2 - 4x + 1"

    print_regex_results(regex_a, f)  # 3
    print_regex_results(regex_b, f)  # - 4
    print_regex_results(regex_c, f)  # 1

    f2 = "3x2 + 4x + 5 - 2x2 - 7x + 4"

    print("x2")
    print_regex_results(regex_a, f2)  # 3, - 2.
    print("x")
    print_regex_results(regex_b, f2)  # 4, - 7.
    print("c")
    print_regex_results(regex_c, f2)  # 5, 4.
