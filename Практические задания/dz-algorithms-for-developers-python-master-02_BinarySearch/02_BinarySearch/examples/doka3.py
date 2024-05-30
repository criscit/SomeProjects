class Player:
    def __init__(self, rating: int, nick_name: str) -> None:
        self.rating = rating
        self.nick_name = nick_name


class Doka3:

    def __init__(self) -> None:
        # Наша рейтинговая таблица выглядит примерно так
        self.ratings = [
            Player(1100, "Crowbar Freeman"),   # 0
            Player(1200, "London Mollarik"),   # 1
            # Player(1600, "Shmike"),
            Player(1600, "Raziel of Kain"),    # 2
            Player(1600, "Gwinter of Rivia"),  # 3
            Player(1600, "Slayer of Fate"),    # 4
            Player(3000, "Jon Know"),          # 5
            Player(4000, "Caius Cosades"),     # 6
        ]

    def find_spot(self, new_player: Player) -> int:
        left = 0
        right = len(self.ratings) - 1

        while left < right:
            middle = (left + right) // 2
            if self.ratings[middle].rating < new_player.rating:
                left = middle + 1
            else:
                right = middle

        return left


if __name__ == "__main__":
    rating = Doka3()
    spot = rating.find_spot(Player(1600, "Shmike"))
    print(spot)
