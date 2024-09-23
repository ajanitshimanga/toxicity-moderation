import logging
import os
from abc import abstractmethod, ABC

from openai import OpenAI
from dotenv import load_dotenv

from schemas.clients.Client import Client
from utils import load_content

logger = logging.Logger(__name__)


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

    def __init__(self, client: Client = None):
        self.system_prompt_location = os.getcwd() + "/data/prompts/toxicity-classification-prompt.txt"
        load_dotenv()

        # TODO (ajanitshimanga): I'd like to change this to a client instance that's passed to ModerationService.
        if client:
            self.client = client
        else:
            self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def classify_text(self, input_text_content: str) -> dict:
        # load system prompt
        system_prompt = load_content(self.system_prompt_location)

        # OpenAI specific request setup TODO(ajanitshimanga): allow client type specific handling of request setup.
        system = [{"role": "system", "content": system_prompt}]
        chat_history = []  # past user and assistant turns for AI memory
        user = [{"role": "user", "content": input_text_content}]

        # OpenAI Chat Completion request for inference
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",    # TODO: config that loads env variable for model type.
            messages=system + chat_history + user,
            max_tokens=3000
        )

        return get_content_from_response(response)
