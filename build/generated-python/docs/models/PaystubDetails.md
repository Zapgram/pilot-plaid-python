# plaid.model.paystub_details.PaystubDetails

An object representing details that can be found on the paystub.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing details that can be found on the paystub. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**pay_period_start_date** | None, str, date,  | NoneClass, str,  | Beginning date of the pay period on the paystub in the &#x27;YYYY-MM-DD&#x27; format. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**pay_period_end_date** | None, str, date,  | NoneClass, str,  | Ending date of the pay period on the paystub in the &#x27;YYYY-MM-DD&#x27; format. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**pay_date** | None, str, date,  | NoneClass, str,  | Pay date on the paystub in the &#x27;YYYY-MM-DD&#x27; format. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**paystub_provider** | None, str,  | NoneClass, str,  | The name of the payroll provider that generated the paystub, e.g. ADP | [optional] 
**pay_frequency** | [**PaystubPayFrequency**](PaystubPayFrequency.md) | [**PaystubPayFrequency**](PaystubPayFrequency.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

