
arr = [6, 3, 5, 2, 8]


def minimal_ind(arr):
    ind = 0
    for item in range(len(arr)):
        minimal = arr[ind]
        if arr[item] < minimal:
            ind = item
    return ind


def sorting_nums_ascending(arr):
    new_arr = []
    for _ in range(len(arr)):
        smallest_ind = minimal_ind(arr)
        value = arr.pop(smallest_ind)
        new_arr.append(value)
    return new_arr


print(sorting_nums_ascending(arr))
