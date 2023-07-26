# TransferConfigurationGetResponse

Defines the response schema for `/transfer/configuration/get`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**max_single_transfer_amount** | **str** | The max limit of dollar amount of a single transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**max_single_transfer_credit_amount** | **str** | The max limit of dollar amount of a single credit transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**max_single_transfer_debit_amount** | **str** | The max limit of dollar amount of a single debit transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**max_daily_credit_amount** | **str** | The max limit of sum of dollar amount of credit transfers in last 24 hours (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**max_daily_debit_amount** | **str** | The max limit of sum of dollar amount of debit transfers in last 24 hours (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**max_monthly_amount** | **str** | The max limit of sum of dollar amount of credit and debit transfers in one calendar month (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**max_monthly_credit_amount** | **str** | The max limit of sum of dollar amount of credit transfers in one calendar month (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**max_monthly_debit_amount** | **str** | The max limit of sum of dollar amount of debit transfers in one calendar month (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**iso_currency_code** | **str** | The currency of the dollar amount, e.g. \&quot;USD\&quot;. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


