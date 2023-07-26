# TransactionsCategoryRule

A representation of a transactions category rule.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier of the rule created | [optional] 
**item_id** | **str** | A unique identifier of the Item the rule was created for. | [optional] 
**created_at** | **datetime** | Date and time when a rule was created in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( &#x60;YYYY-MM-DDTHH:mm:ssZ&#x60; ).  | [optional] 
**personal_finance_category** | **str** | Personal finance category unique identifier.  In the personal finance category taxonomy, this field is represented by the detailed category field.  | [optional] 
**rule_details** | [**TransactionsRuleDetails**](TransactionsRuleDetails.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


