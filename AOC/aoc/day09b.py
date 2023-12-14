"""Day 09 part B solution."""

with open('day09_data.txt', 'r') as file:
    text = file.read().strip()

text = text.split('\n')


def f(xs):
    """Process a list of integers."""
    # Base case.
    if all(x == 0 for x in xs):
        return 0

    # Calculate the differences between consecutive elements in 'xs'.
    differences = []
    for i in range(len(xs) - 1):
        differences.append(xs[i + 1] - xs[i])

    # Recursively call 'f' with updated parameters.
    return xs[0] + -1 * f(differences)


ans = 0

for line in text:
    # Convert each line into a list of integers
    xs = [int(x) for x in line.split()]

    # Add the result of 'f' to 'ans' after processing the list of integers 'xs'
    ans += f(xs)

print(ans)