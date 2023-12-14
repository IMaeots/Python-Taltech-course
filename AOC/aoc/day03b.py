"""Day 03 B Solution."""

from collections import defaultdict

with open('day03_data.txt', 'r') as file:
    text = file.read().strip()

data = text.split('\n')
G = [[c for c in line] for line in data]
R = len(G)
C = len(G[0])

nums = defaultdict(list)
for r, row in enumerate(G):
    gears = set()  # Positions of '*' characters next to the current number
    n = 0
    has_part = False
    for c, _ in enumerate(row):
        if c < C and row[c].isdigit():
            n = n * 10 + int(row[c])
            for rr in [-1, 0, 1]:
                for cc in [-1, 0, 1]:
                    if 0 <= r + rr < R and 0 <= c + cc < C:
                        ch = G[r + rr][c + cc]
                        if not ch.isdigit() and ch != '.':
                            has_part = True
                        if ch == '*':
                            gears.add((r + rr, c + cc))
        elif n > 0:
            for gear in gears:
                nums[gear].append(n)
            n = 0
            has_part = False
            gears = set()

# Calculate gear ratios and sum them up
gear_ratios = []
for k, v in nums.items():
    if len(v) == 2:
        gear_ratios.append(v[0] * v[1])

total_gear_ratios = sum(gear_ratios)
print(total_gear_ratios)
