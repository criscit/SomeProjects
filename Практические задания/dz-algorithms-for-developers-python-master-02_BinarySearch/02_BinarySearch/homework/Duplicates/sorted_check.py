from typing import List


"""
НЕ СМОТРИТЕ В ЭТОТ ФАЙЛ=)
ЗАКРОЙТЕ ЭТОТ КОД!!


Нет, ну если очень хочется, то посмотрите...

Там ниже реализован метод, который проверяет
отсортирован ли список или нет.

Он понадобится для выполнения задания в random_sort.py

Самым лучшим вариантом будет
реализовать такой метод самостоятельно,
и не подсматривать в то что находится там внизу
























































Вы хотя бы попробуйте, у вас наверняка получится!
























































Ок, вот:
"""

def is_sorted(array: List[int]) -> bool:
    for i in range(len(array) - 1):
        # В отсортированном списке каждый следующий элемент должен быть больше либо равен предыдущему
        if array[i + 1] < array[i]:
            return False

    # если цикл закончился, значит условие с return False ни разу не сработало и можно возвращать True
    return True
