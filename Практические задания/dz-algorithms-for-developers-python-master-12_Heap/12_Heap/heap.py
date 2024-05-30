from typing import List


class TruckCoordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def __repr__(self):
        return self.__str__()


def k_closest_trucks(truck_coordinate_list: List[TruckCoordinate], k: int) -> List[TruckCoordinate]:
    return []


def unloading_truck(n: int, times: List[int]) -> List[int]:
    return []


def build_heap_from_array(checks: List[int]) -> None:
    pass
