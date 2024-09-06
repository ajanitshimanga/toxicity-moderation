from datamodels.ToxicityModerationService import ToxicityModerationService, load_content, write_content

from datamodels.LocalPersistenceService import LocalStorageService
from datamodels.WhisperTranscriberService import WhisperTranscriberService
import os


def list_files_in_folder(folder_path):
    # List to store full file paths
    file_paths = []

    # Walk through the directory
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Create full file path
            full_path = os.path.join(root, file)
            file_paths.append(full_path)

    return file_paths


if __name__ == '__main__':
    moderation_service = ToxicityModerationService()

    # "/Users/eren/personal-projects/toxicity-moderation/data/transcripts/toxic-communication-valorant.txt"
    list_file_paths = "//data/transcripts/permissive/"
    file_paths = list_files_in_folder(list_file_paths)
    print(file_paths)

    for file_path in file_paths:
        print("File Path: " + file_path)
        text = load_content(file_path)
        print(text)

        classification_response = moderation_service.classify_text(text)
        write_content(classification_response)
