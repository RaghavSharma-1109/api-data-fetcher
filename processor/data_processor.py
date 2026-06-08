import logging
from datetime import datetime
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
logger = logging.getLogger(__name__)


def process_for_storage(cleaned_data):
    data = cleaned_data.get("data")
    output_data = []
    if not data:
        logger.error('No Data Found')
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
    logger.info('Data processed successfully')
    return {
        "success" : True,
        "data": output_data,
        "error":None
    }