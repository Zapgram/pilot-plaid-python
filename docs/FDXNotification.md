# FDXNotification

Provides the base fields of a notification. Clients will read the `type` property to determine the expected notification payload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_id** | **str** | Id of notification | 
**type** | [**FDXNotificationType**](FDXNotificationType.md) |  | 
**sent_on** | **datetime** | ISO 8601 date-time in format &#39;YYYY-MM-DDThh:mm:ss.nnn[Z|[+|-]hh:mm]&#39; according to [IETF RFC3339](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14) | 
**category** | [**FDXNotificationCategory**](FDXNotificationCategory.md) |  | 
**publisher** | [**FDXParty**](FDXParty.md) |  | 
**notification_payload** | [**FDXNotificationPayload**](FDXNotificationPayload.md) |  | 
**severity** | [**FDXNotificationSeverity**](FDXNotificationSeverity.md) |  | [optional] 
**priority** | [**FDXNotificationPriority**](FDXNotificationPriority.md) |  | [optional] 
**subscriber** | [**FDXParty**](FDXParty.md) |  | [optional] 
**url** | [**FDXHateoasLink**](FDXHateoasLink.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


