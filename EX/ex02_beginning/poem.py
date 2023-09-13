"""EX02 Poem."""

"""
Ask for user's inputs and print out a poem in one line using f string and newline (\n)

Example input:
color = "red"
objects = "violets"
activity = "code"

Example output:
Roses are red,
violets are blue,
I love to code
And so will you!
"""
color = input("Enter a random color: ")
objects = input("Enter a plural noun: ")
activity = input("Enter an activity: ")
print(f"Roses are {color},\n{objects} are blue,\nI love to {activity}\nAnd so will you!")