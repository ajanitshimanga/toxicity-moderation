from llms import LLMService
from llms.OllamaService import OllamaService
from llms.OpenAIService import OpenAIService


class LLMFactory:

    @staticmethod
    def get_llm_service(service_type: str, config: dict) -> LLMService:
        if service_type == "openai":
            return OpenAIService(api_key=config.get("api_key"), model_name=config.get("model_name", "gpt-3.5-turbo"))
        elif service_type == "ollama":
            return OllamaService(api_url=config.get("api_url"))
        else:
            raise ValueError(f"Unsupported LLM service type: {service_type}")
