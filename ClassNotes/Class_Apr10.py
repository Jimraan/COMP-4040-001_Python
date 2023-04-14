# def my_func(num):
#     return num * num
#
# my_list = [1, 2, 3, 4, 5, 6]
#
# #1
# my_list2 = list(map(my_func, my_list))
#
# print(my_list)
# print(my_list2)
# print()
#
# my_list3 = list(map(lambda x: x*x, my_list))
#
# print(my_list3)
# print()
#
# #2
# print("#2")
# my_list4 = list(map(lambda x: x**2 if x % 2 == 0 else x**3, my_list))
# print(my_list4)
# print()
#
# #3
# print("#3")
# res = list(filter(lambda x: x % 2 == 0, my_list))
# print(res)
#
# #4
# print("#4")
# from functools import reduce
# res = reduce(lambda x, y: x * y, my_list)
# print(res)


# dogs = ["Todd", "Tom", "Bob"]
# big_dogs = []
# for dog in dogs:
#     big_dogs.append("Big {}".format(dog))
# print(big_dogs)
#
# big_dogs = ["Big {}".format(dog) for dog in dogs]
# big_dogs = ["Big " + dog for dog in dogs]
#
# print(big_dogs)


# classwork
numbers = [10, 20, 30, 40, 50]
res = {i:numbers[i] for i in range(len(numbers))}
# print(res)

# res = {(lambda i:numbers[i]**2) for i in range(len(numbers))}
res = {i:[num**i for num in numbers] for i in range(len(numbers))}
print(res)
print()

res = {i: list(map(lambda x: x**i, numbers)) for i in range(len(numbers))}
print(res)
print()