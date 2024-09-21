import openai

from llms.LLMService import LLMService


class OpenAIService(LLMService):

    def __init__(self, api_key: str, model_name: str = "gpt-3.5-turbo"):
        self.api_key = api_key
        self.model_name = model_name
        openai.api_key = self.api_key

    def generation_completion(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
