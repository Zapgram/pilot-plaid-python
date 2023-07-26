# plaid.model.transfer_configuration_get_response.TransferConfigurationGetResponse

Defines the response schema for `/transfer/configuration/get`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines the response schema for &#x60;/transfer/configuration/get&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**max_daily_credit_amount** | str,  | str,  | The max limit of sum of dollar amount of credit transfers in last 24 hours (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**max_daily_debit_amount** | str,  | str,  | The max limit of sum of dollar amount of debit transfers in last 24 hours (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**max_single_transfer_debit_amount** | str,  | str,  | The max limit of dollar amount of a single debit transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**max_monthly_debit_amount** | str,  | str,  | The max limit of sum of dollar amount of debit transfers in one calendar month (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**iso_currency_code** | str,  | str,  | The currency of the dollar amount, e.g. \&quot;USD\&quot;. | 
**max_monthly_credit_amount** | str,  | str,  | The max limit of sum of dollar amount of credit transfers in one calendar month (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**max_single_transfer_amount** | str,  | str,  | The max limit of dollar amount of a single transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**max_single_transfer_credit_amount** | str,  | str,  | The max limit of dollar amount of a single credit transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**max_monthly_amount** | str,  | str,  | The max limit of sum of dollar amount of credit and debit transfers in one calendar month (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

