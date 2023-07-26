# WatchlistScreeningIndividualUpdateRequest

Request input for editing an individual watchlist screening

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**watchlist_screening_id** | **str** | ID of the associated screening. | 
**search_terms** | [**UpdateIndividualScreeningRequestSearchTerms**](UpdateIndividualScreeningRequestSearchTerms.md) |  | [optional] 
**assignee** | **str** | ID of the associated user. | [optional] 
**status** | [**WatchlistScreeningStatus**](WatchlistScreeningStatus.md) |  | [optional] 
**client_user_id** | [**ClientUserID**](ClientUserID.md) |  | [optional] 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**reset_fields** | [**WatchlistScreeningIndividualUpdateRequestResettableFieldList**](WatchlistScreeningIndividualUpdateRequestResettableFieldList.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


