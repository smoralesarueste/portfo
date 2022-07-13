import pandas as pd
from datetime import datetime

def append_answer(filepath, data_dict): 
	data_dict["datetime"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	existing_df = pd.read_csv(filepath)
	existing_df = existing_df.append(data_dict, ignore_index = True)
	existing_df.to_csv(path_or_buf = filepath, sep = ",", index = False)
	return True