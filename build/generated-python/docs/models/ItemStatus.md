# plaid.model.item_status.ItemStatus

An object with information about the status of the Item.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | An object with information about the status of the Item. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**investments** | [**ItemStatusInvestments**](ItemStatusInvestments.md) | [**ItemStatusInvestments**](ItemStatusInvestments.md) |  | [optional] 
**transactions** | [**ItemStatusTransactions**](ItemStatusTransactions.md) | [**ItemStatusTransactions**](ItemStatusTransactions.md) |  | [optional] 
**last_webhook** | [**ItemStatusLastWebhook**](ItemStatusLastWebhook.md) | [**ItemStatusLastWebhook**](ItemStatusLastWebhook.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

