# plaid.model.connected_application.ConnectedApplication

Describes the connected application for a particular end user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Describes the connected application for a particular end user. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The name of the application | 
**created_at** | str, date,  | str,  | The date this application was linked in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format in UTC. | value must conform to RFC-3339 full-date YYYY-MM-DD
**application_id** | str,  | str,  | This field will map to the application ID that is returned from /item/applications/list, or provided to the institution in an oauth redirect. | 
**display_name** | None, str,  | NoneClass, str,  | A human-readable name of the application for display purposes | [optional] 
**logo_url** | None, str,  | NoneClass, str,  | A URL that links to the application logo image. | [optional] 
**application_url** | None, str,  | NoneClass, str,  | The URL for the application&#x27;s website | [optional] 
**reason_for_access** | None, str,  | NoneClass, str,  | A string provided by the connected app stating why they use their respective enabled products. | [optional] 
**scopes** | [**ScopesNullable**](ScopesNullable.md) | [**ScopesNullable**](ScopesNullable.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

