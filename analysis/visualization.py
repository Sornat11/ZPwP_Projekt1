import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def plot_match_results(stats):
    """Generuje wykres słupkowy wyników meczu."""
    fig = px.bar(
        x=list(stats.keys()),
        y=list(stats.values()),
        labels={'x': 'Result Type', 'y': 'Count'},
        title='Match Results Statistics'
    )
    return fig