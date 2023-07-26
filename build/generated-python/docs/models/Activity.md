# plaid.model.activity.Activity

Describes a consent activity.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Describes a consent activity. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**activity** | [**ActivityType**](ActivityType.md) | [**ActivityType**](ActivityType.md) |  | 
**initiator** | str,  | str,  | Application ID of the client who initiated the activity. | 
**initiated_date** | str, date,  | str,  | The date this activity was initiated [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format in UTC. | value must conform to RFC-3339 full-date YYYY-MM-DD
**id** | str,  | str,  | A unique identifier for the activity | 
**state** | [**ActionState**](ActionState.md) | [**ActionState**](ActionState.md) |  | 
**target_application_id** | str,  | str,  | This field will map to the application ID that is returned from /item/applications/list, or provided to the institution in an oauth redirect. | [optional] 
**scopes** | [**ScopesNullable**](ScopesNullable.md) | [**ScopesNullable**](ScopesNullable.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

