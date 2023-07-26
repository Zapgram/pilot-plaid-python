# LinkEventsWebhook

Contains a summary of the events from a link session

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;LINK&#x60; | 
**webhook_code** | **str** | &#x60;EVENTS&#x60; | 
**events** | [**[LinkEvent]**](LinkEvent.md) | The link events emitted during the link session | 
**link_session_id** | **str** | An identifier for the link session these events occurred in | 
**link_token** | **str** | The link token used to create the link session these events are from | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


