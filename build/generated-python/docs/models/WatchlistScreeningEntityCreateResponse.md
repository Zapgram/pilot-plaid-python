# plaid.model.watchlist_screening_entity_create_response.WatchlistScreeningEntityCreateResponse

The entity screening object allows you to represent an entity in your system, update its profile, and search for it on various watchlists. Note: Rejected entity screenings will not receive new hits, regardless of entity program configuration.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The entity screening object allows you to represent an entity in your system, update its profile, and search for it on various watchlists. Note: Rejected entity screenings will not receive new hits, regardless of entity program configuration. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**search_terms** | [**EntityWatchlistScreeningSearchTerms**](EntityWatchlistScreeningSearchTerms.md) | [**EntityWatchlistScreeningSearchTerms**](EntityWatchlistScreeningSearchTerms.md) |  | 
**audit_trail** | [**WatchlistScreeningAuditTrail**](WatchlistScreeningAuditTrail.md) | [**WatchlistScreeningAuditTrail**](WatchlistScreeningAuditTrail.md) |  | 
**client_user_id** | [**ClientUserIDNullable**](ClientUserIDNullable.md) | [**ClientUserIDNullable**](ClientUserIDNullable.md) |  | 
**assignee** | [**DashboardUserIDNullable**](DashboardUserIDNullable.md) | [**DashboardUserIDNullable**](DashboardUserIDNullable.md) |  | 
**id** | str,  | str,  | ID of the associated entity screening. | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**status** | [**WatchlistScreeningStatus**](WatchlistScreeningStatus.md) | [**WatchlistScreeningStatus**](WatchlistScreeningStatus.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

