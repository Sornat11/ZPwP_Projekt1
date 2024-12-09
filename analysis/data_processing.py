import pandas as pd

def load_data(file_path):
    """Wczytuje dane z pliku CSV i zwraca DataFrame."""
    return pd.read_csv(file_path)

def preprocess_data(df):
    """Przekształca dane: dodaje kolumny, usuwa brakujące wartości."""
    df['MatchResult'] = df['FTR'].map({'H': 'Home Win', 'A': 'Away Win', 'D': 'Draw'})
    df.dropna(inplace=True)
    return df