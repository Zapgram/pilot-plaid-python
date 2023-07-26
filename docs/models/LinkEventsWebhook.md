# plaid.model.link_events_webhook.LinkEventsWebhook

Contains a summary of the events from a link session

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Contains a summary of the events from a link session | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**webhook_type** | str,  | str,  | &#x60;LINK&#x60; | 
**link_session_id** | str,  | str,  | An identifier for the link session these events occurred in | 
**link_token** | str,  | str,  | The link token used to create the link session these events are from | 
**webhook_code** | str,  | str,  | &#x60;EVENTS&#x60; | 
**[events](#events)** | list, tuple,  | tuple,  | The link events emitted during the link session | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# events

The link events emitted during the link session

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The link events emitted during the link session | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**LinkEvent**](LinkEvent.md) | [**LinkEvent**](LinkEvent.md) | [**LinkEvent**](LinkEvent.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

