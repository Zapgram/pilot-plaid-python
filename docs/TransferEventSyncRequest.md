# TransferEventSyncRequest

Defines the request schema for `/transfer/event/sync`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after_id** | **int** | The latest (largest) &#x60;event_id&#x60; fetched via the sync endpoint, or 0 initially. | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**count** | **int, none_type** | The maximum number of transfer events to return. | [optional]  if omitted the server will use the default value of 25
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


