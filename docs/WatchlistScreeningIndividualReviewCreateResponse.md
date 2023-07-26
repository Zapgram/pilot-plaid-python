# WatchlistScreeningIndividualReviewCreateResponse

A review submitted by a team member for an individual watchlist screening. A review can be either a comment on the current screening state, actions taken against hits attached to the watchlist screening, or both.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the associated review. | 
**confirmed_hits** | **[str]** | Hits marked as a true positive after thorough manual review. These hits will never recur or be updated once dismissed. In most cases, confirmed hits indicate that the customer should be rejected. | 
**dismissed_hits** | **[str]** | Hits marked as a false positive after thorough manual review. These hits will never recur or be updated once dismissed. | 
**comment** | [**ReviewComment**](ReviewComment.md) |  | 
**audit_trail** | [**WatchlistScreeningAuditTrail**](WatchlistScreeningAuditTrail.md) |  | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


