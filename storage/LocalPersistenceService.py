import os
import uuid

from schemas.storage.Storage import Storage


class LocalStorageService(Storage):

    LOCAL_STORAGE_AFFIX = "/data/transcripts"

    def __init__(self):
        self.location = os.getcwd() + self.LOCAL_STORAGE_AFFIX

    def store(self, text: str) -> str:
        text += "\n"
        text_uuid = uuid.uuid4().hex

        path = os.path.join(self.location, text_uuid)
        with open(path, 'w') as file:
            file.write(text)
        return str(path)
