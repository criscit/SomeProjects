from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def get_weight(self) -> int:
        pass
