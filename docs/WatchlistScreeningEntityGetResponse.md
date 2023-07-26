# WatchlistScreeningEntityGetResponse

The entity screening object allows you to represent an entity in your system, update its profile, and search for it on various watchlists. Note: Rejected entity screenings will not receive new hits, regardless of entity program configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the associated entity screening. | 
**search_terms** | [**EntityWatchlistScreeningSearchTerms**](EntityWatchlistScreeningSearchTerms.md) |  | 
**assignee** | **str, none_type** | ID of the associated user. | 
**status** | [**WatchlistScreeningStatus**](WatchlistScreeningStatus.md) |  | 
**client_user_id** | [**ClientUserIDNullable**](ClientUserIDNullable.md) |  | 
**audit_trail** | [**WatchlistScreeningAuditTrail**](WatchlistScreeningAuditTrail.md) |  | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


