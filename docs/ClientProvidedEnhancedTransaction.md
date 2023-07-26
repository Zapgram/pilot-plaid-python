# ClientProvidedEnhancedTransaction

A client-provided transaction that Plaid has enhanced.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique transaction identifier to tie transactions back to clients&#39; systems. | 
**description** | **str** | The raw description of the transaction. | 
**amount** | **float** | The value of the transaction, denominated in the account&#39;s currency, as stated in &#x60;iso_currency_code&#x60;. Positive values when money moves out of the account; negative values when money moves in. For example, debit card purchases are positive; credit card payments, direct deposits, and refunds are negative. | 
**iso_currency_code** | **str** | The ISO-4217 currency code of the transaction. | 
**enhancements** | [**Enhancements**](Enhancements.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


