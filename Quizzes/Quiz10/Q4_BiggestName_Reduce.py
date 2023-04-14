# Quiz 10 Question 4
from functools import reduce
names = []

for i in range(5):
    names.append(input("Enter name " + str(i+1) + ": "))


def bigger(name, name2):
    return name if len(name) > len(name2) else name2


res = list(reduce(bigger, names))
print("No Lambda: ", res)
res = list(reduce(lambda x, y: x if len(x) > len(y) else y, names))
print("With Lambda: ", res)
