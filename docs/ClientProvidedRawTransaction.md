# ClientProvidedRawTransaction

A client-provided transaction for Plaid to enhance.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID for the transaction used to help you tie data back to your systems. | 
**description** | **str** | The raw description of the transaction. | 
**amount** | **float** | The value of the transaction with direction. (NOTE: this will affect enrichment results, so directions are important):.   Negative (-) for credits (e.g., incoming transfers, refunds)   Positive (+) for debits (e.g., purchases, fees, outgoing transfers) | 
**iso_currency_code** | **str** | The ISO-4217 currency code of the transaction e.g. USD. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


