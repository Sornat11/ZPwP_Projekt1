import streamlit as st
from analysis.data_processing import load_data, clean_data, select_cols
from analysis.analysis import (calculate_statistics, calculate_corr_matrix)
from analysis.visualization import (
    plot_choropleth,
    plot_scatter,
    plot_boxplot,
    plot_avg_gdp,
    plot_gdp_histogram,
    plot_correlation
)
from analysis.ML import prepare_data_for_ML, train_model, test_model

# Zmiana tytułu strony i ikony
st.set_page_config(
    page_title="Analiza danych o krajach świata",
    page_icon="🌍",
    layout="wide",  # Poszerzenie szerokości strony
)

st.title("Kraje świata i ich charakterystyka - analiza🌍")

# Wczytanie danych
filepath = 'ZPwP_Projekt1\data\countries_of_the_world.csv'
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
    group_by = st.selectbox("Wybierz kategorię grupowania:",
                            list(available_categories.keys()))

    # Wywołanie funkcji z odpowiednim parametrem
    group_by_column = available_categories[group_by]

    if group_by_column in data.columns:
        avg_gdp_fig = plot_avg_gdp(
            data, group_by_column, f"Średnie PKB na mieszkańca według {group_by}")
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

    st.subheader(
        "Próba predykcji PKB per capita na podstawie zmiennych objaśniających")
    st.text("Zbadanie dokładności predykcji pozwoli odpowiedzieć na pytanie, " +
            "czy pozostałe czynniki mają wpływ na zmienną objaśnianą, oraz czy można dzięki nim oszacować" +
            " jakie jest PKB per capita danego kraju. "
            + "Pierwszym krokiem będzie odrzucenie zmiennych Country oraz Region i zbadanie korelacji pozostałych zmiennych")
    data = data.drop(["Country", "Region"], axis=1)
    corr_matrix = calculate_corr_matrix(data)
    corr_chart = plot_correlation(corr_matrix)
    st.plotly_chart(corr_chart)

    st.text("Następnie spośród zmiennych objaśniających wybrane zostały te, których korelacja ze zmienną objaśnianą" +
            "jest większa niż 0.35 lub mniejsza niż -0.35. Były to: ")
    st.write(
        """ 
        - Net Migration
        - Infant mortality (per 1000 births)
        - Literacy (%)
        - Phones (per 1000)
        - Birthrate
        - Agriculture
        - Service
        """
    )
    st.text("Macierz korelacji dla pozostałych zmiennych prezentuje się następująco:")
    MLData = select_cols(data)
    MLcols_corr = calculate_corr_matrix(MLData)
    MLcorr_chart = plot_correlation(MLcols_corr)
    st.plotly_chart(MLcorr_chart)

    st.text("Problemem może być wysoka wzajemna korelacja zmiennych objaśniających - zostanie on rozwiązany dzięki metodzie PCA. "
            + "Najpierw jednak dane zostały podzielone na zbiór uczący i testowy w stosunku 4:1 oraz poddane standaryzacji." +
            "Następnie na zbiorze uczącym został wytrenowany model regresji liniowej. Dla zbioru testowego osiąga on następujące wyniki:")

    X_train, X_test, y_train, y_test = prepare_data_for_ML(MLData, isPCA=True)
    model = train_model(X_train, y_train)
    mae, r2, fraction = test_model(model, X_test, y_test)
    st.text(f"Średni błąd bezwzględny: {round(mae,2 )}")
    st.text(f"Współczynnik R kwadrat: {round(r2,3)}")
    st.text(f"MAE względem średniego PKB: {round(fraction,3)}")

    st.text("Wyniki nie są zadowalające - prawdopodobną przyczyną jest niepoprawne zastosowanie metody PCA." +
            "Model zostanie zbudowany ponownie - tym razem bez wykorzystania tej metody.")

    X_train, X_test, y_train, y_test = prepare_data_for_ML(MLData, isPCA=False)
    model = train_model(X_train, y_train)
    mae, r2, fraction = test_model(model, X_test, y_test)
    st.text(f"Średni błąd bezwzględny: {round(mae,2)}")
    st.text(f"Współczynnik R kwadrat: {round(r2,3)}")
    st.text(f"MAE względem średniego PKB: {round(fraction,3)}")
else:
    st.error("Nie udało się wczytać danych. Upewnij się, że plik istnieje.")
