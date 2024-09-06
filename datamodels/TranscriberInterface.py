from abc import ABC, abstractmethod


class TranscriberInterface(ABC):

    @abstractmethod
    def __init__(self, location):
        self.location = location

    @abstractmethod
    def transcribe(self) -> str:
        pass
