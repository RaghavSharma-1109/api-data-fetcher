from datetime import datetime
from api.fetcher import get_crypto_prices
from processor.data_cleaner import process_crypto_data
import os
CURRENCIES = {
    'usd': '$',
    'inr': '₹',
    'eur': '€',
    'jpy': '¥' ,
    'gbp': '£',
}
def price_formating(currencies):
    for price in currencies:
        symbol = CURRENCIES.get(price,"")
        if symbol:
            print(f"{price.upper()}: {symbol}{currencies[price]}")
        else:
            print(f"{price.upper()}: {currencies[price]}")
def clean_keys(keys:list):
    cleaned_list = []
    for key in keys:
        if key.strip() == '':
            continue
        cleaned_list.append(key.strip())
    return cleaned_list


def main():
    coins = input("Enter Crypto coins: ").lower().split(",")
    cleaned_coins = clean_keys(coins)
    currencies = input("Enter Exchange currencies: ").lower().split(",")
    cleaned_currencies = clean_keys(currencies)
    final_currencies = ",".join(cleaned_currencies)
    # FETCHER CALL
    raw_data = get_crypto_prices(cleaned_coins,final_currencies)
    final_output = process_crypto_data(raw_data,cleaned_coins,cleaned_currencies)
    # print(final_output)
    if final_output is None:
        print("Something went wrong while fetching data !!")
    elif final_output == {}:
        print("No valid crypto data found!!; recheck input fields.")
    else:
        timestamp = datetime.now()
        timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Time: {timestamp}\n")
        filepath = input("Enter filepath: ")
        if not os.path.exists(filepath) or not os.path.getsize(filepath):
            need_header = True
        elif os.path.exists(filepath) and not os.path.getsize(filepath):
            need_header = False
        if need_header:
            with open(filepath,"a") as file:
                file.write("coin,currency,price,timestamps\n")
            for coin in final_output.items():
                for currency in coin.items():
                    price = coin[currency]
                    file.write(f"{coin},{currency},{price},{timestamp}\n")
                


if __name__ == "__main__":  
    main()