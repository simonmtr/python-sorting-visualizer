from abc import ABC, abstractmethod


class SortingVisualisationA(ABC):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()
    @abstractmethod
    def get_coordinates(self):
        pass
