import requests
class CryptoAPI:
    def __init__(self,url) -> None:
        self.url = url
    def load_crypto_url(self,param):
        #calls api through url
        try: 
            response = requests.get(self.url,params=param)
            if response.status_code == 200:
                data = response.json()
                return data
            return None
        except Exception as e:
            print("API Failed:", e)
            return None
class CryptoProcessor:
    def __init__(self,data,currency) -> None:
        self.data = data
        self.currency = currency
    def process_crypto(self):
        if self.data is None:
            return None 
        cleaned_data = {}

        for coin in self.data:
            price = self.data.get(coin,{}).get(self.currency)
            if price is not None:
                cleaned_data[coin] = price
        if not cleaned_data:
            return None
        return cleaned_data
class CryptoDisplay():
    currencies = {
        'inr': "₹",
        'usd': '$',
        'eur': '€'
    }
    def __init__(self, cleaned_data,currency) -> None:
        self.data = cleaned_data
        self.currency = currency
    def display(self):
        if self.data is None:
            print("No data found!!")
            return None
        for coin in self.data:
            price = self.data[coin]

            print(f"{coin.capitalize()}: {CryptoDisplay.currencies.get(self.currency,'')}{price} {self.currency.upper()}")
            
def run_tracker(url,currency):
    print("Fetching Data....")
    load_data = CryptoAPI(url)
    raw_data = load_data.load_crypto_url(params)
    processed = CryptoProcessor(raw_data,currency)
    cleaned_data = processed.process_crypto()

    print("--- CRYPTO PRICE TRACKER ---")
    crypto = CryptoDisplay(cleaned_data,currency)
    crypto.display()
if __name__ == "__main__":
    url = 'https://api.coingecko.com/api/v3/simple/price'
    coins = input("Enter crypto coins: ").lower().split(",")
    cleaned_coins = []
    for coin in coins:
        if coin.strip() == "":
            continue
        cleaned_coins.append(coin.strip())
    final_coins = ",".join(cleaned_coins)
    currency = input("Enter exchange currency: ").lower()
    run_tracker(url,currency)