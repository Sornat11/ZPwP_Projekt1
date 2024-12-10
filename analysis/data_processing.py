import pandas as pd

def load_data(filepath):
    """
    Wczytuje dane z lokalnego pliku CSV.
    """
    try:
        data = pd.read_csv(filepath)
        return data
    except FileNotFoundError:
        print(f"Plik {filepath} nie został znaleziony.")
        return None
    except Exception as e:
        print(f"Wystąpił błąd podczas wczytywania pliku: {e}")
        return None


def clean_data(data):
    data.columns = data.columns.str.strip()  # Usuwanie spacji z nazw kolumn
    return data