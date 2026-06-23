from Validator.validator import validate
def test_valid_data():
    data = {'data':{"bitcoin":{"inr":60000}}}
    coin =['bitcoin']
    currency = ['inr']

    output= validate(data,coin,currency)

    assert output["success"] is True

def test_invalid_data():
    data = [{"bitcoin":{"inr":60000}}]  
    coin =['bitcoin']
    currency = ['inr']

    output= validate(data,coin,currency)

    assert output["success"] is False
    assert output["data"] is None
    assert output["error"] is not None

def test_coin_missing_in_data():
    data = {'data':{"bitcoin":{"inr":60000}}}
    coins =['bitcoin','tether']
    currency = ['inr']

    output= validate(data,coins,currency)


    assert output["success"] is False
    assert output["data"] is None
    assert output["error"] is not None

def test_data_key_not_in_data():
    data = {'success': True,'error': None}
    coins =['bitcoin']
    currency = ['inr']

    output= validate(data,coins,currency)

    assert output["success"] is False
    assert output["data"] is None
    assert output["error"] is not None

def test_coin_price_not_found():
    data = {'data':{"bitcoin":None}}
    coins =['bitcoin','tether']
    currency = ['inr']

    output= validate(data,coins,currency)

    assert output["success"] is False
    assert output["data"] is None
    assert output["error"] is not None

def test_currency_lower_casing():
    data = {'data':{"bitcoin":{'inr':6600000}}}
    coins =['bitcoin']
    currency = ['INR']

    output= validate(data,coins,currency)

    assert output["success"] is True
    assert output["error"] is None