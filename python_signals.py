import schedule
import time
from rsi_calculator import get_coins_rsi
from bot_sender import send_message

COINS = ['TONUSDT','BTCUSDT','ETHUSDT']

def job():
    rsi_values = get_coins_rsi(COINS)
    for coin, rsi in rsi_values.items():
        print(f"{coin}: {rsi}")
        if isinstance(rsi, float) and rsi < 30:
            message = f"Alert: {coin} RSI is below 30!\nCurrent RSI: {rsi}"
            send_message(message)

def main():
    schedule.every(15).minutes.do(job)    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()