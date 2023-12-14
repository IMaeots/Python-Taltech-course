"""Day 02 part B solution."""

from collections import defaultdict

with open('day02_data.txt', 'r') as file:
    text = file.read().strip()

b = 0

for line in text.split('\n'):
    game, line = line.split(':')
    data = defaultdict(int)
    for event in line.split(';'):
        for balls in event.split(','):
            num, color = balls.split()
            num = int(num)
            data[color] = max(data[color], num)

    score = 1
    for d in data.values():
        score *= d
    b += score

print(b)
