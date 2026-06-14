import logging


logger= logging.getLogger(__name__)

def process_crypto_data(data, coins, currencies):
    try: 
        if not isinstance(coins,list):
            logger.error('Coins must be List')
            return {
                "success" : False,
                "data": None,
                "error": "Invalid Coins/Currencies type"
            }
        if not isinstance(data,dict):
            logger.error('Invalid Data entered')
            return {
                "success" : False,
                "data": None,
                "error": "Invalid Data Input for DataCleaner"
            }
        if not isinstance(currencies,list):
            logger.error('Currencies must be List')
            return {
                "success" : False,
                "data": None,
                "error": "Invalid Currencies Input for DataCleaner"
            }
        if not coins or not currencies:
            logger.error('No Coins/Currencies')
            return {
                "success" : False,
                "data": None,
                "error": "Invalid Input"
            }

        structured_data = {}
        is_missed = {}
        missed_coin = []
        missed_currency = []
        for coin in coins:
            structured_data[coin] = {}
            if coin in data:
                for currency in currencies:
                    if currency in data[coin]:
                        structured_data[coin][currency] = data[coin][currency]
                    else:
                        structured_data[coin][currency] = None
            else:
                for currency in currencies:
                    structured_data[coin][currency] = None
        logger.info('Data cleaned successfully')
        return {
                "success":True,
                "data":structured_data,
                "error":None
            }
    except KeyError as e:
        logger.error(f'Invalid key, {e}')
        return {
                "success" : False,
                "data": None,
                "error": e
            }
    except TypeError as e:
        logger.error(f'Invalid Data type, {e}')
        return {
                "success" : False,
                "data": None,
                "error": e
            }
    except ValueError as e:
        logger.error(f'Invalid Input to Function, {e}')
        return {
                "success" : False,
                "data": None,
                "error": e
            }

