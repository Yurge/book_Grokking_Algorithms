def fast_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        mid_ind = len(arr) // 2
        target = arr[mid_ind]
        less = [num for num in arr if num < target]
        more = [num for num in arr if num > target]
        return fast_sort(less) + [target] + fast_sort(more)


print(fast_sort((5, 3, 7, 6, 8, 1, 2, 4)))
