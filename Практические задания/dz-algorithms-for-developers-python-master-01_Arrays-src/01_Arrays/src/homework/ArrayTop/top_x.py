from typing import List


def find_max_under_boundary(input_array: List[int], top_boundary: int) -> int:
    # Найдем текущий максимум
    current_max = float('-inf')

    for item in input_array:
        # Рассмотрим только те элементы, которые меньше заданного числа
        if item <= top_boundary:
            current_max = max(current_max, item)

    return current_max


def find_top_elements(input_array: List[int], number_of_elements: int) -> List[int]:
    if number_of_elements > len(input_array):
        raise Exception
    # Создадим массив для результата
    input_array = input_array.copy()
    top_elements = []

    # Нам требуется знать предыдущее значение максимума,
    # По-умолчанию мы положим туда максимальное значение для типа float
    previous_max = float('inf')

    # Выполним цикл столько раз, сколько максимумов нам нужно найти
    for i in range(number_of_elements):
        # Найдем текущий максимум
        current_max = find_max_under_boundary(input_array, previous_max)

        input_array.remove(current_max)
        # Обновим значение "предыдущего" максимума
        previous_max = current_max

        # Положим результат в выходной массив
        top_elements.append(current_max)

    return top_elements


def find_min_after_boundary(input_array: List[int], bottom_boundary: int) -> int:
    current_min = float('inf')
    for el in input_array:
        if el >= bottom_boundary and el < current_min:
            current_min = el

    return current_min

def find_bottom_elements(input_array: List[int], number_of_elements: int) -> List[int]:
    if number_of_elements > len(input_array):
        raise Exception

    input_array = input_array.copy()
    res = []
    boundary = float("-inf")
    for i in range(number_of_elements):
        res.append(find_min_after_boundary(input_array, boundary))
        input_array.remove(res[-1])
        boundary = res[-1]
    return res




if __name__ == '__main__':
    array = [100, 100, 100]

    top5 = find_top_elements(array, 3)
    print("Top 5:", top5)
    print(array)
    top8 = find_top_elements(array, 3)
    print("Top 8:", top8)

    bottom5 = find_bottom_elements(array, 3)
    print("Bottom 5:", bottom5)

    bottom8 = find_bottom_elements(array, 3)
    print("Bottom 8:", bottom8)
