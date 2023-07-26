# plaid.model.fdx_notification.FDXNotification

Provides the base fields of a notification. Clients will read the `type` property to determine the expected notification payload

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Provides the base fields of a notification. Clients will read the &#x60;type&#x60; property to determine the expected notification payload | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**notificationPayload** | [**FDXNotificationPayload**](FDXNotificationPayload.md) | [**FDXNotificationPayload**](FDXNotificationPayload.md) |  | 
**sentOn** | str, datetime,  | str,  | ISO 8601 date-time in format &#x27;YYYY-MM-DDThh:mm:ss.nnn[Z|[+|-]hh:mm]&#x27; according to [IETF RFC3339](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14) | value must conform to RFC-3339 date-time
**publisher** | [**FDXParty**](FDXParty.md) | [**FDXParty**](FDXParty.md) |  | 
**notificationId** | str,  | str,  | Id of notification | 
**category** | [**FDXNotificationCategory**](FDXNotificationCategory.md) | [**FDXNotificationCategory**](FDXNotificationCategory.md) |  | 
**type** | [**FDXNotificationType**](FDXNotificationType.md) | [**FDXNotificationType**](FDXNotificationType.md) |  | 
**severity** | [**FDXNotificationSeverity**](FDXNotificationSeverity.md) | [**FDXNotificationSeverity**](FDXNotificationSeverity.md) |  | [optional] 
**priority** | [**FDXNotificationPriority**](FDXNotificationPriority.md) | [**FDXNotificationPriority**](FDXNotificationPriority.md) |  | [optional] 
**subscriber** | [**FDXParty**](FDXParty.md) | [**FDXParty**](FDXParty.md) |  | [optional] 
**url** | [**FDXHateoasLink**](FDXHateoasLink.md) | [**FDXHateoasLink**](FDXHateoasLink.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

