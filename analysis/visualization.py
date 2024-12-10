import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


def plot_choropleth(data):
    """Tworzy mapę świata z gęstością populacji."""
    fig = px.choropleth(
        data,
        locations="Country",
        locationmode="country names",
        color="Pop. Density (per sq. mi.)",
        hover_name="Country",
        color_continuous_scale="Viridis",
    )
    return fig


def plot_scatter(data):
    """Tworzy wykres rozrzutu PKB vs gęstość populacji."""
    fig = px.scatter(
        data,
        x="GDP ($ per capita)",
        y="Pop. Density (per sq. mi.)",
        color="Region",
        hover_name="Country",
        log_x=True,
        size="Population",
    )
    return fig


def plot_boxplot(data):
    """Tworzy wykres pudełkowy gęstości populacji dla regionów."""
    fig = px.box(
        data,
        x="Region",
        y="Pop. Density (per sq. mi.)",
        color="Region",
        log_y=True,
    )
    return fig



