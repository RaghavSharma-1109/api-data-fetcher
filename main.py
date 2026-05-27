from api.fetcher import get_crypto_prices
from datacleaner.data_cleaner import process_crypto_data
from processor.data_processor import process_for_storage
from report_handler import save_report

def main():
    coins = input("Enter cryptocoins: ").lower().split(',')
    final_coins =[]
    for coin in coins:
        coin = coin.strip()
        if not coin:
            continue
        final_coins.append(coin)
    currencies= input("Enter exchange currency: ").lower().split(',')
    final_currencies = []
    for currency in currencies:
        currency = currency.strip()
        if not currency:
            continue
        final_currencies.append(currency)
    if not final_coins or not final_currencies:
        print("No input received")
        return
    result = get_crypto_prices(final_coins,final_currencies)
    if not result["success"]:
        print(result['error'])
        return
    clean_result = process_crypto_data(result,final_coins,final_currencies)
    if not clean_result['success']:
        print(clean_result['error'])
        return
    processed_result = process_for_storage(clean_result)
    if not processed_result['success']:
        print(processed_result['error'])
        return
    # In Next version the user may enter its own filepath for report.
    records = processed_result['data']
    saved = save_report(records,filepath=None)
    if saved['success']:
        print(saved['message'])
        return
    else:
        print(saved['error'])
        return
    

if __name__ == "__main__":
    main()