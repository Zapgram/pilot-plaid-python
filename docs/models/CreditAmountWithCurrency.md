# plaid.model.credit_amount_with_currency.CreditAmountWithCurrency

This contains an amount, denominated in the currency specified by either `iso_currency_code` or `unofficial_currency_code`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This contains an amount, denominated in the currency specified by either &#x60;iso_currency_code&#x60; or &#x60;unofficial_currency_code&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | Value of amount with up to 2 decimal places. | [optional] 
**iso_currency_code** | [**CreditIsoCurrencyCode**](CreditIsoCurrencyCode.md) | [**CreditIsoCurrencyCode**](CreditIsoCurrencyCode.md) |  | [optional] 
**unofficial_currency_code** | [**CreditUnofficialCurrencyCode**](CreditUnofficialCurrencyCode.md) | [**CreditUnofficialCurrencyCode**](CreditUnofficialCurrencyCode.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

