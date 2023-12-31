# ProcessorTransactionsGetRequest

ProcessorTransactionsGetRequest defines the request schema for `/processor/transactions/get`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processor_token** | **str** | The processor token obtained from the Plaid integration partner. Processor tokens are in the format: &#x60;processor-&lt;environment&gt;-&lt;identifier&gt;&#x60; | 
**start_date** | **date** | The earliest date for which data should be returned. Dates should be formatted as YYYY-MM-DD. | 
**end_date** | **date** | The latest date for which data should be returned. Dates should be formatted as YYYY-MM-DD. | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**options** | [**TransactionsGetRequestOptions**](TransactionsGetRequestOptions.md) |  | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


