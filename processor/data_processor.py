# INPUT RECEIVED:
#     {
#   "success": True,
#   "data": {
#     "bitcoin": {
#         "usd": 67000,
#         "inr": 5500000
#     }
#   }
# }
from datetime import datetime
def process_for_storage(cleaned_data):
    data = cleaned_data.get("data")
    output_data = []
    if not data:
        return {
        "success": False,
        "data": None,
        "error": "No data found"
    }
    
    for coin in data:
        for currency in data[coin]:
            temp = {}
            price = data[coin][currency]
            if price is None:
                continue
            temp["coin"] = str(coin)
            temp["currency"] = str(currency)
            temp["price"] = price
            timestamp = datetime.now()
            timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            temp["timestamp"] = timestamp

            output_data.append(temp)
    return {
        "success" : True,
        "data": output_data,
        "error":None
    }