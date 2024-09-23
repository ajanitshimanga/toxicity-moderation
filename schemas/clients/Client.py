from abc import abstractmethod, ABC


class Client(ABC):

    @abstractmethod
    def llm_completion(self, payload: dict):
        raise NotImplementedError
