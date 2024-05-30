from abc import ABC, abstractmethod


class SuperArray(ABC):
    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def get(self, position: int) -> int:
        pass

    @abstractmethod
    def set(self, position: int, value: int) -> None:
        pass
