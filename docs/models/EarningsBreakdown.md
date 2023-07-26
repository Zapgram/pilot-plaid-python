# plaid.model.earnings_breakdown.EarningsBreakdown

An object representing the earnings line items for the pay period.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing the earnings line items for the pay period. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**canonical_description** | [**EarningsBreakdownCanonicalDescription**](EarningsBreakdownCanonicalDescription.md) | [**EarningsBreakdownCanonicalDescription**](EarningsBreakdownCanonicalDescription.md) |  | [optional] 
**current_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Raw amount of the earning line item. | [optional] value must be a 64 bit float
**description** | None, str,  | NoneClass, str,  | Description of the earning line item. | [optional] 
**hours** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Number of hours applicable for this earning. | [optional] 
**iso_currency_code** | None, str,  | NoneClass, str,  | The ISO-4217 currency code of the line item. Always &#x60;null&#x60; if &#x60;unofficial_currency_code&#x60; is non-null. | [optional] 
**rate** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Hourly rate applicable for this earning. | [optional] value must be a 64 bit float
**unofficial_currency_code** | None, str,  | NoneClass, str,  | The unofficial currency code associated with the line item. Always &#x60;null&#x60; if &#x60;iso_currency_code&#x60; is non-&#x60;null&#x60;. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported &#x60;iso_currency_code&#x60;s. | [optional] 
**ytd_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The year-to-date amount of the deduction. | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

