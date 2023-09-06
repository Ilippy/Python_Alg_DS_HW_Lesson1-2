import random
from time import time
import numpy


def how_long(func, arr):
    temp_list = arr[::]
    start = time()
    func(temp_list)
    print(f"На это ушло времени {time() - start}")


# Задание 1
# 1.Необходимо написать один из простых алгоритмов сортировки, имеющий сложность O(n2).
# 2.Можно выбрать из пузырьковой сортировки, сортировки вставками и
# сортировки выбором.
# 3.Следует обратить внимание на сложность данных алгоритмов и
# указать признаки квадратичной сложности для каждого из них

def sorting(array: list):
    """Пузырьковая сортировка"""
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


# Задание 2
# Написать алгоритм быстрого поиска (quicksort).

def quick_sort(array: list) -> list:
    """Быстрая сортировка"""
    if len(array) <= 1:
        return array
    q = random.choice(array)
    left_array = []
    middle_array = []
    right_array = []
    for el in array:
        if el == q:
            middle_array.append(el)
        elif el < q:
            left_array.append(el)
        else:
            right_array.append(el)
    return quick_sort(left_array) + middle_array + quick_sort(right_array)

    # Сортировка целых чисел
    # Исходная последовательность чисел длины n, а в конце отсортированная, хранится в массиве A.
    # Также используется вспомогательный массив C с индексами от 0  до k−1, изначально заполняемый нулями.
    # Последовательно пройдём по массиву A и запишем в C[i] количество чисел, равных i.
    # Теперь достаточно пройти по массиву C и для каждого number∈{0,...,k−1}  в массив A
    # последовательно записать число C[number] раз.


def counting_sort(array: list) -> list:
    temp_array = [0] * (max(array) + 1)
    for el in array:
        temp_array[el] += 1
    result_array = []
    for i in range(len(temp_array)):
        result_array += [i] * temp_array[i]
    return result_array


def merge_two_list(a: list, b: list) -> list:
    result = []
    while a and b:
        result.append((a if a[0] < b[0] else b).pop(0))
    result += a + b
    return result


def merge_sort(array: list) -> list:
    """Сортировка слиянием"""
    mid = len(array) // 2
    return array if len(array) <= 1 else merge_two_list(merge_sort(array[:mid]), merge_sort(array[mid:]))


# ДЗ - Реализовать алгоритм пирамидальной сортировки (сортировка кучей).
def heapify(array: list, i: int, n: int):
    i_left = 2 * i + 1
    i_right = 2 * i + 2
    i_largest = i
    if i_left <= n and array[i_left] > array[i_largest]:
        i_largest = i_left
    if i_right <= n and array[i_right] > array[i_largest]:
        i_largest = i_right
    if i_largest == i:
        return
    else:
        array[i_largest], array[i] = array[i], array[i_largest]
        heapify(array, i_largest, n)


def build_max_heap(array: list):
    i_middle = len(array) // 2
    for index in range(i_middle, -1, -1):
        heapify(array, index, len(array) - 1)


def heap_sort(array: list) -> list:
    build_max_heap(array)
    for index in range(len(array) - 1, 0, -1):
        array[0], array[index] = array[index], array[0]
        heapify(array, 0, index - 1)
    return array


#
# test_list = [random.randint(0, 100) for _ in range(10)]
# print(test_list)
# print(heap_sort(test_list))


new_list = [random.randint(0, 1_000_000) for _ in range(10_000)]
# print(new_list)

print("Numpy sort")
how_long(numpy.sort, new_list)

print("Built in sorting")
how_long(sorted, new_list)

print("Quick sort")
how_long(quick_sort, new_list)

print("Merge sort")
how_long(merge_sort, new_list)

print("Heap sort")
how_long(heap_sort, new_list)

print("Counting sort")
how_long(counting_sort, new_list)

print("Bubble sort")
how_long(sorting, new_list)
