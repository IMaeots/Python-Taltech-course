"""Day 04 part A solution."""

with open('day04_data.txt', 'r') as file:
    text = file.read().strip()

lines = text.split('\n')
p1 = 0
for i, line in enumerate(lines):
    first, rest = line.split('|')
    id_, card = first.split(':')
    card_nums = [int(x) for x in card.split()]
    rest_nums = [int(x) for x in rest.split()]
    val = len(set(card_nums) & set(rest_nums))
    if val > 0:
        p1 += 2 ** (val - 1)

print(p1)
