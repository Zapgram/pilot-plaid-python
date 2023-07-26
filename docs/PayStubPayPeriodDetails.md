# PayStubPayPeriodDetails

Details about the pay period.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_amount** | **float, none_type** | The amount of the paycheck. | 
**distribution_breakdown** | [**[PayStubDistributionBreakdown]**](PayStubDistributionBreakdown.md) |  | 
**end_date** | **date, none_type** | The date on which the pay period ended, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (\&quot;yyyy-mm-dd\&quot;). | 
**gross_earnings** | **float, none_type** | Total earnings before tax/deductions. | 
**iso_currency_code** | **str, none_type** | The ISO-4217 currency code of the net pay. Always &#x60;null&#x60; if &#x60;unofficial_currency_code&#x60; is non-null. | 
**pay_date** | **date, none_type** | The date on which the pay stub was issued, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (\&quot;yyyy-mm-dd\&quot;). | 
**pay_frequency** | **str, none_type** | The frequency at which an individual is paid. | 
**start_date** | **date, none_type** | The date on which the pay period started, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (\&quot;yyyy-mm-dd\&quot;). | 
**unofficial_currency_code** | **str, none_type** | The unofficial currency code associated with the net pay. Always &#x60;null&#x60; if &#x60;iso_currency_code&#x60; is non-&#x60;null&#x60;. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported &#x60;iso_currency_code&#x60;s. | 
**pay_basis** | [**CreditPayStubPayBasisType**](CreditPayStubPayBasisType.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


