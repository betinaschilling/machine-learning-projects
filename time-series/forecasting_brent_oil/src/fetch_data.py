# src/fetch_data.py

import os
import requests
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()
API_KEY = os.getenv("EIA_API_KEY")

if not API_KEY:
    raise ValueError("A variável de ambiente EIA_API_KEY não está definida no .env")

def get_brent_data(save_path="data/brent_raw.csv"):
    base_url = "https://api.eia.gov/v2/petroleum/pri/spt/data/"
    params = {
        "api_key": API_KEY,
        "frequency": "daily",
        "data[0]": "value",
        "facets[product][]": "RBRTE",
        "sort[0][column]": "period",
        "sort[0][direction]": "asc"
    }

    print("🔁 Requisitando dados do Brent via EIA API v2 (correta)...")
    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        print(response.text)
        raise RuntimeError(f"Erro na API: {response.status_code}")

    data = response.json()
    records = data.get("response", {}).get("data", [])

    if not records:
        raise ValueError("Nenhum dado encontrado na resposta da API.")

    df = pd.DataFrame(records)
    df = df.rename(columns={"period": "date", "value": "price"})
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    Path(save_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(save_path, index=False)
    print(f"✅ Dados salvos em: {save_path}")

    return df

def current_date():
    raise NotImplementedError

def fetch_brent_prophet_format(api_key=API_KEY, start_date="1980-01-01", end_date="2025-01-01"):
    """
    Coleta dados do Brent da EIA no formato compatível com o Prophet (colunas: ds, y).
    Usa o código EPCBRENT (Europe Brent Spot Price FOB).
    """
    url = "https://api.eia.gov/v2/petroleum/pri/spt/data/"
    params = {
        'api_key': api_key,
        'facets[product][]': 'EPCBRENT',
        'data[]': 'value',
        'frequency': 'daily',
        'start': start_date,
        'end': end_date,
        'offset': 0
    }

    all_data = []
    print("🔁 Coletando dados paginados da EIA para Prophet...")

    while True:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(response.text)
            raise ConnectionError(f"Erro na requisição: Status Code {response.status_code}")

        data = response.json()
        brent_data = data.get('response', {}).get('data', [])
        if not brent_data:
            break

        all_data.extend(brent_data)

        if len(brent_data) < 500:
            break

        params['offset'] += 500

    if not all_data:
        raise ValueError("❌ Nenhum dado encontrado na resposta.")

    df = pd.DataFrame(all_data)
    df = df[['period', 'value']].rename(columns={'period': 'ds', 'value': 'y'})
    df['ds'] = pd.to_datetime(df['ds'])
    df['y'] = pd.to_numeric(df['y'], errors='coerce')
    df = df.dropna().sort_values('ds')

    print(f"✅ {len(df)} registros carregados com sucesso.")
    return df

if __name__ == "__main__":
    get_brent_data()
    # df_prophet = fetch_brent_prophet_format()