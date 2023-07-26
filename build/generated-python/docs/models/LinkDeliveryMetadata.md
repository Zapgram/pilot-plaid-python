# plaid.model.link_delivery_metadata.LinkDeliveryMetadata

Information related to the related to the delivery of the link session to users

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Information related to the related to the delivery of the link session to users | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**communication_method** | [**LinkDeliveryWebhookCommunicationMethod**](LinkDeliveryWebhookCommunicationMethod.md) | [**LinkDeliveryWebhookCommunicationMethod**](LinkDeliveryWebhookCommunicationMethod.md) |  | [optional] 
**delivery_status** | [**LinkDeliveryWebhookDeliveryStatus**](LinkDeliveryWebhookDeliveryStatus.md) | [**LinkDeliveryWebhookDeliveryStatus**](LinkDeliveryWebhookDeliveryStatus.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

