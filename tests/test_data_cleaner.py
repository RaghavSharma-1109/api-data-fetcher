from datacleaner.data_cleaner import process_crypto_data

def test_process_crypto_data():
    data = {"bitcoin":{"inr":6600000}}
    coins =["bitcoin"]
    currencies=["inr"]

    output = process_crypto_data(data,coins,currencies)


    assert output["success"] is True
    assert output["error"] is None
    assert output["data"] == {'bitcoin':{'inr':6600000}}

def test_coins_as_string():
    coins = "bitcoin"
    data = {"bitcoin":{"inr":6600000}}
    currencies=["inr"]

    output  = process_crypto_data(data,coins,currencies)

    assert output["success"] is False
    assert output["data"] is None
def test_data_not_dict():
    coins = ["bitcoin"]
    data = [{"bitcoin":{"inr":6600000}}]
    currencies=["inr"]
    output  = process_crypto_data(data,coins,currencies)

    assert output["success"] is False
    assert output["data"] is None

def test_currency_empty_list():
    coins = ["bitcoin"]
    data = {"bitcoin":{"inr":6600000}}
    currencies=[]
    output  = process_crypto_data(data,coins,currencies)

    assert output["success"] is False
    assert output["data"] is None

def test_coin_not_in_data():
    coins = ["bitcoin","Dogecoin"]
    data = {"bitcoin":{"inr":6600000}}
    currencies=["inr"]
    output  = process_crypto_data(data,coins,currencies)

    assert output["success"] is True
    assert output["data"] is not None
    try_data = output["data"]

    for coin in coins:
        for currency in currencies:
            if coin not in data:
                assert try_data[coin][currency] is None
                break