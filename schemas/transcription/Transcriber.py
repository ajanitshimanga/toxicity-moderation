from abc import ABC, abstractmethod


class Transcriber(ABC):

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def transcribe(self, mp3_path: str) -> str:
        raise NotImplementedError
