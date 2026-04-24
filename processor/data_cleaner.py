def process_crypto_data(data,coins,currencies):
    # input and data validation ->
    if not coins or not currencies:
        return None
    if data is None:
        return None
    if not isinstance(data,dict):
        return None
    if data == {}:
        return None
    # data extraction and processing ->
    structured_data = {}
    for coin in coins:
        if coin not in data:
            continue
        temp = {}
        for currency in currencies:
            if currency not in data[coin]:
                continue

            temp[currency] = data[coin][currency] 
        if temp:
            structured_data[coin] = temp
    return structured_data