import os
import uuid


def write_content(content: str, file_name: str = None,
                  absolute_save_path: str = os.getcwd() + "/data/responses/") -> bool:
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


def load_content(absolute_file_path: str) -> str | None:
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
        return
    return content_to_classify


def list_files_in_folder(folder_path):
    """

    :param folder_path:
    :return:
    """
    # List to store full file paths
    file_paths = []

    # Walk through the directory
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Create full file path
            full_path = os.path.join(root, file)
            file_paths.append(full_path)
    return file_paths
