"""EX02 Maths."""

"""
Find the average of a, b, c and d, but first the numbers must be multiplied. a multiplied by 1, b multiplied by 2,
c multiplied by 3 and d multiplied by 4.
After the multiplication find the average of the numbers and print it out.

Example 1
a = 0
b = 0
c = 0
d = 4

Output
4

Example 2
a = 1
b = 2
c = 3
d = 4
Output
7.5

Example 2
a = 5
b = 0
c = 5
d = 1

Output
6

 """
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
d = int(input("Enter the value of d: "))
print(f"{(a + b * 2 + c * 3 + d * 4) / 4}")

"""
Calculate the sum of two fractions.

One fraction is x/y where x and y are numbers given as input.
The other fraction is u/t where u and t are also numbers given as input.

Find and print the sum of x/y + u/t.

NB! the fraction does not have to be in the simplest form.
NB! the answer should be given as a string and should not contain any commas.

Example 1
x = 1
y = 3
u = 1
t = 3

Output
2/3 or 6/9 or 4/6

Example 2
x = 2
y = 5
u = 1
t = 5

Output
3/5
"""
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
u = int(input("Enter the value of u: "))
t = int(input("Enter the value of t: "))
print(f"{x * t + y * u}/{y * t}")

"""
Calculate and print how many hours are needed per week with given ECTS and amount of weeks, if each ECTS is 26 hours.

If it is not possible, print out -1.

Example 1
ects = 30
weeks = 12

Output
65

Example 2
ects = 1
weeks = 1

output
26

Example 3
ects = 1
weeks = 0

output
-1
"""
ects = int(input("Enter the amount of ECTS: "))
weeks = int(input("Enter the number of weeks: "))
try:
    print(f"{ects * 26 / weeks}")
except:
    print("-1")
