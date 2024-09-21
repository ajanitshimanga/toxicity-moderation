from abc import ABC, abstractmethod


class LLMService(ABC):

    @abstractmethod
    def generation_completion(self, prompt: str) -> str:
        raise NotImplementedError

