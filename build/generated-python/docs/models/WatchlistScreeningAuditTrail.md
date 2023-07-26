# plaid.model.watchlist_screening_audit_trail.WatchlistScreeningAuditTrail

Information about the last change made to the parent object specifying what caused the change as well as when it occurred.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Information about the last change made to the parent object specifying what caused the change as well as when it occurred. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**source** | [**Source**](Source.md) | [**Source**](Source.md) |  | 
**dashboard_user_id** | [**DashboardUserIDNullable**](DashboardUserIDNullable.md) | [**DashboardUserIDNullable**](DashboardUserIDNullable.md) |  | 
**timestamp** | str, datetime,  | str,  | An ISO8601 formatted timestamp. | value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

