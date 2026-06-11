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
        if not coins or not currencies:
            logger.error('No Coins/Currencies')
            return {
                "success" : False,
                "data": None,
                "error": "Invalid Input"
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
        if not data["success"]:
            logger.error('No Data to clean')
            return {
                "success" : False,
                "data": None,
                "error": "No (Success=True) Data entered in cleaner "
            }
        if data.get("data") is not None:
            temp_data = data['data']
        else:
            logger.error('No Data Found')
            return {
                "success" : False,
                "data": None,
                "error": "Unable to find data for cleaner"
            }
    
        structured_data = {}
        is_missed = {}
        missed_coin = []
        missed_currency = []
        for coin in coins:
            structured_data[coin] = {}
            if coin in temp_data:
                for currency in currencies:
                    if currency in temp_data[coin]:
                        structured_data[coin][currency] = temp_data[coin][currency]
                    else:
                        if currency not in missed_currency:
                            missed_currency.append(currency)

                        structured_data[coin][currency] = None
            else:
                

                if coin not in missed_coin:
                    missed_coin.append(coin)
                    

                for currency in currencies:
                    structured_data[coin][currency] = None
        is_missed["missing_currencies"] = missed_currency
        is_missed["missing_coins"] = missed_coin
        if missed_coin or missed_currency:
            logger.warning(f'Missing data - coins: {missed_coin}, currencies: {missed_currency}')
            return {
                "success":True,
                "data":structured_data,
                "error": is_missed
            }
        logger.info('Data cleaned successfully')
        return {
                "success":True,
                "data":structured_data,
                "error":None
            }
    except KeyError as e:
        logger.error(f'Invalid key, {e}')
        return None
    except TypeError as e:
        logger.error(f'Invalid Data type, {e}')
        return None
    except ValueError as e:
        logger.error(f'Invalid Input to Function, {e}')
        return None

