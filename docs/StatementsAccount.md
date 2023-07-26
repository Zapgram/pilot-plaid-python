# StatementsAccount

Account associated with the item.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Plaid&#39;s unique identifier for the account. | 
**account_name** | **str** | The name of the account, either assigned by the user or by the financial institution itself. | 
**account_type** | **str** | The type of account. Possible values are investment, credit, depository, loan, brokerage, other. | 
**statements** | [**[StatementsStatement]**](StatementsStatement.md) | The list of statements&#39; metadata associated with this account. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


