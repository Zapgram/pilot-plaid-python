# plaid.model.investments_transactions_override.InvestmentsTransactionsOverride

Specify the list of investments transactions on the account.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specify the list of investments transactions on the account. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date** | str, date,  | str,  | Posting date for the transaction. Must be formatted as an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) date. | value must conform to RFC-3339 full-date YYYY-MM-DD
**quantity** | decimal.Decimal, int, float,  | decimal.Decimal,  | The number of units of the security involved in this transaction. Must be positive if the type is a buy and negative if the type is a sell. | value must be a 64 bit float
**price** | decimal.Decimal, int, float,  | decimal.Decimal,  | The price of the security at which this transaction occurred. | value must be a 64 bit float
**name** | str,  | str,  | The institution&#x27;s description of the transaction. | 
**currency** | str,  | str,  | Either a valid &#x60;iso_currency_code&#x60; or &#x60;unofficial_currency_code&#x60; | 
**type** | str,  | str,  | The type of the investment transaction. Possible values are: &#x60;buy&#x60;: Buying an investment &#x60;sell&#x60;: Selling an investment &#x60;cash&#x60;: Activity that modifies a cash position &#x60;fee&#x60;: A fee on the account &#x60;transfer&#x60;: Activity that modifies a position, but not through buy/sell activity e.g. options exercise, portfolio transfer | 
**fees** | decimal.Decimal, int, float,  | decimal.Decimal,  | The combined value of all fees applied to this transaction. | [optional] value must be a 64 bit float
**security** | [**SecurityOverride**](SecurityOverride.md) | [**SecurityOverride**](SecurityOverride.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

