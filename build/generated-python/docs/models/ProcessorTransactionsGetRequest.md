# plaid.model.processor_transactions_get_request.ProcessorTransactionsGetRequest

ProcessorTransactionsGetRequest defines the request schema for `/processor/transactions/get`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ProcessorTransactionsGetRequest defines the request schema for &#x60;/processor/transactions/get&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**end_date** | str, date,  | str,  | The latest date for which data should be returned. Dates should be formatted as YYYY-MM-DD. | value must conform to RFC-3339 full-date YYYY-MM-DD
**processor_token** | str,  | str,  | The processor token obtained from the Plaid integration partner. Processor tokens are in the format: &#x60;processor-&lt;environment&gt;-&lt;identifier&gt;&#x60; | 
**start_date** | str, date,  | str,  | The earliest date for which data should be returned. Dates should be formatted as YYYY-MM-DD. | value must conform to RFC-3339 full-date YYYY-MM-DD
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**options** | [**TransactionsGetRequestOptions**](TransactionsGetRequestOptions.md) | [**TransactionsGetRequestOptions**](TransactionsGetRequestOptions.md) |  | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

