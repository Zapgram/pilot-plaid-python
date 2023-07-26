# CreditSessionBankIncomeResult

The details of a bank income verification in Link

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**CreditSessionBankIncomeStatus**](CreditSessionBankIncomeStatus.md) |  | [optional] 
**item_id** | **str** | The Plaid Item ID. The &#x60;item_id&#x60; is always unique; linking the same account at the same institution twice will result in two Items with different &#x60;item_id&#x60; values. Like all Plaid identifiers, the &#x60;item_id&#x60; is case-sensitive. | [optional] 
**institution_id** | **str** | The Plaid Institution ID associated with the Item. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


