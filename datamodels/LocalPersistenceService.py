import os
import uuid


from datamodels.StorageInterface import StorageInterface


class LocalStorageService(StorageInterface):
    def __init__(self):
        self.location = os.getcwd() + "/data/transcripts"

    def store(self, text: str) -> None:
        text = text + "\n"
        text_uuid = uuid.uuid4().hex
        with open(os.path.join(self.location, text_uuid), 'w') as file:
            file.write(text)
        return
