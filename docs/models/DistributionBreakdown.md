# plaid.model.distribution_breakdown.DistributionBreakdown

Information about the accounts that the payment was distributed to.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Information about the accounts that the payment was distributed to. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account_name** | None, str,  | NoneClass, str,  | Name of the account for the given distribution. | [optional] 
**bank_name** | None, str,  | NoneClass, str,  | The name of the bank that the payment is being deposited to. | [optional] 
**current_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The amount distributed to this account. | [optional] value must be a 64 bit float
**iso_currency_code** | None, str,  | NoneClass, str,  | The ISO-4217 currency code of the net pay. Always &#x60;null&#x60; if &#x60;unofficial_currency_code&#x60; is non-null. | [optional] 
**mask** | None, str,  | NoneClass, str,  | The last 2-4 alphanumeric characters of an account&#x27;s official account number. | [optional] 
**type** | None, str,  | NoneClass, str,  | Type of the account that the paystub was sent to (e.g. &#x27;checking&#x27;). | [optional] 
**unofficial_currency_code** | None, str,  | NoneClass, str,  | The unofficial currency code associated with the net pay. Always &#x60;null&#x60; if &#x60;iso_currency_code&#x60; is non-&#x60;null&#x60;. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported &#x60;iso_currency_code&#x60;s. | [optional] 
**current_pay** | [**Pay**](Pay.md) | [**Pay**](Pay.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

