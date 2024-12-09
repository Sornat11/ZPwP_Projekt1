import streamlit as st
import pandas as pd
from data_fetcher import fetch_data
from data_processing import process_data
from analysis import generate_analysis

# Tytuł aplikacji
st.title("Analiza danych English Premier League")

# Sekcja ładowania danych
st.header("Pobieranie danych")
data_dir = "data"  # Katalog na dane
dataset_name = "final_dataset"

st.write("Pobieranie danych z API Kaggle...")
try:
    csv_path = fetch_data(dataset_name, data_dir)
    st.success("Dane zostały pobrane.")
except Exception as e:
    st.error(f"Błąd podczas pobierania danych: {e}")
    st.stop()

# Wczytywanie i przetwarzanie danych
st.header("Przetwarzanie danych")
try:
    data_splits = process_data(csv_path)
    st.success("Dane zostały przetworzone.")
except Exception as e:
    st.error(f"Błąd podczas przetwarzania danych: {e}")
    st.stop()

# Wyświetlenie podzielonych danych
st.subheader("Dane podzielone na podstawie roku")
st.write("**Dane przed rokiem 2000:**")
st.dataframe(data_splits["before_2000"].head())
st.write("**Dane od roku 2000:**")
st.dataframe(data_splits["after_2000"].head())

# Analiza i wizualizacja
st.header("Analiza i wizualizacja danych")
figures = generate_analysis(data_splits)

for fig_title, fig in figures.items():
    st.subheader(fig_title)
    st.pyplot(fig)

