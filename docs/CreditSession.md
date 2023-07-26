# CreditSession

Metadata and results for a Link session

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_session_id** | **str** | The unique identifier associated with the Link session. This identifier matches the &#x60;link_session_id&#x60; returned in the onSuccess/onExit callbacks. | [optional] 
**session_start_time** | **datetime** | The time when the Link session started | [optional] 
**results** | [**CreditSessionResults**](CreditSessionResults.md) |  | [optional] 
**errors** | [**[CreditSessionError]**](CreditSessionError.md) | The set of errors that occurred during the Link session. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


