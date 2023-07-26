# ItemActivityListResponse

Describes a historical log of user consent events.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**activities** | [**[Activity]**](Activity.md) | A list of activities. | 
**last_data_access_times** | [**[LastDataAccessTimes]**](LastDataAccessTimes.md) | An array of objects containing timestamps for the last time each data type was accessed per application. | 
**cursor** | **str** | Cursor used for pagination. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


