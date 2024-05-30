from item import Item
from typing import List


def sort(items: List[Item]):
    #  Write code here
    pass


def quick_sort(array, low, high):
    if not array:
        return  # завершить выполнение если длина массива равна 0

    if low >= high:
        return  # завершить выполнение если уже нечего делить

    # выбрать опорный элемент
    middle = low + (high - low) / 2
    opora = array[middle]

    # разделить на подмассивы, который больше и меньше опорного элемента
    i = low
    j = high
    while i <= j:
        while array[i].compare_to(opora) < 0:
            i += 1
        while array[j].compare_to(opora) > 0:
            j -= 1
        if i <= j:  # меняем местами
            array[i] = array[j]
            array[j] = temp
            i += 1
            j -= 1

    # вызов рекурсии для сортировки левой и правой части
    if low < j:
        quick_sort(array, low, j)

    if high > i:
        quick_sort(array, i, high)
