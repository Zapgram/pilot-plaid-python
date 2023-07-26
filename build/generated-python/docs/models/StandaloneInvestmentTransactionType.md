# plaid.model.standalone_investment_transaction_type.StandaloneInvestmentTransactionType

Valid values for investment transaction types and subtypes. Note that transactions representing inflow of cash will appear as negative amounts, outflow of cash will appear as positive amounts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Valid values for investment transaction types and subtypes. Note that transactions representing inflow of cash will appear as negative amounts, outflow of cash will appear as positive amounts. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cancel** | str,  | str,  | A cancellation of a pending transaction | 
**transfer** | str,  | str,  | Activity that modifies a position, but not through buy/sell activity e.g. options exercise, portfolio transfer | 
**buy** | str,  | str,  | Buying an investment | 
**fee** | str,  | str,  | Fees on the account, e.g. commission, bookkeeping, options-related. | 
**sell** | str,  | str,  | Selling an investment | 
**cash** | str,  | str,  | Activity that modifies a cash position | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

