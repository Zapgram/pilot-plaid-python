# plaid.model.fdx_notification_payload.FDXNotificationPayload

Custom key-value pairs payload for a notification

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Custom key-value pairs payload for a notification | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | ID for the origination entity related to the notification | [optional] 
**idType** | [**FDXNotificationPayloadIdType**](FDXNotificationPayloadIdType.md) | [**FDXNotificationPayloadIdType**](FDXNotificationPayloadIdType.md) |  | [optional] 
**[customFields](#customFields)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# customFields

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FDXFiAttribute**](FDXFiAttribute.md) | [**FDXFiAttribute**](FDXFiAttribute.md) | [**FDXFiAttribute**](FDXFiAttribute.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

