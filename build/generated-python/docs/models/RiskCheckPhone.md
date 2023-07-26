# plaid.model.risk_check_phone.RiskCheckPhone

Result summary object specifying values for `phone` attributes of risk check.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Result summary object specifying values for &#x60;phone&#x60; attributes of risk check. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[linked_services](#linked_services)** | list, tuple,  | tuple,  | A list of online services where this phone number has been detected to have accounts or other activity. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# linked_services

A list of online services where this phone number has been detected to have accounts or other activity.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of online services where this phone number has been detected to have accounts or other activity. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RiskCheckLinkedService**](RiskCheckLinkedService.md) | [**RiskCheckLinkedService**](RiskCheckLinkedService.md) | [**RiskCheckLinkedService**](RiskCheckLinkedService.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

