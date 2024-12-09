import pandas as pd

def process_data(filepath):
    """
    Przetwarza dane: ładuje plik CSV i dzieli dane na podstawie roku (przed 2000 i od 2000).
    """
    data = pd.read_csv(filepath)

    # Upewnienie się, że kolumna 'Date' istnieje
    if "Date" not in data.columns:
        raise ValueError("Kolumna 'Date' nie istnieje w danych.")
    
    data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%y')
    data['Year'] = data['Date'].dt.year

    # Podział danych na podstawie roku
    median_year = data['Date'].median()
    before_2000 = data[data["Date"] < median_year]
    after_2000 = data[data["Date"] >= median_year]

    return {
        "before_2000": before_2000,
        "after_2000": after_2000,
    }