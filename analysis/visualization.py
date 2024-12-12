import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd

def plot_choropleth(data):
    """Tworzy mapę świata z gęstością populacji."""

    fig = px.choropleth(
        data,
        locations="Country",
        locationmode="country names",
        color="Pop. Density (per sq. mi.)",
        hover_name="Country",
        color_continuous_scale="Reds",
        range_color=(0, 200)
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
        log_y=True,
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

def plot_gdp_histogram(data):
    """Tworzy histogram PKB na mieszkańca."""
    fig = px.histogram(data, x="GDP ($ per capita)", nbins=50, color="Region")
    return fig

def plot_avg_gdp(data, group_by_column, title):
    """Tworzy wykres słupkowy średniego PKB na mieszkańca według wybranej kategorii."""
    avg_gdp = data.groupby(group_by_column)["GDP ($ per capita)"].mean().reset_index()
    fig = px.bar(avg_gdp, x=group_by_column, y="GDP ($ per capita)", title=title, color=group_by_column)
    return fig
