"""Day 01 part B solution."""

with open('day01_data.txt', 'r') as file:
    text = file.read().strip()

b = 0
for line in text.split('\n'):
    b_digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            b_digits.append(c)

        for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(val):
                b_digits.append(str(d + 1))

    b += int(b_digits[0] + b_digits[-1])

print(b)  # Part B answer
