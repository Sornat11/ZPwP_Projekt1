# Analiza danych ekonomicznych i predykcja PKB per capita

Projekt obejmuje analizę danych ekonomicznych oraz budowę modelu regresji liniowej do przewidywania PKB per capita na podstawie wybranych wskaźników.

## 📋 Opis
- Wczytuje i czyści dane z pliku CSV.
- Generuje statystyki opisowe i macierz korelacji.
- Wytwarza interaktywne wykresy przydate w procesie analizy danych
- Przygotowuje dane do uczenia maszynowego (w tym opcjonalną redukcję wymiarowości PCA).
- Trenuje i testuje model regresji liniowej.
- Oblicza metryki oceny: MAE, R² oraz błąd względny.

## 🛠 Wymagania
- Python 3.8+
- Zainstalowane zależności z `requirements.txt`

## 📥 Instalacja
1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/twoja_nazwa_użytkownika/nazwa_repo.git
   cd nazwa_repo
   ```

2. Zainstaluj zależności:
    ```bash
    pip install -r requirements.txt
    ```

3. Uruchom główny skrypt:
    ```bash
    python main.py
    ```