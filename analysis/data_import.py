<<<<<<< HEAD
=======
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

print(f"Zestaw danych został pobrany do katalogu: {output_dir}")
>>>>>>> 48d7a7f (CHUJ WIE CO TU SIE DZIEJE)
