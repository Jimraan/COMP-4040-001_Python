# Quiz 10 Question 5
# Using Python, ask the user to enter a number. Then using that number in a single line
# code, produce a list of dictionaries as in the following example:
# Enter your number: 4
# [{1: {“item 1”: [1, 1, 1]}}, {2: {“item 2”: [4, 4, 4]}}, {3: {“item 3”: [27, 27, 27]}}, {4: {“item 4”: [256,
# 256, 256]}}]
# Note that, each dictionary has a key and a list of three values that each of them is to the power
# of itself.
# Here is another example:
# Enter a number: 5
# [{1: {“item 1”: [1, 1, 1]}}, {2: {“item 2”: [4, 4, 4]}}, {3: {“item 3”: [27, 27, 27]}}, {4: {“item 4”: [256,
# 256, 256]}}, {5: {“item 5”: [ 3125, 3125, 3125]}}}]

user_input = int(input("Enter a number: "))

res = [{i: {"list " + str(i): list(map(lambda x: x**i, [i, i, i]))}} for i in range(1, user_input+1)]
print(res)
