from report_handler import save_report
from report_handler import formatter

def test_output():
    data = [{'coin':'bitcoin','currency':'inr','price':66000,'timestamp':'2024-03-01 15:30:00'}]
    output =save_report(data)

    assert output['success'] is True
    assert output['data'] is not None
    assert output['message'] is not None

def test_invalid_input():
    data ={'coin':'bitcoin','currency':'inr','price':66000,'timestamp':'2024-03-01 15:30:00'}
    output =save_report(data)

    assert output['success'] is False
    assert output['data'] is None
    assert output['error'] is not None

def test_missing_keys_in_input():
    data =[{'coin':'bitcoin','price':66000,'timestamp':'2024-03-01 15:30:00'}]
    output =save_report(data)

    assert output['success'] is False
    assert output['data'] is None
    assert output['error'] is not None
    
def test_empty_input():
    data = []
    output=save_report(data)

    assert output['success'] is False
    assert output['data'] is None
    assert output['error'] is not None

def test_none_value_in_record():
    data ={'coin':'bitcoin','currency': None,'price':66000,'timestamp':'2024-03-01 15:30:00'}
    output=formatter(data)

    assert output['success'] is False
    assert output['data'] is None
    assert output['error'] is not None
