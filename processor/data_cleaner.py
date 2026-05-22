def process_crypto_data(data:dict, coins, currencies):
    if not coins or not currencies:
        return {
            "success" : False,
            "data": None,
            "error": "Invalid Input"
        }
    if not data["success"]:
        return data
    if data['error'] == None:
        temp_data = data['data']
    structured_data = {}
    is_missed = None
    for coin in coins:
        structured_data[coin] = {}
        if coin in temp_data:
            for currency in currencies:
                if currency in temp_data[coin]:
                    structured_data[coin][currency] = temp_data[coin][currency]
                else:
                    is_missed = currency
                    structured_data[coin][currency] = None
        else:
            is_missed = coin
            for currency in currencies:
                structured_data[coin][currency] = None
    if is_missed:
        return {
            "success":True,
            "data":structured_data,
            "error":"Data Is Missing"
        }
    return {
            "success":True,
            "data":structured_data,
            "error":None
        }
