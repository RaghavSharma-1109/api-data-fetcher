import logging
from api.fetcher import get_crypto_prices
from datacleaner.data_cleaner import process_crypto_data
from processor.data_processor import process_for_storage
from report_handler import save_report
from Validator.validator import validate

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

def clean_data(items:list):
    result = []
    for data in items:
        data = data.strip()
        if not data:
            continue
        result.append(data)
    return result
def main():
    coins = input("Enter cryptocoins: ").lower().split(',')
    final_coins =clean_data(coins)
    currencies= input("Enter exchange currency: ").lower().split(',')
    final_currencies = clean_data(currencies)
    if not final_coins or not final_currencies:
        logger.warning("No input received")
        return
    result = get_crypto_prices(final_coins,final_currencies)
    if not result["success"]:
        logger.error(result['error'])
        return
    output = validate(result,final_coins,final_currencies)
    if not output["success"]:
        logger.error(output["error"])
        return
    clean_result = process_crypto_data(output,final_coins,final_currencies)
    if not clean_result['success']:
        logger.error(clean_result['error'])
        return
    processed_result = process_for_storage(clean_result)
    if not processed_result['success']:
        logger.error(processed_result['error'])
        return
    # In Next version the user may enter its own filepath for report.
    records = processed_result['data']
    saved = save_report(records)
    if saved['success']:
        logger.info(saved['message'])
        return
    else:
        logger.warning(saved['error'])
        return
    

if __name__ == "__main__":
    main()