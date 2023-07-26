# plaid.model.watchlist_screening_individual.WatchlistScreeningIndividual

The screening object allows you to represent a customer in your system, update their profile, and search for them on various watchlists. Note: Rejected customers will not receive new hits, regardless of program configuration.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The screening object allows you to represent a customer in your system, update their profile, and search for them on various watchlists. Note: Rejected customers will not receive new hits, regardless of program configuration. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**search_terms** | [**WatchlistScreeningSearchTerms**](WatchlistScreeningSearchTerms.md) | [**WatchlistScreeningSearchTerms**](WatchlistScreeningSearchTerms.md) |  | 
**audit_trail** | [**WatchlistScreeningAuditTrail**](WatchlistScreeningAuditTrail.md) | [**WatchlistScreeningAuditTrail**](WatchlistScreeningAuditTrail.md) |  | 
**client_user_id** | [**ClientUserIDNullable**](ClientUserIDNullable.md) | [**ClientUserIDNullable**](ClientUserIDNullable.md) |  | 
**assignee** | [**DashboardUserIDNullable**](DashboardUserIDNullable.md) | [**DashboardUserIDNullable**](DashboardUserIDNullable.md) |  | 
**id** | str,  | str,  | ID of the associated screening. | 
**status** | [**WatchlistScreeningStatus**](WatchlistScreeningStatus.md) | [**WatchlistScreeningStatus**](WatchlistScreeningStatus.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

