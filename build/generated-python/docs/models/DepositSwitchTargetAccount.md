# plaid.model.deposit_switch_target_account.DepositSwitchTargetAccount

The deposit switch destination account

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The deposit switch destination account | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account_number** | str,  | str,  | Account number for deposit switch destination | 
**account_name** | str,  | str,  | The name of the deposit switch destination account, as it will be displayed to the end user in the Deposit Switch interface. It is not required to match the name used in online banking. | 
**account_subtype** | str,  | str,  | The account subtype of the account, either &#x60;checking&#x60; or &#x60;savings&#x60;. | must be one of ["checking", "savings", ] 
**routing_number** | str,  | str,  | Routing number for deposit switch destination | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

