# TransactionsRulesListResponse

TransactionsRulesListResponse defines the response schema for `/beta/transactions/rules/v1/list`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**[TransactionsCategoryRule]**](TransactionsCategoryRule.md) | A list of the Item&#39;s transaction rules | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


