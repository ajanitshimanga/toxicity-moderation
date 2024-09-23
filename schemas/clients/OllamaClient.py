import requests

from schemas.clients.Client import Client


class OllamaClient(Client):
    def __init__(self, url, model_name: str = "llama3"):
        self.model_name = model_name
        self.url = url

    def llm_completion(self, payload: dict):
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(self.url, json=payload, headers=headers)
        return response
