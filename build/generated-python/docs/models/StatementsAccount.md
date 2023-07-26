# plaid.model.statements_account.StatementsAccount

Account associated with the item.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Account associated with the item. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account_type** | str,  | str,  | The type of account. Possible values are investment, credit, depository, loan, brokerage, other. | 
**account_id** | str,  | str,  | Plaid&#x27;s unique identifier for the account. | 
**account_name** | str,  | str,  | The name of the account, either assigned by the user or by the financial institution itself. | 
**[statements](#statements)** | list, tuple,  | tuple,  | The list of statements&#x27; metadata associated with this account. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# statements

The list of statements' metadata associated with this account.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of statements&#x27; metadata associated with this account. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**StatementsStatement**](StatementsStatement.md) | [**StatementsStatement**](StatementsStatement.md) | [**StatementsStatement**](StatementsStatement.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

