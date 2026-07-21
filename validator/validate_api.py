import logging

logger = logging.getLogger(__name__)

def validate(raw_data,coins,currencies):
    if not isinstance(raw_data, dict):
        logger.error('Fetcher must return dict')
        return {
            "success":False,
            "data": None,
            "error": "Invalid data input from fetcher to validator"
        }
    try:
        response = raw_data.get("data")
        if response is None:
            logger.error('Api does not return anything')
            return {
                "success":False,
                "data":None,
                "error": 'Api does not return anything'
            }
        for coin in coins:
            coin = coin.lower()
            if coin not in response:
                logger.error(f'Coin[{coin}] not in API response.')
                return {
                    "success":False,
                    "data": None,
                    "error": "API response Missing coin"
                }
            if not response[coin]:
                logger.error('Coin price not fetched')
                return {
                    "success": False,
                    "data":None,
                    "error":f"Coin {coin} data not fetched"
                }
            for currency in currencies:
                currency = currency.lower()
                if currency not in response[coin]:
                    logger.error(f'Currency [{currency}] is Missing in response')
                    return {
                        "success":False,
                        "data":None,
                        "error":"Api response misses currency"
                    }
        logger.info("API response data VALIDATED")
        return {
            "success":True,
            "data": response,
            "error": None
        }

    except KeyError as e:
        logger.error(f"Invalid Key, {e}")
        return {
            "success":False,
            "data":None,
            "error":"Invalid key from fetcher data"
        }
