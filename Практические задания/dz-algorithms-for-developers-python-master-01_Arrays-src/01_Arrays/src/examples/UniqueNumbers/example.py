from typing import List


def find_unique(phone_numbers: List[int]) -> List[int]:
    # Заведем список уникальных номеров, "Блокнотик"
    unique_numbers = []

    # Пройдемся циклом по нашим номерам
    for current_number in phone_numbers:
        # Проверим есть ли уже этот номер в "Блокнотике"
        already_exists = False
        for existing_number in unique_numbers:
            if current_number == existing_number:
                already_exists = True
                break

        # Если его там нет — то добавим
        if not already_exists:
            unique_numbers.append(current_number)

    return unique_numbers


if __name__ == '__main__':
    phone_numbers = [+79161002030, +79255558877, +79219990000, +79161002030]
    unique_numbers = find_unique(phone_numbers)
    print("Unique numbers: ", unique_numbers)

"""
————————————————————————
—— Подумать на досуге ——
————————————————————————

Этот пример можно решить многими способами,
здесь мы намеренно рассматриваем самый явный и примитивный подход,
чтобы разобраться во времени выполнения этого кода.

Как бы вы переписали этот кода с использованием всех ваших знаний?
Как бы изменилось время выполнения этого кода?
"""
