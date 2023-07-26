# plaid.model.credit_pay_stub_employee.CreditPayStubEmployee

Data about the employee.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data about the employee. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**marital_status** | None, str,  | NoneClass, str,  | Marital status of the employee - either &#x60;SINGLE&#x60; or &#x60;MARRIED&#x60;. | 
**address** | [**CreditPayStubAddress**](CreditPayStubAddress.md) | [**CreditPayStubAddress**](CreditPayStubAddress.md) |  | 
**taxpayer_id** | [**PayStubTaxpayerID**](PayStubTaxpayerID.md) | [**PayStubTaxpayerID**](PayStubTaxpayerID.md) |  | 
**name** | None, str,  | NoneClass, str,  | The name of the employee. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

