# CreditPayStubNetPay

An object representing information about the net pay amount on the pay stub.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_amount** | **float, none_type** | Raw amount of the net pay for the pay period. | 
**description** | **str, none_type** | Description of the net pay. | 
**iso_currency_code** | **str, none_type** | The ISO-4217 currency code of the net pay. Always &#x60;null&#x60; if &#x60;unofficial_currency_code&#x60; is non-null. | 
**unofficial_currency_code** | **str, none_type** | The unofficial currency code associated with the net pay. Always &#x60;null&#x60; if &#x60;iso_currency_code&#x60; is non-&#x60;null&#x60;. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported &#x60;iso_currency_code&#x60;s. | 
**ytd_amount** | **float, none_type** | The year-to-date amount of the net pay. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


