import ccxt
import pandas as pd
from ta.momentum import RSIIndicator
import datetime
import os

# ========= CONFIGURAÇÕES ==========
symbol = 'DOGE/USDT'         # Par desejado
timeframe = '1h'             # Candles de 1h
periodo_rsi = 14
dias_lookback = 30           # Últimos 30 dias
exchange = ccxt.binance()

# ========= CRIAR PASTA ==========
os.makedirs("Bot", exist_ok=True)

# ========= FUNÇÃO ==========
def calcular_rsi_ultimos_30_dias(symbol):
    agora = exchange.milliseconds()
    um_dia_ms = 24 * 60 * 60 * 1000
    desde = agora - dias_lookback * um_dia_ms

    print(f"⏳ Baixando dados desde: {datetime.datetime.fromtimestamp(desde / 1000)}")

    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, since=desde, limit=1000)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')

    # Filtra apenas candles nos minutos múltiplos de 15
    df = df[df['datetime'].dt.minute.isin([0, 15, 30, 45])].reset_index(drop=True)

    rsi_indicator = RSIIndicator(df['close'], window=periodo_rsi)
    df['rsi'] = rsi_indicator.rsi()

    df = df.dropna(subset=['rsi'])

    # Escreve em log3.txt
    with open("Bot/log3.txt", "w", encoding="utf-8") as f:
        for _, row in df.iterrows():
            linha = f"{row['datetime'].strftime('%d/%m/%Y %H:%M')} | RSI: {row['rsi']:.2f}"
            f.write(linha + "\n")

    print(f"✅ Dados salvos em Bot/log3.txt")

# ========= EXECUTAR ==========
calcular_rsi_ultimos_30_dias(symbol)
