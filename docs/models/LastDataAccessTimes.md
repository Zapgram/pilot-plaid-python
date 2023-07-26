# plaid.model.last_data_access_times.LastDataAccessTimes

Describes the last time each datatype was accessed by an application.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Describes the last time each datatype was accessed by an application. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account_routing_number** | None, str, datetime,  | NoneClass, str,  | The last time account_routing_number was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed. | value must conform to RFC-3339 date-time
**payroll_info** | None, str, datetime,  | NoneClass, str,  | The last time payroll_info was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed. | value must conform to RFC-3339 date-time
**transaction_risk_info** | None, str, datetime,  | NoneClass, str,  | The last time transaction_risk_info was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed. | value must conform to RFC-3339 date-time
**account_balance_info** | None, str, datetime,  | NoneClass, str,  | The last time account_balance_info was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed. | value must conform to RFC-3339 date-time
**credit_and_loans** | None, str, datetime,  | NoneClass, str,  | The last time credit_and_loans was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed. | value must conform to RFC-3339 date-time
**contact_details** | None, str, datetime,  | NoneClass, str,  | The last time contact_details was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed. | value must conform to RFC-3339 date-time
**investments** | None, str, datetime,  | NoneClass, str,  | The last time investments was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed. | value must conform to RFC-3339 date-time
**transactions** | None, str, datetime,  | NoneClass, str,  | The last time transactions was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed. | value must conform to RFC-3339 date-time
**application_id** | str,  | str,  | ID of the application accessing data. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

