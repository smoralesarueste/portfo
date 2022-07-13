import pandas as pd
import os

from datetime import datetime
from pathlib import Path

def append_answer(filepath, data_dict):
        filepath = str(Path(os.path.realpath(__file__)).parent) + "/" + filepath
        data_dict["datetime"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        existing_df = pd.read_csv(filepath)
        existing_df = existing_df.append(data_dict, ignore_index = True)
        existing_df.to_csv(path_or_buf = filepath, sep = ",", index = False)
        return True