import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


def load_data() -> pd.DataFrame:
    """
    Generates imaginary data.

    In the real project I'll use real data to train the model.
    """
    np.random.seed(42)
    n_samples = 1000

    dados = {
        "desemprego": np.random.uniform(5, 15, n_samples),
        "evasao_escolar": np.random.uniform(2, 10, n_samples),
        "densidade_populacional": np.random.uniform(1000, 5000, n_samples),
        # a variável alvo: taxa de ocorrências (fortemente correlacionada com as acima)
        "taxa_criminalidade": np.random.uniform(0, 100, n_samples),
    }

    # criando abaixo uma correlação artificial para o modelo aprender
    dados["taxa_criminalidade"] += (dados["desemprego"] * 3) + (dados["evasao_escolar"] * 2)

    return pd.DataFrame(dados)


def train_model(df) -> RandomForestRegressor:
    print("Treinando o modelo Random Forest...")

    X = df[["desemprego", "evasao_escolar", "densidade_populacional"]]
    y = df["taxa_criminalidade"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    modelo = RandomForestRegressor(n_estimators=50, random_state=42)
    modelo.fit(X_train, y_train)

    score = modelo.score(X_test, y_test)
    print(f"Modelo treinado! R² Score: {score:.2f}")

    return modelo


def model() -> RandomForestRegressor:
    df_cidade = load_data()
    modelo_ml = train_model(df_cidade)

    return modelo_ml
