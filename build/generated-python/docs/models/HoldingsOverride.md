# plaid.model.holdings_override.HoldingsOverride

Specify the holdings on the account.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specify the holdings on the account. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**institution_price** | decimal.Decimal, int, float,  | decimal.Decimal,  | The last price given by the institution for this security | value must be a 64 bit float
**security** | [**SecurityOverride**](SecurityOverride.md) | [**SecurityOverride**](SecurityOverride.md) |  | 
**quantity** | decimal.Decimal, int, float,  | decimal.Decimal,  | The total quantity of the asset held, as reported by the financial institution. | value must be a 64 bit float
**currency** | str,  | str,  | Either a valid &#x60;iso_currency_code&#x60; or &#x60;unofficial_currency_code&#x60; | 
**institution_price_as_of** | str, date,  | str,  | The date at which &#x60;institution_price&#x60; was current. Must be formatted as an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) date. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**cost_basis** | decimal.Decimal, int, float,  | decimal.Decimal,  | The average original value of the holding. Multiple cost basis values for the same security purchased at different prices are not supported. | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

