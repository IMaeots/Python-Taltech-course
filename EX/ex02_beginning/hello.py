"""EX02 Hello."""

"""
Print Hello
Example output:

What is your name? Mari
Hello, Mari! Enter a random number: 5
Great! Now enter a second random number: 4
5 + 4 is 9

"""
# ask for a name
name = input("What is your name? ")
# ask for first random number
num1 = int(input("Hello, {}! Enter a random number: ".format(name)))
# ask for second random number
num2 = int(input("Great! Now enter a second random number: "))
# print out sum
print(f"{num1} + {num2} is {num1 + num2}")
