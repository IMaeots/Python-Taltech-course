"""
Create a machine that dispenses money using 1€, 5€, 10€, 20€, 50€ and 100€ banknotes.

Given the sum, one must print out how many banknotes does it take to cover the sum. Task is to cover the sum with as little
banknotes as possible.

Example
The sum is 72€
We use four banknotes to cover it. The banknotes are 20€, 50€, 1€ and 1€.
"""

amount = int(input("Enter a sum: "))
banknotes = 0
while amount > 0:
    if amount >= 100:
        banknotes += 1
        amount -= 100
    elif amount >= 50:
        banknotes += 1
        amount -= 50
    elif amount >= 20:
        banknotes += 1
        amount -= 20
    elif amount >= 10:
        banknotes += 1
        amount -= 10
    elif amount >= 5:
        banknotes += 1
        amount -= 5
    elif amount >= 1:
        banknotes += 1
        amount -= 1

print(f"Amount of banknotes needed: {banknotes}")