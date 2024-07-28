import schedule
import time
from rsi_calculator import get_coins_rsi
from bot_sender import send_message
import json
import os

with open('settings.json') as f:
    settings = json.load(f)
    
COINS = settings['coins']
CHECK_INTERVAL = settings['check_interval']
RSI_THRESHOLD = settings['rsi_threshold']

def job():
    rsi_values = get_coins_rsi(COINS)
    for coin, rsi in rsi_values.items():
        print(f"{coin}: {rsi}")
        if isinstance(rsi, float) and rsi < RSI_THRESHOLD:
            message = f"Alert: {coin} RSI is below 30!\nCurrent RSI: {rsi}"
            send_message(message)

def main():
    print(f'Bot is Started, Checking RSI every {CHECK_INTERVAL} Minutes')
    schedule.every(CHECK_INTERVAL).minutes.do(job)    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()