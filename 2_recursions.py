# Вычислить значение факториала
def factorial(item):
    if item == 1:
        return 1
    else:
        return item * factorial(item - 1)


# print(factorial(3))

# Разделить поле на одинаковые квадраты максимального размера.
# Ищем размер такого квадрата
def max_side_quater(length, width):
    if length % width == 0:
        return width
    else:
        new_width = length % width
        return max_side_quater(width, new_width)


# print(max_side_quater(1680, 640))

# Вычислить сумму списка
def summ(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + summ(arr[1:])


# print(summ([1, 2, 3, 4]))


# Посчитать количество элементов списка
def count_items(arr):
    if arr == []:
        return 0
    else:
        return 1 + count_items(arr[1:])


# print(count_items(['hu', 'ооо', 'gyg', 'dgd']))


# Вычислисть максимальное значение в списке
def max_value(arr):
    maximum = arr[0]
    if len(arr) < 2:
        return maximum
    else:
        new_arr = [i for i in arr if i > maximum]
        return max_value(new_arr)


# print(max_value([1, 2, 3, 4, 5, 3, 7, 2, 1, 0]))


# Бинарный поиск
def be_search(arr, answer):
    mid = len(arr) // 2
    guess = arr[mid]
    if guess == answer:
        return guess
    elif guess < answer:
        return be_search(arr[mid + 1:], answer)
    else:
        return be_search(arr[:mid], answer)


# print(be_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 4))
