# LinkUserDeliveryStatusWebhook

Webhook indicating that the status of the delivery of the hosted link session to a user

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;LINK_DELIVERY&#x60; | 
**webhook_code** | **str** | &#x60;DELIVERY_STATUS&#x60; | 
**link_delivery_session_id** | **str** | The ID of the Hosted Link session. | 
**timestamp** | **str** | Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. | 
**link_delivery_metadata** | [**LinkDeliveryMetadata**](LinkDeliveryMetadata.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


