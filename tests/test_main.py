import main
def test_success_main(mocker):
    mocker_input = mocker.patch("main.input",side_effect=['bitcoin','inr'])
    mocker_get_crypto = mocker.patch("main.get_crypto_prices",return_value={"success":True,"data":{'bitcoin':{'inr':10000}},"error":None})
    mocker_validate = mocker.patch("main.validate",return_value={"success":True,"data":{'bitcoin':{'inr':10000}},"error":None})
    mocker_processor = mocker.patch("main.process_crypto_data",return_value={"success":True,"data":{'bitcoin':{'inr':10000}},"error":None})
    mocker_processed = mocker.patch("main.process_for_storage",return_value={"success":True,"data":[{"coin": "bitcoin","currency":' inr', "price": 10000,"timestamp":"2026-07-15 20:51:39"}],"error":None})
    mocker_saved_report = mocker.patch("main.save_report",return_value={"success":True,"message":'saved'})
    
    main.main()
    
    mocker_input.assert_has_calls([mocker.call("Enter cryptocoins: "),mocker.call("Enter exchange currency: ")])
    mocker_get_crypto.assert_called_once_with(['bitcoin'],['inr'])
    mocker_validate.assert_called_once_with({'success':True,'data':{'bitcoin':{'inr':10000}},'error':None},['bitcoin'],['inr'])
    mocker_processor.assert_called_once_with({'bitcoin':{'inr':10000}},['bitcoin'],['inr'])
    mocker_processed.assert_called_once_with({'bitcoin':{'inr':10000}})
    mocker_saved_report.assert_called_once_with([{"coin": "bitcoin","currency":' inr', "price": 10000,"timestamp":'2026-07-15 20:51:39'}])

def test_get_crypto_price(mocker):
    mocker_input = mocker.patch("main.input",side_effect=['bitcoin','inr'])
    mocker_get_crypto = mocker.patch("main.get_crypto_prices",return_value={"success":False,"data":None,"error":'abc'})
    mocker_validate = mocker.patch("main.validate")
    mocker_processor = mocker.patch("main.process_crypto_data")
    mocker_processed = mocker.patch("main.process_for_storage")
    mocker_saved_report = mocker.patch("main.save_report")

    main.main()
    mocker_input.assert_has_calls([mocker.call("Enter cryptocoins: "),mocker.call("Enter exchange currency: ")])
    mocker_get_crypto.assert_called_once_with(['bitcoin'],['inr'])
    mocker_validate.assert_not_called()
    mocker_processor.assert_not_called()
    mocker_processed.assert_not_called()
    mocker_saved_report.assert_not_called()

def test_validate(mocker):
    mocker_input = mocker.patch("main.input",side_effect=['bitcoin','inr'])
    mocker_get_crypto = mocker.patch("main.get_crypto_prices",return_value={"success":True,"data":{'bitcoin':{'inr':10000}},"error":None})
    mocker_validate = mocker.patch("main.validate",return_value={"success":False,"data":None,"error":'abc'})
    mocker_processor = mocker.patch("main.process_crypto_data")
    mocker_processed = mocker.patch("main.process_for_storage")
    mocker_saved_report = mocker.patch("main.save_report")

    main.main()
    mocker_input.assert_has_calls([mocker.call("Enter cryptocoins: "),mocker.call("Enter exchange currency: ")])
    mocker_get_crypto.assert_called_once_with(['bitcoin'],['inr'])
    mocker_validate.assert_called_once_with({'success':True,'data':{'bitcoin':{'inr':10000}},'error':None},['bitcoin'],['inr'])
    mocker_processor.assert_not_called()
    mocker_processed.assert_not_called()
    mocker_saved_report.assert_not_called()

def test_process_crypto_data(mocker):
    mocker_input = mocker.patch("main.input",side_effect=['bitcoin','inr'])
    mocker_get_crypto = mocker.patch("main.get_crypto_prices",return_value={"success":True,"data":{'bitcoin':{'inr':10000}},"error":None})
    mocker_validate = mocker.patch("main.validate",return_value={"success":True,"data":{'bitcoin':{'inr':10000}},"error":None})
    mocker_processor = mocker.patch("main.process_crypto_data",return_value={"success":False,"data":None,"error":'abc'})
    mocker_processed = mocker.patch("main.process_for_storage")
    mocker_saved_report = mocker.patch("main.save_report")

    main.main()
    mocker_input.assert_has_calls([mocker.call("Enter cryptocoins: "),mocker.call("Enter exchange currency: ")])
    mocker_get_crypto.assert_called_once_with(['bitcoin'],['inr'])
    mocker_validate.assert_called_once_with({'success':True,'data':{'bitcoin':{'inr':10000}},'error':None},['bitcoin'],['inr'])
    mocker_processor.assert_called_once_with({'bitcoin':{'inr':10000}},['bitcoin'],['inr'])
    mocker_processed.assert_not_called()
    mocker_saved_report.assert_not_called()

def test_process_for_storage(mocker):
    mocker_input = mocker.patch("main.input",side_effect=['bitcoin','inr'])
    mocker_get_crypto = mocker.patch("main.get_crypto_prices",return_value={"success":True,"data":{'bitcoin':{'inr':10000}},"error":None})
    mocker_validate = mocker.patch("main.validate",return_value={"success":True,"data":{'bitcoin':{'inr':10000}},"error":None})
    mocker_processor = mocker.patch("main.process_crypto_data",return_value={"success":True,"data":{'bitcoin':{'inr':10000}},"error":None})
    mocker_processed = mocker.patch("main.process_for_storage",return_value={"success":False,"data":None,"error":'abc'})
    mocker_saved_report = mocker.patch("main.save_report")

    main.main()
    mocker_input.assert_has_calls([mocker.call("Enter cryptocoins: "),mocker.call("Enter exchange currency: ")])
    mocker_get_crypto.assert_called_once_with(['bitcoin'],['inr'])
    mocker_validate.assert_called_once_with({'success':True,'data':{'bitcoin':{'inr':10000}},'error':None},['bitcoin'],['inr'])
    mocker_processor.assert_called_once_with({'bitcoin':{'inr':10000}},['bitcoin'],['inr'])
    mocker_processed.assert_called_once_with({'bitcoin':{'inr':10000}})
    mocker_saved_report.assert_not_called()

def test_save_report(mocker, caplog):
    mocker_input = mocker.patch("main.input",side_effect=['bitcoin','inr'])
    mocker_get_crypto = mocker.patch("main.get_crypto_prices",return_value={"success":True,"data":{'bitcoin':{'inr':10000}},"error":None})
    mocker_validate = mocker.patch("main.validate",return_value={"success":True,"data":{'bitcoin':{'inr':10000}},"error":None})
    mocker_processor = mocker.patch("main.process_crypto_data",return_value={"success":True,"data":{'bitcoin':{'inr':10000}},"error":None})
    mocker_processed = mocker.patch("main.process_for_storage",return_value={"success":True,"data":[{"coin": "bitcoin","currency":' inr', "price": 10000,"timestamp":"2026-07-15 20:51:39"}],"error":None})
    mocker_saved_report = mocker.patch("main.save_report",return_value={"success":False,"data":None,"error":'abc'})

    main.main()
    mocker_input.assert_has_calls([mocker.call("Enter cryptocoins: "),mocker.call("Enter exchange currency: ")])
    mocker_get_crypto.assert_called_once_with(['bitcoin'],['inr'])
    mocker_validate.assert_called_once_with({'success':True,'data':{'bitcoin':{'inr':10000}},'error':None},['bitcoin'],['inr'])
    mocker_processor.assert_called_once_with({'bitcoin':{'inr':10000}},['bitcoin'],['inr'])
    mocker_processed.assert_called_once_with({'bitcoin':{'inr':10000}})
    mocker_saved_report.assert_called_once_with([{"coin": "bitcoin","currency":' inr', "price": 10000,"timestamp":'2026-07-15 20:51:39'}])
    
    assert caplog.records[-1].levelname == "WARNING"
    assert "abc" in caplog.records[-1].message

def test_empty_input(mocker,caplog):
    mocker_input = mocker.patch("main.input",side_effect=['',''])
    mocker_get_crypto = mocker.patch("main.get_crypto_prices")
    mocker_validate = mocker.patch("main.validate")
    mocker_processor = mocker.patch("main.process_crypto_data")
    mocker_processed = mocker.patch("main.process_for_storage")
    mocker_saved_report = mocker.patch("main.save_report")

    main.main()
    mocker_input.assert_has_calls([mocker.call("Enter cryptocoins: "),mocker.call("Enter exchange currency: ")])
    mocker_get_crypto.assert_not_called()
    mocker_validate.assert_not_called()
    mocker_processor.assert_not_called()
    mocker_processed.assert_not_called()
    mocker_saved_report.assert_not_called()

    assert caplog.records[-1].levelname == "WARNING"
    assert "No input received" in caplog.records[-1].message

def test_clean_output(mocker):
    result = main.clean_data([' bitcoin ', ' ethereum'])
    assert result == ['bitcoin','ethereum']