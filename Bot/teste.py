import ccxt
import pandas as pd
from ta.momentum import RSIIndicator
import datetime
import time
import os

# ========== CONFIGURAÇÕES ==========
tempo_minutos = 15
timeframe = '1h'
limite_rsi = 100  # Número de candles para RSI
valor_max_notional = 2.0

# ========== FUNÇÕES ==========

def buscar_pares_baratos():
    exchange = ccxt.binance()
    markets = exchange.load_markets()
    pares = []
    for symbol in markets:
        if symbol.endswith('/USDT') and 'limits' in markets[symbol]:
            try:
                min_notional = markets[symbol]['limits']['cost']['min']
                if min_notional is not None and min_notional < valor_max_notional:
                    pares.append(symbol)
            except:
                continue
    return pares

def calcular_rsi(exchange, symbol, timeframe='1h', periodo=14):
    try:
        dados = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limite_rsi)
        df = pd.DataFrame(dados, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        indicador = RSIIndicator(df['close'], window=periodo)
        df['rsi'] = indicador.rsi()
        return df['rsi'].iloc[-1]
    except Exception as e:
        print(f"Erro ao calcular RSI para {symbol}: {e}")
        return None

# ========== LOOP DO BOT ==========

os.makedirs("Bot", exist_ok=True)

exchange = ccxt.binance()

while True:
    try:
        data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        pares = buscar_pares_baratos()

        for symbol in pares:
            rsi = calcular_rsi(exchange, symbol, timeframe)
            if rsi is not None:
                linha = f"{data_hora} | {symbol} | RSI: {rsi:.2f}"
                print(linha)
                with open("Bot/log2.txt", "a", encoding="utf-8") as f:
                    f.write(linha + "\n")

    except Exception as e:
        print("⚠️ Erro geral:", e)

    # Espera até o próximo múltiplo de tempo_minutos
    now = datetime.datetime.now()
    minuto_atual = now.minute
    proximo_multiplo = ((minuto_atual // tempo_minutos) + 1) * tempo_minutos
    if proximo_multiplo >= 60:
        proxima_execucao = (now + datetime.timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
    else:
        proxima_execucao = now.replace(minute=proximo_multiplo, second=0, microsecond=0)

    delay = (proxima_execucao - now).total_seconds()
    time.sleep(delay)
