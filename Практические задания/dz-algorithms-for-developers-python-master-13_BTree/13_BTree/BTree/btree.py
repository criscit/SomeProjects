from typing import List


class BTree:
    def __init__(self):
        # TODO implement this
        pass

    def add(self, x: int):
        """Добавляет число X в дерево."""
        # TODO implement this

    def contains(self, x: int) -> bool:
        """Проверяет, было ли число X добавлено в дерево."""
        # TODO implement this

    def get_max_height(self) -> int:
        """Выводит текущую максимальную глубину дерева."""
        # TODO implement this
        return 1

    def get_sorted(self) -> List[int]:
        """Возвращает список всех чисел, добавленных в дерево в возрастающем порядке."""
        # TODO implement this
        return []

    # shortcuts for magic methods
    __contains__ = contains
