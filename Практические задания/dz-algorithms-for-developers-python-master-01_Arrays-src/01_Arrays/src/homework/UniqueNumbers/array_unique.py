from typing import List


def letters_learned_today(word: str) -> str:
    res = ""
    for ch in word:
        if ch not in res:
            res += ch
    return res


def avoid_jail_due_to_tax_fraud(report: List[List[int]]) -> int:
    unique = []
    for row in report:
        for col in row:
            if col in unique:
                return col
            unique.append(col)

    return -1  # please implement
