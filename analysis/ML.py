from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


def prepare_data_for_ML(data, isPCA):
    data = data.dropna()
    y = data['GDP ($ per capita)']
    X = data.drop(['GDP ($ per capita)'], axis=1)
    X = X.fillna(0)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.fit_transform(X_test)

    if isPCA:
        pca = PCA(n_components=2)
        X_train = pca.fit_transform(X_train)
        X_test = pca.fit_transform(X_test)
    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def test_model(model, X_test, y_test):
    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    fraction = mae / y_test.mean()
    r2 = r2_score(y_test, y_pred)
    return mae, r2, fraction
