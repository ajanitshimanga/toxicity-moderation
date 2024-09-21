import os
from abc import abstractmethod, ABC

from openai import OpenAI
from dotenv import load_dotenv

from utils import load_content


def get_content_from_response(response):
    return response.choices[0].message.content


class ToxicityModerationInterface(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def classify_text(self, text_content: str) -> str:
        pass


class ToxicityModerationService(ToxicityModerationInterface):
    def __init__(self):
        self.system_prompt_location = os.getcwd() + "/data/prompts/toxicity-classification-prompt.txt"
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # I'd like to change this to an LLM instance that's passed in.

    def classify_text(self, text_content: str) -> dict:
        system = [{"role": "system", "content": load_content(self.system_prompt_location)}]
        chat_history = []  # past user and assistant turns for AI memory
        user = [{"role": "user", "content": text_content}]
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=system + chat_history + user,
            max_tokens=3000
        )
        print("****** response: ", response)
        print("~~~~~ result content: " + get_content_from_response(response))
        return get_content_from_response(response)

