# plaid.model.watchlist_screening_entity_program_get_response.WatchlistScreeningEntityProgramGetResponse

A program that configures the active lists, search parameters, and other behavior for initial and ongoing screening of entities.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A program that configures the active lists, search parameters, and other behavior for initial and ongoing screening of entities. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[lists_enabled](#lists_enabled)** | list, tuple,  | tuple,  | Watchlists enabled for the associated program | 
**audit_trail** | [**WatchlistScreeningAuditTrail**](WatchlistScreeningAuditTrail.md) | [**WatchlistScreeningAuditTrail**](WatchlistScreeningAuditTrail.md) |  | 
**is_archived** | bool,  | BoolClass,  | Archived programs are read-only and cannot screen new customers nor participate in ongoing monitoring. | 
**name** | [**EntityWatchlistScreeningProgramName**](EntityWatchlistScreeningProgramName.md) | [**EntityWatchlistScreeningProgramName**](EntityWatchlistScreeningProgramName.md) |  | 
**created_at** | str, datetime,  | str,  | An ISO8601 formatted timestamp. | value must conform to RFC-3339 date-time
**name_sensitivity** | [**ProgramNameSensitivity**](ProgramNameSensitivity.md) | [**ProgramNameSensitivity**](ProgramNameSensitivity.md) |  | 
**id** | str,  | str,  | ID of the associated entity program. | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**is_rescanning_enabled** | bool,  | BoolClass,  | Indicator specifying whether the program is enabled and will perform daily rescans. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# lists_enabled

Watchlists enabled for the associated program

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Watchlists enabled for the associated program | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EntityWatchlistCode**](EntityWatchlistCode.md) | [**EntityWatchlistCode**](EntityWatchlistCode.md) | [**EntityWatchlistCode**](EntityWatchlistCode.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

