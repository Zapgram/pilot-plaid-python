# WatchlistScreeningEntityProgramGetResponse

A program that configures the active lists, search parameters, and other behavior for initial and ongoing screening of entities.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the associated entity program. | 
**created_at** | **datetime** | An ISO8601 formatted timestamp. | 
**is_rescanning_enabled** | **bool** | Indicator specifying whether the program is enabled and will perform daily rescans. | 
**lists_enabled** | [**[EntityWatchlistCode]**](EntityWatchlistCode.md) | Watchlists enabled for the associated program | 
**name** | [**EntityWatchlistScreeningProgramName**](EntityWatchlistScreeningProgramName.md) |  | 
**name_sensitivity** | [**ProgramNameSensitivity**](ProgramNameSensitivity.md) |  | 
**audit_trail** | [**WatchlistScreeningAuditTrail**](WatchlistScreeningAuditTrail.md) |  | 
**is_archived** | **bool** | Archived programs are read-only and cannot screen new customers nor participate in ongoing monitoring. | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


