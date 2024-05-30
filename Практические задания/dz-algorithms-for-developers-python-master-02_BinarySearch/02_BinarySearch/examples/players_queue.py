from typing import List


class Player:

    def __init__(self, rating_band: int, nick_name: str) -> None:
        self.rating_band = rating_band
        self.nick_name = nick_name


def search_leftmost_player_with_rating(queue: List[Player], search: int) -> int:
    left = 0
    right = len(queue)
    while left < right:
        middle = (left + right) // 2
        if queue[middle].rating_band < search:
            left = middle + 1
        else:
            right = middle

    return left


if __name__ == '__main__':
    queue = [
        Player(1000, "Crowbar Freeman"),
        Player(1000, "London Mollarik"),
        Player(1010, "London Mollarik 10"),
        Player(1012, "London Mollarik 12"),
        Player(1014, "London Mollarik 14"),
        Player(1016, "London Mollarik 16"),
        Player(1016, "London Mollarik 18"),
        Player(1500, "Raziel of Kain"),
        Player(1500, "Gwinter of Rivia"),
        Player(1500, "Slayer of Fate"),
        Player(3000, "Jon Know"),
        Player(4000, "Caius Cosades")
    ]

    print("1011:" + queue[search_leftmost_player_with_rating(queue, 1011)].nick_name)
    print("1013:" + queue[search_leftmost_player_with_rating(queue, 1013)].nick_name)
    print("1015:" + queue[search_leftmost_player_with_rating(queue, 1015)].nick_name)
    print("1017:" + queue[search_leftmost_player_with_rating(queue, 1017)].nick_name)
