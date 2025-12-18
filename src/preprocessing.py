import pandas as pd
from pathlib import Path

def load_and_check(path):
    data = pd.read_csv(path)
    data["Date"] = pd.to_datetime(data["Date"])
    informacion_nulos = data.isnull().sum()
    print(f"columnassss {data.columns}")
    print(data.head())
    print(f"cantidad nulos por columna: \n{informacion_nulos}")
    print(f"forma: {data.shape}")
    print(f"estadisticas: \n {data.describe()}")
    print(f"informacion importante : \n")
    data.info()
    return data




path = Path('data/csv/SPY.csv')
load_and_check(path)
