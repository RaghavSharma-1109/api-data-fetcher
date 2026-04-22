import requests
def get_crypto_prices(coins:list,currency):
    url = "https://api.coingecko.com/api/v3/simple/price"
    cleaned_coins = []
    for coin in coins:
        cleaned_coins.append(coin.strip())
    final_coin = ",".join(cleaned_coins)
    url += f"?ids={final_coin}&vs_currencies={currency.strip()}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        return None
    except Exception as e:
        print("API FAILED!! ", e)
        return None
if __name__ == "__main__":
    coins = input("Enter cryptocoins: ").lower().split(',')
    currency = input("Enter exchange currency: ")
    get_crypto_prices(coins,currency)