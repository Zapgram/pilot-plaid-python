# plaid.model.pay_stub_pay_period_details.PayStubPayPeriodDetails

Details about the pay period.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Details about the pay period. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**end_date** | None, str, date,  | NoneClass, str,  | The date on which the pay period ended, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (\&quot;yyyy-mm-dd\&quot;). | value must conform to RFC-3339 full-date YYYY-MM-DD
**pay_date** | None, str, date,  | NoneClass, str,  | The date on which the pay stub was issued, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (\&quot;yyyy-mm-dd\&quot;). | value must conform to RFC-3339 full-date YYYY-MM-DD
**unofficial_currency_code** | None, str,  | NoneClass, str,  | The unofficial currency code associated with the net pay. Always &#x60;null&#x60; if &#x60;iso_currency_code&#x60; is non-&#x60;null&#x60;. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported &#x60;iso_currency_code&#x60;s. | 
**gross_earnings** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Total earnings before tax/deductions. | value must be a 64 bit float
**[distribution_breakdown](#distribution_breakdown)** | list, tuple,  | tuple,  |  | 
**pay_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The amount of the paycheck. | value must be a 64 bit float
**iso_currency_code** | None, str,  | NoneClass, str,  | The ISO-4217 currency code of the net pay. Always &#x60;null&#x60; if &#x60;unofficial_currency_code&#x60; is non-null. | 
**pay_frequency** | None, str,  | NoneClass, str,  | The frequency at which an individual is paid. | 
**start_date** | None, str, date,  | NoneClass, str,  | The date on which the pay period started, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (\&quot;yyyy-mm-dd\&quot;). | value must conform to RFC-3339 full-date YYYY-MM-DD
**pay_basis** | [**CreditPayStubPayBasisType**](CreditPayStubPayBasisType.md) | [**CreditPayStubPayBasisType**](CreditPayStubPayBasisType.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# distribution_breakdown

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PayStubDistributionBreakdown**](PayStubDistributionBreakdown.md) | [**PayStubDistributionBreakdown**](PayStubDistributionBreakdown.md) | [**PayStubDistributionBreakdown**](PayStubDistributionBreakdown.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

