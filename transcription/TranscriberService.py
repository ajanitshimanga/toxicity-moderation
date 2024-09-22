from schemas.storage.Storage import Storage
from schemas.transcription.Transcriber import Transcriber


class TranscriptionService:
    def __init__(self, transcription_strategy: Transcriber, persistence_service: Storage):
        self.transcription_strategy = transcription_strategy
        self.persistence_service = persistence_service

    def transcribe(self, mp3_path: str) -> None:
        """
        Generates a transcript from an mp3 audio file at (mp3_path) and persists the log via persistence_service.
        :return:
        """
        transcript = self.transcription_strategy.transcribe(mp3_path)
        self.persistence_service.store(transcript)
        return
