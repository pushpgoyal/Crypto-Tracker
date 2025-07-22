import requests
from db_config import connect_db
import time
import os
from dotenv import load_dotenv

load_dotenv()  

api_key = os.getenv("API_KEY")

all_coins = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=inr&order=market_cap_desc&per_page=150&page=1").json()
coin_ids = [coin['id'] for coin in all_coins]
coins = ",".join(coin_ids)

conn = connect_db()
cursor = conn.cursor()

cursor.execute("DELETE FROM CRYPTO WHERE timestamp < NOW() - INTERVAL 1 DAY")

while True:
    url = "https://api.coingecko.com/api/v3/simple/price" 

    params = {
        "ids": coins,
        "vs_currencies": "inr"
    }
    headers = {"x-cg-demo-api-key": api_key}

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        prices = response.json()
    except Exception as e:
        print("API error:", e)
        time.sleep(60)
        continue


    print(prices)

    for coin, info in prices.items():
        if 'inr' in info:
            price = info['inr']
            cursor.execute("INSERT INTO CRYPTO (COIN, PRICE) VALUES(%s, %s)", (coin, float(price)))
        else:
            print(f"Price for {coin} not available in INR.")
    conn.commit()
    time.sleep(60)

print("Data saved to DB!")

