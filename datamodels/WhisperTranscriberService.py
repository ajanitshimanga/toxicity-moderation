import os

from openai import OpenAI
from dotenv import load_dotenv

from datamodels.TranscriberInterface import TranscriberInterface


class WhisperTranscriberService(TranscriberInterface):
    def __init__(self):

        self.location = os.getcwd() + "data/mp3/streamers/drk-audio.mp3"
        load_dotenv()

    def transcribe(self, audio_file_path: str) -> str:
        audio_file_path = self.location    # CHANGE LATER

        # Create an api client
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))    # Change this to an OPENAPI_Client_getter

        # Load audio file
        audio_file = open(audio_file_path, "rb")

        # Transcribe
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
        # Print the transcribed text
        print(transcription.text)
        return transcription.text
