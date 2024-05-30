from typing import List, Optional

from contact import Contact


class Node:
    def __init__(self):
        self.next: List[Optional[Node]] = [None] * 256
        self.end_here: List[Contact] = []
        self.cnt = 0


class ContactBook:
    """XXX Этот класс должен быть реализован при помощи бора (trie)."""

    def __init__(self):
        self.root = Node()

    def add(self, s: Contact):
        """Добавляет имя нового контакта в адресную книгу."""
        # TODO please implement this

    def contains(self, name: str) -> bool:
        """Возвращает true, если контакт с именем name есть в книге."""
        # TODO please implement this
        return False

    def count_starts_with(self, pref: str) -> int:
        """Возвращает количество контактов, добавленных в адресную книгу, имена которых начинаются с pref."""
        # TODO please implement this
        return 0

    def starts_with(self, pref: str) -> List[Contact]:
        """Возвращает все контакты, имена которых начинаются с префикса pref."""
        # TODO please implement this
        return []

    __contains__ = contains
