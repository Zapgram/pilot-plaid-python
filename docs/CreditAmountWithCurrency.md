# CreditAmountWithCurrency

This contains an amount, denominated in the currency specified by either `iso_currency_code` or `unofficial_currency_code`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Value of amount with up to 2 decimal places. | [optional] 
**iso_currency_code** | **str, none_type** | The ISO 4217 currency code of the amount or balance. | [optional] 
**unofficial_currency_code** | **str, none_type** | The unofficial currency code associated with the amount or balance. Always &#x60;null&#x60; if &#x60;iso_currency_code&#x60; is non-null. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


