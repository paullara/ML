from collections import defaultdict

def find_mode(arr):
    frequency = defaultdict(int)
    mode = arr[0]
    max_count = 0

    for num in arr:
        frequency[num] += 1
        if frequency[num] > max_count:
            max_count = frequency[num]
            mode = num
    return mode


arr = [2, 1, 2, 3, 4, 5]

mode = find_mode(arr)
print("Mode: ",mode)