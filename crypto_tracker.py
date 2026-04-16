import requests
class CryptoAPI:
    def __init__(self,url) -> None:
        self.url = url
    def load_crypto_url(self):
        #calls api through url
        response = requests.get(self.url)
        