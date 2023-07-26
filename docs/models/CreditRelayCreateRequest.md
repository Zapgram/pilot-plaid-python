# plaid.model.credit_relay_create_request.CreditRelayCreateRequest

CreditRelayCreateRequest defines the request schema for `/credit/relay/create`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | CreditRelayCreateRequest defines the request schema for &#x60;/credit/relay/create&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[report_tokens](#report_tokens)** | list, tuple,  | tuple,  | List of report token strings, with at most one token of each report type. Currently only Asset Report token is supported. | 
**secondary_client_id** | str,  | str,  | The &#x60;secondary_client_id&#x60; is the client id of the third party with whom you would like to share the relay token. | 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**webhook** | None, str,  | NoneClass, str,  | URL to which Plaid will send webhooks when the Secondary Client successfully retrieves an Asset Report by calling &#x60;/credit/relay/get&#x60;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# report_tokens

List of report token strings, with at most one token of each report type. Currently only Asset Report token is supported.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of report token strings, with at most one token of each report type. Currently only Asset Report token is supported. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The report token. It can only be an asset report token token. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

