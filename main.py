import streamlit as st
from analysis.data_processing import load_data, preprocess_data
from analysis.analysis import calculate_win_statistics
from analysis.visualization import plot_match_results

# Ustawienia strony
st.set_page_config(
    page_title="Analiza wyników Premier League",
    page_icon="⚽"
)

st.title("Analiza wyników Premier League")

# Wczytywanie i przetwarzanie danych
file_path = "../ZPwP_Projekt1/ZPwP_Projekt1/data/EPL01-22.csv"
data = load_data(file_path)
data = preprocess_data(data)

st.header("Podgląd danych")
st.write(data.head())

# Analiza
st.header("Statystyki wyników meczów")
stats = calculate_win_statistics(data)
st.write(stats)

# Wizualizacja
st.header("Wizualizacja wyników")
fig = plot_match_results(stats)
st.plotly_chart(fig)