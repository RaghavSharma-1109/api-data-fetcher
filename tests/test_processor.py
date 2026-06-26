from processor.data_processor import process_for_storage

def test_output_type():
    data = {
        'bitcoin':{
            'inr':66000
            },
        'ethereum':{
            'inr':10000
            }
    }
    output = process_for_storage(data)

    assert output is not None
    assert isinstance(output,dict) is True
    assert isinstance(output['data'], list) is True

def test_output_keys():
    data = {
            'bitcoin':{
                'inr':66000
                },
            'ethereum':{
                'inr':10000
                }
        }
    output = process_for_storage(data)
    assert len(output['data'])>0
    for item in output['data']:
        assert isinstance(item,dict) is True
        
        assert item['coin'] is not None
        assert item['currency'] is not None
        assert item['price'] is not None
        assert item['timestamp'] is not None

def test_output_have_all_keys():
    data = {'bitcoin':None}

    output = process_for_storage(data)

    assert output['success'] is False
    assert output['data'] is None
    assert output['error'] is not None 

def test_input_empty():
    data = {}

    output = process_for_storage(data)

    assert output['success'] is False
    assert output['data'] is None
    assert output['error'] is not None

def test_missing_price():
    data = {
            'bitcoin':{
                'inr':None
                },
            'ethereum':{
                'inr':None
                }
        }
    output = process_for_storage(data)

    assert output['success'] is False
    assert output['data'] is None
    assert output['error'] is not None

