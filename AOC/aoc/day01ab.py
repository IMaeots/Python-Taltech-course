with open('day01_data.txt', 'r') as file:
    text = file.read().strip()

a = 0
b = 0
for line in text.split('\n'):
    a_digits = []
    b_digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            a_digits.append(c)
            b_digits.append(c)
        for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(val):
                b_digits.append(str(d + 1))
    a += int(a_digits[0] + a_digits[-1])
    b += int(b_digits[0] + b_digits[-1])
print(a)  # Part A answer
print(b)  # Part B answer
