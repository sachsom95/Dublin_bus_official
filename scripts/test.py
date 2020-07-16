import math


def binary(val, lst):
    first = 0
    last = len(lst) - 1
    mid = 0

    while (first <= last):
        mid = math.floor((first + last) / 2)
        if (lst[mid] < val):
            first = mid+1
        else:
            last = mid-1

        if (lst[mid] == val):
            return True
    else:
        return False


x = [1, 2, 3, 4]
print(binary(5, x))