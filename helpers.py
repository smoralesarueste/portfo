import pandas as pd
import os, requests

from datetime import datetime
from pathlib import Path

def append_answer(filepath, data_dict):
        filepath = str(Path(os.path.realpath(__file__)).parent) + "/" + filepath
        data_dict["datetime"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        existing_df = pd.read_csv(filepath)
        existing_df = existing_df.append(data_dict, ignore_index = True)
        existing_df.to_csv(path_or_buf = filepath, sep = ",", index = False)
        return True

def send_email(data):

        return requests.post(
        "https://api.mailgun.net/v3/https://api.mailgun.net/v3/sandbox3d0117fcadc74e07ab1d630ca45d490f.mailgun.org/messages",
        auth=("api", "ef8ab09ac600e5aa22698a226391c195-18e06deb-a9b9a04e"),
        data={"from": f"Excited User <{os.environ['USER']}>",
                "to": f"Excited User <{os.environ['USER']}>",
                "subject": "New form answer from Web Page!",
                "text": str(data)})