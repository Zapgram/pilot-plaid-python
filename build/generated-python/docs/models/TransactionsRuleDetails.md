# plaid.model.transactions_rule_details.TransactionsRuleDetails

A representation of transactions rule details.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A representation of transactions rule details. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**field** | [**TransactionsRuleField**](TransactionsRuleField.md) | [**TransactionsRuleField**](TransactionsRuleField.md) |  | 
**query** | str,  | str,  | For TRANSACTION_ID field, provide transaction_id. For NAME field, provide a string pattern.  | 
**type** | [**TransactionsRuleType**](TransactionsRuleType.md) | [**TransactionsRuleType**](TransactionsRuleType.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

