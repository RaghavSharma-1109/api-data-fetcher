import requests
def get_crypto_prices(coins:list,currency):
    url = "https://api.coingecko.com/api/v3/simple/price"

    final_coin = ",".join(coins)
    final_currencies = ",".join(currency)
    url += f"?ids={final_coin}&vs_currencies={final_currencies}"

    try:
        response = requests.get(url,timeout=5)
        if response.status_code == 200:
            data = response.json()
            return {
                "success": True,
                "data": data,
                "error": None
            }
        else :
            return {
            "success":False,
            "data": None,
            "error": "API returned error response"
        }
    except requests.exceptions.Timeout:
        # timeout case
        return {
                "success":False,
                "data": None,
                "error": "Request Timed out"
            }

    except requests.exceptions.ConnectionError:
        # no internet
        return {
            "success":False,
            "data": None,
            "error": "Connection error"
        }

    except requests.exceptions.RequestException:
        # other request-related issues
        return {
            "success":False,
            "data": None,
            "error": "Unexpected API response"
        }


# data returned from fetcher.py 
#       {
#           "success": True/False,
#           "data": data or None,
#           "error": Error Message
#             }