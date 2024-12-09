def calculate_win_statistics(df):
    """Oblicza statystyki wygranych drużyn domowych i wyjazdowych."""
    home_wins = df[df['FTR'] == 'H'].shape[0]
    away_wins = df[df['FTR'] == 'A'].shape[0]
    draws = df[df['FTR'] == 'D'].shape[0]
    return {"Home Wins": home_wins, "Away Wins": away_wins, "Draws": draws}