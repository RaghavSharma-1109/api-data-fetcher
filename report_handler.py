import os
def formatter(data):

    coin = data.get("coin")
    currency = data.get("currency")
    price = data.get("price")
    timestamp = data.get("timestamp")
    new_line = f"{coin:<15} |{currency:<8} |{price:<13} |{timestamp:<15}\n"
    return new_line
def save_report(records,filepath):
    if not filepath:
        filepath="crypto_data.txt"
    
    if not records:
        return {
            'success': False,
            'data' : None,
            'error': 'No Records Found'
        }
    is_exists = os.path.exists(filepath)
    with open(filepath,"a") as f:
        if not is_exists:   
            header = f"{'Coin':<15}| {'Currency':<8}| {'Price':<13}| {'Timestamp':<15}\n"
            f.write(header)
            f.write(f"{'-'*15} |{'-'*8} |{'-'*13} |{'-'*15}\n")
        
        for data in records:
            new_line = formatter(data)
            f.write(new_line)