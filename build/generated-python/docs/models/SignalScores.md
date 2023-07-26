# plaid.model.signal_scores.SignalScores

Risk scoring details broken down by risk category.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Risk scoring details broken down by risk category. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**customer_initiated_return_risk** | [**CustomerInitiatedReturnRisk**](CustomerInitiatedReturnRisk.md) | [**CustomerInitiatedReturnRisk**](CustomerInitiatedReturnRisk.md) |  | [optional] 
**bank_initiated_return_risk** | [**BankInitiatedReturnRisk**](BankInitiatedReturnRisk.md) | [**BankInitiatedReturnRisk**](BankInitiatedReturnRisk.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

