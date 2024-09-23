from schemas.storage.DataStore import DataStore
from schemas.transcription.Transcriber import Transcriber


class TranscriptionService:
    def __init__(self, transcriber: Transcriber, storage_service: DataStore):
        self.transcription_strategy = transcriber
        self.persistence_service = storage_service

    def transcribe(self, mp3_path: str) -> None:
        """
        Generates a transcript from an mp3 audio file at (mp3_path) and persists the log via persistence_service.
        :return:
        """
        transcript = self.transcription_strategy.transcribe(mp3_path)
        self.persistence_service.store(transcript)
        return
