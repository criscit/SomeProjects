def ip_to_mask(s: str) -> int:
    """
    Возвращает битовую маску по ip адресу.

    >>> ip_to_mask("0.0.0.0")
    0
    >>> ip_to_mask("127.0.0.1")
    2130706433
    """
    # TODO Implement this
    return 0


def is_submask(mask: str, submask: str) -> bool:
    """Возвращает, является ли submask подмаской mask."""
    # TODO Implement this
    return False


def rotate(mask: int, cnt: int) -> int:
    """
    Возвращает битовую маску циклически сдвинутую на cnt
    Циклы использовать запрещено. cnt может быть меньше 0 и больше 32.

    >>> rotate(1, 1)
    2
    >>> rotate(1, -1)
    -2147483648
    """
    # TODO Implement this
    return mask
