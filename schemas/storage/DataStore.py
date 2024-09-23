from abc import ABC, abstractmethod


class DataStore(ABC):

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def store(self, text: str) -> str:
        raise NotImplementedError
