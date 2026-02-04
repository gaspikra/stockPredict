from pathlib import Path

path = Path("data/csv")
def descargar_datos(nombre_ticker, period_selected, path):
    import yfinance as yf

    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)

    VALID_PERIODS = [
    '1d', '5d', 
    '1mo', '3mo', '6mo', 
    '1y', '2y', '5y', '15y', 
    'ytd', 'max'
]
    if(period_selected not in VALID_PERIODS):
        raise ValueError(f"Periodo inválido: '{period_selected}'. Opciones: {VALID_PERIODS}")
    if isinstance(nombre_ticker, list):
        for ticker in nombre_ticker:
            data = yf.download(ticker,period = period_selected, auto_adjust= False)
            data.columns = data.columns.droplevel('Ticker')
            data.columns.name = None
            guardar_csv(path, ticker, data)
    else:
        data = yf.download(nombre_ticker,period = period_selected, auto_adjust= False)
        data.columns = data.columns.droplevel('Ticker')
        data.columns.name = None
        guardar_csv(path,nombre_ticker,data)

def guardar_csv(path, nombre_ticker, data):
     try:
        archivo_destino = path / f"{nombre_ticker}.csv"
        data.to_csv(archivo_destino)
     except Exception as e:
         print(f"error procesando:{nombre_ticker}: {e}")
         
descargar_datos('SPY', '15y', path)