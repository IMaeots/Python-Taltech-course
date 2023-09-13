"""EX02 operations."""

from math import floor

""" Add a to b. Print out the result."""
a = int(input("Enter the value for a:"))
b = int(input("Enter the value for b:"))
print(f"{a + b}")

""" Subtract d from c. Print out the result."""
c = int(input("Enter the value for c:"))
d = int(input("Enter the value for d:"))
print(f"{c - d}")

""" Multiply e by f. Print the result."""
e = int(input("Enter the value for e:"))
f = int(input("Enter the value for f:"))
print(f"{e * f}")

"""Divide g by h. Print the result."""
g = int(input("Enter the value for g:"))
h = int(input("Enter the value for h:"))
print(f"{g / h}")

"""Divide i by j. Print the remainder. Use an arithmetic operator."""
i = int(input("Enter the value for i:"))
j = int(input("Enter the value for j:"))
print(f"{i % j}")

"""Divide k by L. Print out the floor value. Use an arithmetic operator."""
k = int(input("Enter the value for k:"))
L = int(input("Enter the value for L:"))
print(f"{floor(k / L)}")

"""Calculate m raised to the power of n. Print out the result."""
m = int(input("Enter the value for m:"))
n = int(input("Enter the value for n:"))
print(f"{m ** n}")

"""If o is greater or equal than p then print True. If not then print False."""
o = int(input("Enter the value for o:"))
p = int(input("Enter the value for p:"))
if o >= p:
    print("True")
else:
    print("False")

"""If r is less or equal than q then print True. If not then print False. """
q = int(input("Enter the value for q:"))
r = int(input("Enter the value for r:"))
if r <= q:
    print("True")
else:
    print("False")

"""If s and z are the same values, then print True. If not then print False."""
s = int(input("Enter the value for s:"))
z = int(input("Enter the value for z:"))
if s == z:
    print("True")
else:
    print("False")

"""If t value is not the same as u value then print True. If not then print False."""
t = int(input("Enter the value for t:"))
u = int(input("Enter the value for u:"))
if t != u:
    print("True")
else:
    print("False")

"""Print out the volume of the cuboid."""
length = int(input("Enter the value for length:"))
width = int(input("Enter the value for width:"))
height = int(input("Enter the value for height:"))
print(f"{length * width * height}")

"""Convert days, minutes, hours and seconds into minutes.

Example 1
days = 0
hours = 0
minutes = 1
seconds = 15

Output
1.25

Example 2
days = 0
hours = 1
minutes = 5
seconds = 0

Output
65
"""
days = int(input("Enter the value for days:"))
hours = int(input("Enter the value for hours:"))
minutes = int(input("Enter the value for minutes:"))
seconds = int(input("Enter the value for seconds:"))
print(f"{days * 1440 + hours * 60 + minutes + seconds / 60}")