# plaid.model.pay_period_details.PayPeriodDetails

Details about the pay period.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Details about the pay period. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**check_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The amount of the paycheck. | [optional] value must be a 64 bit float
**[distribution_breakdown](#distribution_breakdown)** | list, tuple,  | tuple,  |  | [optional] 
**end_date** | None, str, date,  | NoneClass, str,  | The pay period end date, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format: \&quot;yyyy-mm-dd\&quot;. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**gross_earnings** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Total earnings before tax/deductions. | [optional] value must be a 64 bit float
**pay_date** | None, str, date,  | NoneClass, str,  | The date on which the paystub was issued, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (\&quot;yyyy-mm-dd\&quot;). | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**pay_frequency** | None, str,  | NoneClass, str,  | The frequency at which an individual is paid. | [optional] must be one of ["PAY_FREQUENCY_UNKNOWN", "PAY_FREQUENCY_WEEKLY", "PAY_FREQUENCY_BIWEEKLY", "PAY_FREQUENCY_SEMIMONTHLY", "PAY_FREQUENCY_MONTHLY", None, ] 
**pay_day** | None, str, date,  | NoneClass, str,  | The date on which the paystub was issued, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (\&quot;yyyy-mm-dd\&quot;). | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**start_date** | None, str, date,  | NoneClass, str,  | The pay period start date, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format: \&quot;yyyy-mm-dd\&quot;. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# distribution_breakdown

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DistributionBreakdown**](DistributionBreakdown.md) | [**DistributionBreakdown**](DistributionBreakdown.md) | [**DistributionBreakdown**](DistributionBreakdown.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

