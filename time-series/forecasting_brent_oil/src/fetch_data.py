# src/fetch_data.py

import yfinance as yf
import pandas as pd
from pathlib import Path

def get_brent_data(start="2010-01-01", end=None, save_path="data/brent_raw.csv"):
    """
    Baixa os dados históricos do petróleo Brent via yfinance e salva em CSV.

    Args:
        start (str): Data de início no formato 'YYYY-MM-DD'
        end (str or None): Data final. Se None, usa a data atual.
        save_path (str): Caminho do arquivo de saída CSV
    """
    ticker = yf.Ticker("BZ=F")
    df = ticker.history(start=start, end=end)

    if df.empty:
        raise ValueError("Nenhum dado retornado. Verifique o ticker ou as datas.")

    df.reset_index(inplace=True)
    df = df[["Date", "Open", "High", "Low", "Close", "Volume"]]
    df.columns = [c.lower() for c in df.columns]

    Path(save_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(save_path, index=False)

    print(f"Dados salvos em: {save_path}")
    return df

if __name__ == "__main__":
    get_brent_data()
