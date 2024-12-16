def calculate_statistics(data):
    """Zwraca podstawowe statystyki opisowe."""
    return data.describe()


def calculate_corr_matrix(data):
    correlation_matrix = data.corr()
    return correlation_matrix
