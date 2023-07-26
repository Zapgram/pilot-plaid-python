# plaid.model.item_activity_list_response.ItemActivityListResponse

Describes a historical log of user consent events.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Describes a historical log of user consent events. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[activities](#activities)** | list, tuple,  | tuple,  | A list of activities. | 
**[last_data_access_times](#last_data_access_times)** | list, tuple,  | tuple,  | An array of objects containing timestamps for the last time each data type was accessed per application. | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**cursor** | str,  | str,  | Cursor used for pagination. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# activities

A list of activities.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of activities. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Activity**](Activity.md) | [**Activity**](Activity.md) | [**Activity**](Activity.md) |  | 

# last_data_access_times

An array of objects containing timestamps for the last time each data type was accessed per application.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of objects containing timestamps for the last time each data type was accessed per application. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**LastDataAccessTimes**](LastDataAccessTimes.md) | [**LastDataAccessTimes**](LastDataAccessTimes.md) | [**LastDataAccessTimes**](LastDataAccessTimes.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

