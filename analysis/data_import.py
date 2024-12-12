# import os
# from kaggle.api.kaggle_api_extended import KaggleApi

# def fetch_data(dataset_name, output_dir):
#     """
#     Pobiera dane z API Kaggle i zapisuje je w katalogu output_dir.
#     """
#     api = KaggleApi()
#     api.authenticate()

#     # Tworzenie katalogu, jeśli nie istnieje
#     os.makedirs(output_dir, exist_ok=True)

#     # Pobieranie i rozpakowywanie danych
#     api.dataset_download_files(dataset_name, path=output_dir, unzip=True)

#     # Szukanie pliku CSV
#     for file in os.listdir(output_dir):
#         if file.endswith(".csv"):
#             return os.path.join(output_dir, file)

#     raise FileNotFoundError("Nie znaleziono pliku CSV w pobranych danych.")