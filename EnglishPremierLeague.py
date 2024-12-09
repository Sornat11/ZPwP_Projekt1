

import kaggle



import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Inicjalizacja API
api = KaggleApi()
api.authenticate()

import kagglehub

# Download latest version
path = kagglehub.dataset_download("saife245/english-premier-league")

print("Path to dataset files:", path)