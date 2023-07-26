# plaid.model.dashboard_user.DashboardUser

Account information associated with a team member with access to the Plaid dashboard.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Account information associated with a team member with access to the Plaid dashboard. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**email_address** | str,  | str,  | A valid email address. | 
**created_at** | str, datetime,  | str,  | An ISO8601 formatted timestamp. | value must conform to RFC-3339 date-time
**id** | str,  | str,  | ID of the associated user. | 
**status** | [**DashboardUserStatus**](DashboardUserStatus.md) | [**DashboardUserStatus**](DashboardUserStatus.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

