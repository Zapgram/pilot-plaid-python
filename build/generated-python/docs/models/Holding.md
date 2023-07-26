# plaid.model.holding.Holding

A securities holding at an institution.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A securities holding at an institution. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cost_basis** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The original total value of the holding. This field is calculated by Plaid as the sum of the purchase price of all of the shares in the holding. | value must be a 64 bit float
**unofficial_currency_code** | None, str,  | NoneClass, str,  | The unofficial currency code associated with the holding. Always &#x60;null&#x60; if &#x60;iso_currency_code&#x60; is non-&#x60;null&#x60;. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported &#x60;iso_currency_code&#x60;s.  | 
**institution_price** | decimal.Decimal, int, float,  | decimal.Decimal,  | The last price given by the institution for this security. | value must be a 64 bit float
**account_id** | str,  | str,  | The Plaid &#x60;account_id&#x60; associated with the holding. | 
**quantity** | decimal.Decimal, int, float,  | decimal.Decimal,  | The total quantity of the asset held, as reported by the financial institution. If the security is an option, &#x60;quantity&#x60; will reflect the total number of options (typically the number of contracts multiplied by 100), not the number of contracts. | value must be a 64 bit float
**institution_value** | decimal.Decimal, int, float,  | decimal.Decimal,  | The value of the holding, as reported by the institution. | value must be a 64 bit float
**iso_currency_code** | None, str,  | NoneClass, str,  | The ISO-4217 currency code of the holding. Always &#x60;null&#x60; if &#x60;unofficial_currency_code&#x60; is non-&#x60;null&#x60;. | 
**security_id** | str,  | str,  | The Plaid &#x60;security_id&#x60; associated with the holding. Security data is not specific to a user&#x27;s account; any user who held the same security at the same financial institution at the same time would have identical security data. The &#x60;security_id&#x60; for the same security will typically be the same across different institutions, but this is not guaranteed. The &#x60;security_id&#x60; does not typically change, but may change if inherent details of the security change due to a corporate action, for example, in the event of a ticker symbol change or CUSIP change. | 
**institution_price_as_of** | None, str, date,  | NoneClass, str,  | The date at which &#x60;institution_price&#x60; was current. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**institution_price_datetime** | None, str, datetime,  | NoneClass, str,  | Date and time at which &#x60;institution_price&#x60; was current, in ISO 8601 format (YYYY-MM-DDTHH:mm:ssZ).  This field is returned for select financial institutions and comes as provided by the institution. It may contain default time values (such as 00:00:00).  | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

