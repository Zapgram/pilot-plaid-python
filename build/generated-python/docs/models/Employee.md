# plaid.model.employee.Employee

Data about the employee.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data about the employee. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**address** | [**PaystubAddress**](PaystubAddress.md) | [**PaystubAddress**](PaystubAddress.md) |  | 
**name** | None, str,  | NoneClass, str,  | The name of the employee. | 
**marital_status** | None, str,  | NoneClass, str,  | Marital status of the employee - either &#x60;single&#x60; or &#x60;married&#x60;. | [optional] 
**taxpayer_id** | [**TaxpayerID**](TaxpayerID.md) | [**TaxpayerID**](TaxpayerID.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

