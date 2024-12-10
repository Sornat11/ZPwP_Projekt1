import streamlit as st
from analysis.data_processing import load_data, clean_data
from analysis.analysis import calculate_statistics
from analysis.visualization import (
    plot_choropleth,
    plot_scatter,
    plot_boxplot,
)

# Zmiana tytułu strony i ikony
st.set_page_config(
    page_title="Analiza danych o krajach świata",
    page_icon="🌍",
    layout="wide",  # Poszerzenie szerokości strony
)

st.title("Kraje świata i ich charakterystyka - analiza🌍")

# Wczytanie danych
filepath = 'C:/Users/Sornat/Desktop/ZPwP_Projekt1/ZPwP_Projekt1/data/countries_of_the_world.csv'
data = load_data(filepath)

if data is not None:
    clean_data(data)

    st.subheader("Prezentacja danych")
    st.dataframe(data)

    # Analiza danych
    st.subheader("Podstawowe statystyki")
    stats = calculate_statistics(data)
    st.write(stats)

    # Wizualizacje
    st.subheader("Mapa świata - gęstość populacji")
    choropleth_fig = plot_choropleth(data)
    st.plotly_chart(choropleth_fig)

    st.subheader("Wykres rozrzutu - PKB vs gęstość populacji")
    scatter_fig = plot_scatter(data)
    st.plotly_chart(scatter_fig)

    st.subheader("Wykres pudełkowy - gęstość populacji w regionach")
    boxplot_fig = plot_boxplot(data)
    st.plotly_chart(boxplot_fig)


else:
    st.error("Nie udało się wczytać danych. Upewnij się, że plik istnieje.")
