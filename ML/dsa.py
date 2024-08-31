import sys

def check(arr):
    min = sys.maxsize
    for i in arr:
        if i < min:
            min = i
    for i in arr:
        if not i % min == 0:
            return False
    return True

numbers = [20, 15, 5, 30, 35, 29]

print(check(numbers))