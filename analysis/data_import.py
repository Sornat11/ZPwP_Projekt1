<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 9f6dd27a1f426076884159a98d864abb7e80fa0d
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
<<<<<<< HEAD
>>>>>>> 48d7a7f (CHUJ WIE CO TU SIE DZIEJE)
=======
>>>>>>> 9f6dd27a1f426076884159a98d864abb7e80fa0d
