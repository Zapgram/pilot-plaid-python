# WatchlistScreeningIndividual

The screening object allows you to represent a customer in your system, update their profile, and search for them on various watchlists. Note: Rejected customers will not receive new hits, regardless of program configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the associated screening. | 
**search_terms** | [**WatchlistScreeningSearchTerms**](WatchlistScreeningSearchTerms.md) |  | 
**assignee** | **str, none_type** | ID of the associated user. | 
**status** | [**WatchlistScreeningStatus**](WatchlistScreeningStatus.md) |  | 
**client_user_id** | [**ClientUserIDNullable**](ClientUserIDNullable.md) |  | 
**audit_trail** | [**WatchlistScreeningAuditTrail**](WatchlistScreeningAuditTrail.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


