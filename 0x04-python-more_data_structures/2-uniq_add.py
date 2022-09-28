#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return
    number = 0
    for i in set(my_list):
        number += i
    return number
