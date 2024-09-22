import os

from openai import OpenAI
from dotenv import load_dotenv

from schemas.transcription.Transcriber import Transcriber


class WhisperTranscriberService(Transcriber):
    MODEL_TYPE = "whisper-1"

    def __init__(self):

        self.CWD = os.getcwd()
        self.default_test_location = os.getcwd() + "data/mp3/streamers/drk-audio.mp3"
        load_dotenv()

    def transcribe(self, audio_path: str) -> str:
        """
        For transcribing locally stored audio file paths to be sent to whisper transcription endpoint.

        :param audio_path:
        :return:
        """
        if not audio_path:
            full_mp3_path = self.default_test_location
        else:
            full_mp3_path = self.CWD + audio_path

        # Create an api client
        # TODO (ajanitshimanga): I'd like to change this to a client instance that can be passed in.
        # Change this to an OPENAPI_Client_getter?
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        # Load audio file
        audio_file = open(full_mp3_path, "rb")

        # Transcribe
        transcription = client.audio.transcriptions.create(
            model=self.MODEL_TYPE,
            file=audio_file
        )

        return transcription.text
