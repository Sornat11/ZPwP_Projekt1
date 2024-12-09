<<<<<<< HEAD:analysis/data_import.py
=======


>>>>>>> d4158ae383238e53edfba28cd753999a4c107d60:EnglishPremierLeague.py
import kaggle


import os
from kaggle.api.kaggle_api_extended import KaggleApi
os.environ['KAGGLE_CONFIG_DIR'] = os.path.abspath("./kaggle/kaggle.json")

# Inicjalizacja API
api = KaggleApi()
api.authenticate()

# Pobranie zestawu danych
dataset = "saife245/english-premier-league"
output_dir = "data"
api.dataset_download_files(dataset, path=output_dir, unzip=True)

<<<<<<< HEAD:analysis/data_import.py
print(f"Zestaw danych został pobrany do katalogu: {output_dir}")
=======
print(f"Zestaw danych został pobrany do katalogu: {output_dir}")
>>>>>>> d4158ae383238e53edfba28cd753999a4c107d60:EnglishPremierLeague.py
