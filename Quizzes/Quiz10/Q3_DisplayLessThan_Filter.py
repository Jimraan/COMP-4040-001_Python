# Quiz 10 Question 3
# Given the following list
# my_list = [35, 11, 8, 2, 43, 17, 4, 99, 9, 72]
# Using Python, ask the user to enter a number and display a list of numbers that are less than
# that number. For example, if a user enters 11, it should display
# [8, 2, 4, 9]

my_list = [35, 11, 8, 2, 43, 17, 4, 99, 9, 72]

user_input = int(input("Enter a number "))


def less_than(num):
    if num < user_input:
        return True


print("Number is ", str(user_input), ", list is: ", my_list)
res = list(filter(less_than, my_list))
print("No lambda: ", res)
res = list(filter(lambda x: x < user_input, my_list))
print("With lambda: ", res)

