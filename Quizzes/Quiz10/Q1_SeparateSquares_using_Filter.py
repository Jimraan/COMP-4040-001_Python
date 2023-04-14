# Quiz 10 Question 1
# Given a list of integers, write Python code to separate only the squares of the odd
# numbers from the list my_list.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def sep_squares(numbers):
    # using filter and lambda
    res = list(filter(lambda x: x % 2 != 0, numbers))
    for i in range(len(res)):
        res[i] = res[i]**2

    return res


print(sep_squares(my_list))
