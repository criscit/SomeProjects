from typing import List


class DatingUser:
    def __init__(self, iq: int, name: str):
        self.iq = iq
        self.name = name


def do_i_know_this_language(languages: List[str], search: str) -> bool:
    pass

def find_phone_number(sorted_phone_numbers: List[int], search: int) -> int:
    pass

def find_users(users_sorted_by_iq: List[DatingUser], lower_iq_bound: int, professor_iq: int) -> List[str]:
    pass
