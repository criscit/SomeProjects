from typing import List


class TextEditor:
    def insert_character_at(self, position: int, c: str) -> None:
        """
        Этот метод должен вставлять символ в строку на позиции position
        Например когда пользователь напечатал “При|ет мир!” (этот текст у нас в атрибуте text)
        и его курсор находится между буквами “и” и “е”, и он нажимает “в”.
        В этот момент вызывается метод insert_character_at(3, “в”), после чего в атрибуте text
        значение меняется на “Привет мир!”
        """

    def backspace(self, position: int) -> None:
        """
        “Привет Мм|ир!” => “Привет Мир!”
        """

    def __init__(self) -> None:
        self.text_length: int = 0
        self.text: List[str] = [" "] * 255  # Больше 255 символов в память не влезает =/
        # Пустое место в списке self.text забито просто “пробелами”
        # Например, если self.text_length = 3, и text = {‘ш’,’к’,’я’, … еще 252 символа ‘пробел’ .. }
