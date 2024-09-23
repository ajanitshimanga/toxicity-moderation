from toxicitymoderation.ToxicityModerationService import ToxicityModerationService
from pydantic import BaseModel
import os
from fastapi import FastAPI
from fastapi import HTTPException

from utils import list_files_in_folder, write_content, load_content


class ToxicityModerationServiceProvider:
    DEFAULT_SERVICE_TYPE = "STANDARD_MODERATION_SERVICE"

    def __init__(self, service_type: str = DEFAULT_SERVICE_TYPE):
        self.service_selector = service_type

    def get_service(self):
        if self.service_selector == self.DEFAULT_SERVICE_TYPE:
            return ToxicityModerationService()
        if self.service_selector is None:
            return ValueError("")


app = FastAPI()
moderation_service = ToxicityModerationServiceProvider().get_service()
CWD = os.getcwd()
# CWD + /data/transcripts/toxic-communication-valorant.txt"
list_file_paths = CWD + "/data/transcripts/permissive"


class ToxicityDetectionInferenceRequest(BaseModel):
    user_text: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/inference/toxicity/")
def classify_toxic_conversation(request: ToxicityDetectionInferenceRequest):
    user_text = request.user_text

    if not user_text:
        raise HTTPException(status_code=400, detail="No user_text provided in request.")

    file_paths = list_files_in_folder(list_file_paths)
    print(file_paths)

    for file_path in file_paths:
        print("File Path: " + file_path)
        text = load_content(file_path)
        print(text)

        classification_response = moderation_service.classify_text(text)
        write_content(classification_response)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=False)
