from abc import ABC, abstractmethod


class StorageInterface(ABC):

    @abstractmethod
    def __init__(self, location):
        self.location = location

    @abstractmethod
    def store(self) -> None:
        pass
