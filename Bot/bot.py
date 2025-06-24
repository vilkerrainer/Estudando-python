import ccxt
import pandas as pd
from ta.momentum import RSIIndicator
import time
import datetime
import os

# ========= CONFIGURAÇÃO KEYS =========
API_KEY = '0rkeBKavD8LOVzxQJU8SUQS6bmd9Jtd7vwcJpwr7M0n0a7estL9epOT4oXDX5z2Y'
API_SECRET = '6tmGrxpsPbfM41oS67kAWRFQgQRSw6WVEKTxrcNpWe4AFnrzb6QRzYukJtABKoar'

# ========== CONFIGURAÇÕES ==========
cripto = 'PEPE'
tempo_minutos = 15
symbol = f'{cripto}/USDT'
timeframe = '1h'
capital_usdt = 1.5
rsi_compra = 40
rsi_venda = 55
min_quantidade = 5  # Quantidade mínima de cripto para vender

# ========== CONEXÃO COM A BINANCE ==========
exchange = ccxt.binance({
    'apiKey': API_KEY,
    'secret': API_SECRET,
    'enableRateLimit': True,
})

# ========== FUNÇÕES ==========

def pegar_min_notional():
    market = exchange.load_markets()[symbol]
    return market['limits']['cost']['min']

def buscar_dados():
    dados = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=100)
    df = pd.DataFrame(dados, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    return df

def calcular_rsi(df, periodo=14):
    indicador = RSIIndicator(df['close'], window=periodo)
    df['rsi'] = indicador.rsi()
    return df

def pegar_saldos():
    saldo = exchange.fetch_balance()
    return saldo['USDT']['free'], saldo[cripto]['free']

def comprar_cripto(usdt, data_hora):
    preco = exchange.fetch_ticker(symbol)['ask']
    quantidade = round(usdt / preco, 2)
    ordem = exchange.create_market_buy_order(symbol, quantidade)
    msg = f"{data_hora} ✅ COMPRA: {quantidade} {cripto} por {usdt:.2f} USDT (preço: {preco:.6f})"
    print(msg)
    with open("Bot/compra.txt", "a", encoding="utf-8") as f:
        f.write(msg + "\n")
    return ordem

def vender_cripto(quantidade, data_hora):
    preco = exchange.fetch_ticker(symbol)['bid']
    quantidade = round(quantidade, 2)
    ordem = exchange.create_market_sell_order(symbol, quantidade)
    msg = f"{data_hora} ✅ VENDA: {quantidade} {cripto} (preço: {preco:.6f})"
    print(msg)
    with open("Bot/venda.txt", "a", encoding="utf-8") as f:
        f.write(msg + "\n")
    return ordem

# ========== LOOP DO BOT ==========
os.makedirs("Bot", exist_ok=True)

while True:
    try:
        data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        df = buscar_dados()
        df = calcular_rsi(df)
        rsi = df['rsi'].iloc[-1]
        usdt, cripto_saldo = pegar_saldos()
        preco = exchange.fetch_ticker(symbol)['ask']
        min_notional = pegar_min_notional()
        
        quantidade = int((capital_usdt / preco) * 100) / 100  # Calcula e trunca
        valor_efetivo = quantidade * preco

        log = f"{data_hora} | RSI: {rsi:.2f} | USDT: {usdt:.2f} | {cripto}: {cripto_saldo:.2f} | minNotional: {min_notional:.4f}"
        print(log)
        with open("Bot/log.txt", "a", encoding="utf-8") as f:
            f.write(log + "\n")

        # COMPRA
        if rsi < rsi_compra:
            if usdt >= capital_usdt and valor_efetivo >= min_notional and quantidade > 0:
                try:
                    comprar_cripto(capital_usdt, data_hora)
                except Exception as e:
                    print(f"{data_hora} ⚠️ Erro ao tentar comprar: {e}")
            else:
                print(f"{data_hora} ⚠️ Compra ignorada. Saldo insuficiente (${usdt:.2f}) ou valor efetivo muito baixo (${valor_efetivo:.6f}).")

        # VENDA
        if rsi > rsi_venda:
            preco_venda = exchange.fetch_ticker(symbol)['bid']
            valor_efetivo_venda = cripto_saldo * preco_venda

            if cripto_saldo >= min_quantidade and valor_efetivo_venda >= min_notional:
                try:
                    vender_cripto(cripto_saldo, data_hora)
                except Exception as e:
                    print(f"{data_hora} ⚠️ Erro ao tentar vender: {e}")
            else:
                print(f"{data_hora} ⚠️ Venda ignorada. Valor insuficiente ({valor_efetivo_venda:.4f} < {min_notional}) ou saldo muito baixo ({cripto_saldo:.4f} < {min_quantidade}).")

    except Exception as e:
        print("⚠️ Erro:", e)

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
