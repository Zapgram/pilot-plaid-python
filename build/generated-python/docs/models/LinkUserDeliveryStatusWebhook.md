# plaid.model.link_user_delivery_status_webhook.LinkUserDeliveryStatusWebhook

Webhook indicating that the status of the delivery of the hosted link session to a user

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Webhook indicating that the status of the delivery of the hosted link session to a user | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**link_delivery_metadata** | [**LinkDeliveryMetadata**](LinkDeliveryMetadata.md) | [**LinkDeliveryMetadata**](LinkDeliveryMetadata.md) |  | 
**webhook_type** | str,  | str,  | &#x60;LINK_DELIVERY&#x60; | 
**link_delivery_session_id** | str,  | str,  | The ID of the Hosted Link session. | 
**webhook_code** | str,  | str,  | &#x60;DELIVERY_STATUS&#x60; | 
**timestamp** | str,  | str,  | Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

