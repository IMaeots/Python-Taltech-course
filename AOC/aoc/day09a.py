"""Day 09 part A solution."""

with open('day09_data.txt', 'r') as file:
    text = file.read().strip()

total = 0
for line in text.split('\n'):
    nums = [int(n) for n in line.split()]
    final_nums = []

    while set(nums) != {0}:
        final_nums.append(nums[-1])
        nums = [nums[i] - nums[i - 1] for i in range(1, len(nums))]

    total += sum(final_nums)

print(total)
