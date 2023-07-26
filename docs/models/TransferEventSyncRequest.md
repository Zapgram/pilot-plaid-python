# plaid.model.transfer_event_sync_request.TransferEventSyncRequest

Defines the request schema for `/transfer/event/sync`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines the request schema for &#x60;/transfer/event/sync&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**after_id** | decimal.Decimal, int,  | decimal.Decimal,  | The latest (largest) &#x60;event_id&#x60; fetched via the sync endpoint, or 0 initially. | 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**count** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The maximum number of transfer events to return. | [optional] if omitted the server will use the default value of 25
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
