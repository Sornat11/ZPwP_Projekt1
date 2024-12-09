import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_analysis(data_splits):
    """
    Generuje analizy i wizualizacje na podstawie podzielonych danych.
    """
    figures = {}

    # Wspólne dane
    combined_data = pd.concat([data_splits["before_2000"], data_splits["after_2000"]])

    # Rozkład lat
    fig1, ax1 = plt.subplots()
    sns.histplot(combined_data["year"], bins=20, kde=True, ax=ax1)
    ax1.set_title("Rozkład meczów w latach")
    ax1.set_xlabel("Rok")
    ax1.set_ylabel("Liczba meczów")
    figures["Rozkład meczów"] = fig1

    # Liczba meczów drużyn (przykład analizy)
    if "team" in combined_data.columns:
        fig2, ax2 = plt.subplots()
        team_counts = combined_data["team"].value_counts().head(10)
        team_counts.plot(kind="bar", ax=ax2, color="skyblue")
        ax2.set_title("Top 10 drużyn z największą liczbą meczów")
        ax2.set_xlabel("Drużyna")
        ax2.set_ylabel("Liczba meczów")
        figures["Top 10 drużyn"] = fig2

    return figures
