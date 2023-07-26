# plaid.model.processor_balance_get_request_options.ProcessorBalanceGetRequestOptions

An optional object to filter `/processor/balance/get` results.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An optional object to filter &#x60;/processor/balance/get&#x60; results. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**min_last_updated_datetime** | str, datetime,  | str,  | Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDTHH:mm:ssZ&#x60;) indicating the oldest acceptable balance when making a request to &#x60;/accounts/balance/get&#x60;.  If the balance that is pulled for &#x60;ins_128026&#x60; (Capital One) is older than the given timestamp, an &#x60;INVALID_REQUEST&#x60; error with the code of &#x60;LAST_UPDATED_DATETIME_OUT_OF_RANGE&#x60; will be returned with the most recent timestamp for the requested account contained in the response.  This field is only used when the institution is &#x60;ins_128026&#x60; (Capital One), in which case a value must be provided or an &#x60;INVALID_REQUEST&#x60; error with the code of &#x60;INVALID_FIELD&#x60; will be returned. For all other institutions, this field is ignored. | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
