# Activity

Describes a consent activity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**ActivityType**](ActivityType.md) |  | 
**initiated_date** | **date** | The date this activity was initiated [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format in UTC. | 
**id** | **str** | A unique identifier for the activity | 
**initiator** | **str** | Application ID of the client who initiated the activity. | 
**state** | [**ActionState**](ActionState.md) |  | 
**target_application_id** | **str** | This field will map to the application ID that is returned from /item/applications/list, or provided to the institution in an oauth redirect. | [optional] 
**scopes** | [**ScopesNullable**](ScopesNullable.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


