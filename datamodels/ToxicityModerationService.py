import os
import uuid

from openai import OpenAI
from dotenv import load_dotenv


def get_content_from_response(response):
    return response.choices[0].message.content


class ToxicityModerationService:
    def __init__(self):
        self.system_prompt_location = "/Users/eren/personal-projects/toxicity-moderation/" \
                                      "data/prompts/toxicity-classification-prompt.txt"
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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


def write_content(content: str, file_name: str = None,
                  absolute_save_path: str = "/Users/eren/personal-projects/toxicity-moderation/data/responses/") -> bool:
    """
    If write succeeds, then True is returned. Else False.

    :param content:
    :param file_name:
    :param absolute_save_path:
    :return:
    """
    if not file_name:
        file_name = "response_" + str(uuid.uuid4()) + ".txt"

    full_path = os.path.join(absolute_save_path, file_name)

    try:
        with open(full_path, 'w') as file:
            file.write(content + "\n")
    except Exception as e:
        print("Error in write_content: " + str(e))
        return False
    print("Wrote contents to: " + str(full_path))
    return True


def load_content(absolute_file_path: str) -> str:
    """
    If load succeeds, then text is returned. Else None.


    :param absolute_file_path:
    :return:
    """

    try:
        with open(absolute_file_path, 'r') as file:
            content_to_classify = file.read()
    except Exception as e:

        print("Error in load_content: " + str(e))
        return None
    return content_to_classify

