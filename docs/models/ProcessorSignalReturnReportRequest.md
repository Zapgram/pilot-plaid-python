# plaid.model.processor_signal_return_report_request.ProcessorSignalReturnReportRequest

ProcessorSignalReturnReportRequest defines the request schema for `/processor/signal/return/report`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ProcessorSignalReturnReportRequest defines the request schema for &#x60;/processor/signal/return/report&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**processor_token** | str,  | str,  | The processor token obtained from the Plaid integration partner. Processor tokens are in the format: &#x60;processor-&lt;environment&gt;-&lt;identifier&gt;&#x60; | 
**client_transaction_id** | str,  | str,  | Must be the same as the &#x60;client_transaction_id&#x60; supplied when calling &#x60;/processor/signal/evaluate&#x60; | 
**return_code** | str,  | str,  | Must be a valid ACH return code (e.g. \&quot;R01\&quot;)  If formatted incorrectly, this will result in an [&#x60;INVALID_FIELD&#x60;](/docs/errors/invalid-request/#invalid_field) error. | 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**returned_at** | None, str, datetime,  | NoneClass, str,  | Date and time when you receive the returns from your payment processors, in ISO 8601 format (&#x60;YYYY-MM-DDTHH:mm:ssZ&#x60;). | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

