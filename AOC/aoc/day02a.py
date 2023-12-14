from collections import defaultdict

color_limits = {'red': 12, 'green': 13, 'blue': 14}

with open('day02_data.txt', 'r') as file:
    lines = file.readlines()

total_score = 0

# Process each line
for line in lines:
    game, data_str = line.strip().split(':')
    events = data_str.split(';')

    color_data = defaultdict(int)
    ok = True

    for event in events:
        balls = event.split(',')
        for ball in balls:
            num, color = ball.split()
            num = int(num)
            color_data[color] = max(color_data[color], num)
            if num > color_limits.get(color, 0):
                ok = False

    if ok:
        score = 1
        for value in color_data.values():
            score *= value
        total_score += int(game.split()[-1])

print(total_score)
