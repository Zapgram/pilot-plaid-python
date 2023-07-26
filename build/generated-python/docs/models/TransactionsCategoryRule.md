# plaid.model.transactions_category_rule.TransactionsCategoryRule

A representation of a transactions category rule.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A representation of a transactions category rule. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | A unique identifier of the rule created | [optional] 
**item_id** | str,  | str,  | A unique identifier of the Item the rule was created for. | [optional] 
**created_at** | str, datetime,  | str,  | Date and time when a rule was created in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( &#x60;YYYY-MM-DDTHH:mm:ssZ&#x60; ).  | [optional] value must conform to RFC-3339 date-time
**personal_finance_category** | str,  | str,  | Personal finance category unique identifier.  In the personal finance category taxonomy, this field is represented by the detailed category field.  | [optional] 
**rule_details** | [**TransactionsRuleDetails**](TransactionsRuleDetails.md) | [**TransactionsRuleDetails**](TransactionsRuleDetails.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

