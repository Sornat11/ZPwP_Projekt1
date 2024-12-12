import streamlit as st
from analysis.data_processing import load_data, clean_data
from analysis.analysis import calculate_statistics
from analysis.visualization import (
    plot_choropleth,
    plot_scatter,
    plot_boxplot,
    plot_avg_gdp,
    plot_gdp_histogram
    
)

# Zmiana tytułu strony i ikony
st.set_page_config(
    page_title="Analiza danych o krajach świata",
    page_icon="🌍",
    layout="wide",  # Poszerzenie szerokości strony
)

st.title("Kraje świata i ich charakterystyka - analiza🌍")

# Wczytanie danych
filepath = '../ZPwP_Projekt1/data/countries_of_the_world.csv'
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

    available_categories = {
    "Region": "Region",
    "Klimat": "Climate"
    }

    st.subheader("Średnie PKB na mieszkańca według wybranej kategorii")

    # Wybór kategorii przez użytkownika
    group_by = st.selectbox("Wybierz kategorię grupowania:", list(available_categories.keys()))

    # Wywołanie funkcji z odpowiednim parametrem
    group_by_column = available_categories[group_by]

    if group_by_column in data.columns:
        avg_gdp_fig = plot_avg_gdp(data, group_by_column, f"Średnie PKB na mieszkańca według {group_by}")
        st.plotly_chart(avg_gdp_fig)
        

    st.subheader("Histogram - Rozkład PKB na mieszkańca")
    # Lista dostępnych regionów
    all_regions = data['Region'].dropna().unique()

    # Wybór regionów przez użytkownika
    selected_regions = st.multiselect(
        "Wybierz regiony do wyświetlenia na histogramie:",
        options=all_regions,
        default=all_regions[:3]  # Domyślnie wybierz kilka pierwszych regionów
    )

    # Tworzenie histogramu dla wybranych regionów
    if selected_regions:
        gdp_histogram_fig = plot_gdp_histogram(data, selected_regions)
        st.plotly_chart(gdp_histogram_fig)
    else:
        st.warning("Wybierz przynajmniej jeden region, aby wyświetlić histogram.")


else:
    st.error("Nie udało się wczytać danych. Upewnij się, że plik istnieje.")
