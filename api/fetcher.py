import logging
import requests
from config import url as api_url
from config import timeout


logger=logging.getLogger(__name__)


def get_crypto_prices(coins:list,currency):
    
    final_coin = ",".join(coins)
    final_currencies = ",".join(currency)
    endpoint = f"?ids={final_coin}&vs_currencies={final_currencies}"
    required_url = api_url + endpoint
    try:
        response = requests.get(required_url,timeout=timeout)
        if response.status_code == 200:
            data = response.json()
            logger.info('API DATA FETCHED')
            return {
                "success": True,
                "data": data,
                "error": None
            }
        else :
            logger.error(f'Unable to fetch data {response.status_code}')
            return {
            "success":False,
            "data": None,
            "error": "API returned error response"
        }
    except requests.exceptions.Timeout:
        # timeout case
        logger.error('SESSION TIMEOUT')
        return {
                "success":False,
                "data": None,
                "error": "Request Timed out"
            }

    except requests.exceptions.ConnectionError:
        # no internet
        logger.error('BAD NETWORK GATEWAY')
        return {
            "success":False,
            "data": None,
            "error": "Connection error"
        }

    except requests.exceptions.RequestException:
        # other request-related issues
        logger.error('API call Failed')
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