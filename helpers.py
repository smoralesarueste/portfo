
from pathlib import Path
from datetime import datetime

import os

BASE_FOLDER = Path(os.path.realpath(__file__)).parent


def append_answer(file_path:str, data: dict): 
	target_path = str(BASE_FOLDER) + "/" + file_path

	new_line = "\n" + ",".join(["'" + str(val).replace("'", '"') + "'" for val in data.values()] + ["'" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "'"])

	with open(target_path, "a") as file: 
		file.write(new_line)
	return True