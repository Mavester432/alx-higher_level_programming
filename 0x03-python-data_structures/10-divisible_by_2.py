#!/usr/bin/python3
def divisible_by_2(my_list=None):
    if my_list is None:
        my_list = []

    new_list = []
    if my_list:
        for num in my_list:
            new_list.append(True if num % 2 == 0 else False)
        return new_list
