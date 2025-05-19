## ⛽ `forecasting_brent_oil`

Este projeto aplica técnicas de séries temporais para modelar e prever os preços do petróleo Brent, com foco em precisão preditiva, comparação de modelos e análise dos padrões sazonais e de volatilidade. Os dados são obtidos via APIs públicas e o estudo segue rigor acadêmico.

### 📌 Objetivos
- Construir um pipeline completo de previsão do preço do Brent.
- Comparar modelos clássicos (ARIMA, Prophet) e deep learning (LSTM).
- Avaliar desempenho em diferentes janelas de tempo e regimes de volatilidade.
- Investigar efeitos de choques externos e padrões sazonais.

### 🧱 Estrutura do Projeto
```
forecasting_brent_oil/
├── data/
│   └── brent_raw.csv
├── notebooks/
│   ├── 01_eda_visualization.ipynb
│   ├── 02_arima_model.ipynb
│   ├── 03_prophet_model.ipynb
│   ├── 04_lstm_model.ipynb
│   └── 05_model_comparison.ipynb
├── src/
│   ├── preprocessing.py
│   ├── modeling.py
│   └── evaluation.py
├── models/
│   └── saved_models/
└── README.md
```

### 🛠️ Modelos Aplicados
- **ARIMA / SARIMA**: Modelagem clássica de dependência temporal e sazonalidade.
- **Prophet (Meta)**: Modelo estruturado para tendências e feriados.
- **LSTM (Keras/TensorFlow)**: Rede neural recorrente para captura de longas dependências.

### 📈 Avaliação de Desempenho
- Métricas: RMSE, MAE, MAPE, sMAPE
- Backtesting com janelas deslizantes
- Visualizações: Forecast plot, residuals, distribuição dos erros

### 🧪 Experimentos Extras
- Transformações de séries: log, diff, z-score
- Teste de estacionariedade (ADF, KPSS)
- Análise de impacto de eventos exógenos (ex: OPEP, guerra, pandemia)

### 🔍 Referências e Dados
- Fonte de dados: [EIA API](https://www.eia.gov/opendata/) ou Yahoo Finance (`yfinance`)
- Referências teóricas:
  - Hyndman & Athanasopoulos (2021) - *Forecasting: Principles and Practice*
  - Brownlee (2020) - *Deep Learning for Time Series Forecasting*
