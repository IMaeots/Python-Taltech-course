"""Day 01 part A solution."""

with open('day01_data.txt', 'r') as file:
    text = file.read().strip()

a = 0
for line in text.split('\n'):
    a_digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            a_digits.append(c)

    a += int(a_digits[0] + a_digits[-1])
print(a)  # Part A answer
