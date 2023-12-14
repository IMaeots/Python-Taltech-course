"""Day 03 A Solution."""

with open('day03_data.txt', 'r') as file:
    text = file.read().strip()

data = text.split('\n')
G = [[c for c in line] for line in data]
R, C = len(G), len(G[0])

def is_valid(row, col):
    return 0 <= row < R and 0 <= col < C

p1 = 0
for r in range(R):
    for c in range(C):
        if G[r][c].isdigit():
            number = int(G[r][c])
            has_part = False
            gears = {(r + rr, c + cc) for rr in [-1, 0, 1] for cc in [-1, 0, 1]
                     if is_valid(r + rr, c + cc) and not G[r + rr][c + cc].isdigit() and G[r + rr][c + cc] != '.'}
            for rr, cc in gears:
                if G[rr][cc] == '*':
                    has_part = True
            if has_part:
                p1 += number

print(p1)
