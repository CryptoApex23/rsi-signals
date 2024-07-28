import os
import requests
import pandas as pd
import ta
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()
BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")
BYBIT_URL = "https://api.bybit.com/v5/"

# Load settings from settings.json
with open('settings.json') as f:
    settings = json.load(f)
    
INTERVAL_MINUTES = settings['interval_minutes']

def get_bybit_klines(symbol, interval, limit=200):
    url = f'{BYBIT_URL}market/kline?category=spot&symbol={symbol}&interval={interval}&limit={limit}'
    response = requests.get(url)
    data = response.json()['result']['list']

    df = pd.DataFrame(data, columns=[
        'startTime', 'openPrice', 'highPrice', 'lowPrice', 'closePrice', 
        'volume', 'turnover'
    ])
    df['startTime'] = df['startTime'].astype(int)  # Explicitly cast to int
    df['timestamp'] = pd.to_datetime(df['startTime'], unit='ms')
    df.set_index('timestamp', inplace=True)
    df['close'] = df['closePrice'].astype(float)
    return df

def calculate_rsi(symbol):
    df = get_bybit_klines(symbol, INTERVAL_MINUTES)
    rsi = ta.momentum.RSIIndicator(df['close'], window=14)
    return rsi.rsi().iloc[-1]

def get_coins_rsi(coins):
    """Get the 15-minute RSI for a list of coins."""
    rsi_values = {}
    for coin in coins:
        try:
            rsi_values[coin] = calculate_rsi(coin)
        except Exception as e:
            rsi_values[coin] = f"Error: {str(e)}"  # Improved error handling
    return rsi_values





