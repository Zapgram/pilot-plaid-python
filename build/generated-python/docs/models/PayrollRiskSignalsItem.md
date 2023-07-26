# plaid.model.payroll_risk_signals_item.PayrollRiskSignalsItem

Object containing fraud risk data pertaining to the Item linked as part of the verification.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing fraud risk data pertaining to the Item linked as part of the verification. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**item_id** | str,  | str,  | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**[verification_risk_signals](#verification_risk_signals)** | list, tuple,  | tuple,  | Array of payroll income document authenticity data retrieved for each of the user&#x27;s accounts. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# verification_risk_signals

Array of payroll income document authenticity data retrieved for each of the user's accounts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of payroll income document authenticity data retrieved for each of the user&#x27;s accounts. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DocumentRiskSignalsObject**](DocumentRiskSignalsObject.md) | [**DocumentRiskSignalsObject**](DocumentRiskSignalsObject.md) | [**DocumentRiskSignalsObject**](DocumentRiskSignalsObject.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

