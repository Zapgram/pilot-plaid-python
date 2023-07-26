# plaid.model.risk_check_device.RiskCheckDevice

Result summary object specifying values for `device` attributes of risk check.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Result summary object specifying values for &#x60;device&#x60; attributes of risk check. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ip_timezone_offset** | [**UTCOffset**](UTCOffset.md) | [**UTCOffset**](UTCOffset.md) |  | 
**ip_proxy_type** | [**ProxyType**](ProxyType.md) | [**ProxyType**](ProxyType.md) |  | 
**ip_spam_list_count** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Count of spam lists the IP address is associated with if known. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

