import requests

from llms.LLMService import LLMService


class OllamaService(LLMService):

    def __init__(self, api_url: str):
        self.api_url = api_url

    def generation_completion(self, prompt: str) -> str:
        response = requests.post(self.api_url, json={"prompt": prompt})
        return response.json().get("output", "No response")
