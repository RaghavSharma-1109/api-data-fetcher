import logging
import os
from config import filepath


logger = logging.getLogger(__name__)

def formatter(data):
    if not isinstance(data,dict):
        logger.error('Invalid data in list')
        return {
            'success':False,
            'data':None,
            'error':'Invalid data in list'
        }
    try:
        coin = data["coin"]
        currency = data["currency"]
        price = data["price"]
        timestamp = data["timestamp"]
        if coin is  None or currency is  None or price is None or timestamp is None:
            logger.error('Invalid value: None')
            return {
                'success': False,
                'data':None,
                'error': 'Invalid value: None'
            }    
        new_line = f"{coin:<15}|{currency:<8}|{price:<13}|{timestamp:<15}\n"
    except KeyError as e:
        logger.error(e)
        return {
            'success':False,
            'data':None,
            'error':e
        }
    return {
        'success':True,
        'data':new_line,
        'error': None
    }
def save_report(records, path=filepath):
    if not isinstance(records,list):
        logger.error('Invalid Input to save_report')
        return {
            'success': False,
            'data': None,
            'error':'Invalid Input to save_report'
        }
    if not records:
        logger.error('No Records of Data Found')
        return {
            'success': False,
            'data' : None,
            'error': 'No Records Found'
        }
    is_exists = os.path.exists(path)
    with open(path,"a") as f:
        if not is_exists:   
            header = f"{'Coin':<15}|{'Currency':<8}|{'Price':<13}|{'Timestamp':<15}\n"
            f.write(header)
            f.write(f"{'-'*15}|{'-'*8}|{'-'*13}|{'-'*15}\n")
        
        for data in records:
            if not isinstance(data,dict):
                logger.error('Invalid data in list')
                return {
                    'success':False,
                    'data':None,
                    'error':'Invalid data in list'
                }
            new_line = formatter(data)
            if new_line['success'] ==False:
                logger.error('formatter failed')
                return new_line
            f.write(new_line['data'])

    logger.info('Data Saved Successfully')
    return {
        'success': True,
        'data': records,
        'message': 'Records saved successfully!!'
    }