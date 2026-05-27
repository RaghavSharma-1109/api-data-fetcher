def process_crypto_data(data:dict, coins, currencies):
    if not coins or not currencies:
        return {
            "success" : False,
            "data": None,
            "error": "Invalid Input"
        }
    if not data["success"]:
        return data
    if data.get("data") != None:
        temp_data = data['data']
    else:
        return data
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
        return {
            "success":True,
            "data":structured_data,
            "error": is_missed
        }

    return {
            "success":True,
            "data":structured_data,
            "error":None
        }
