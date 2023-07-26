# WatchlistScreeningIndividualReviewCreateRequest

Request input for creating a screening review

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmed_hits** | **[str]** | Hits to mark as a true positive after thorough manual review. These hits will never recur or be updated once dismissed. In most cases, confirmed hits indicate that the customer should be rejected. | 
**dismissed_hits** | **[str]** | Hits to mark as a false positive after thorough manual review. These hits will never recur or be updated once dismissed. | 
**watchlist_screening_id** | **str** | ID of the associated screening. | 
**comment** | [**ReviewComment**](ReviewComment.md) |  | [optional] 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

