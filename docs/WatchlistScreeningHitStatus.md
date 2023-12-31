# WatchlistScreeningHitStatus

The current state of review. All watchlist screening hits begin in a `pending_review` state but can be changed by creating a review. When a hit is in the `pending_review` state, it will always show the latest version of the watchlist data Plaid has available and be compared against the latest customer information saved in the watchlist screening. Once a hit has been marked as `confirmed` or `dismissed` it will no longer be updated so that the state is as it was when the review was first conducted.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The current state of review. All watchlist screening hits begin in a &#x60;pending_review&#x60; state but can be changed by creating a review. When a hit is in the &#x60;pending_review&#x60; state, it will always show the latest version of the watchlist data Plaid has available and be compared against the latest customer information saved in the watchlist screening. Once a hit has been marked as &#x60;confirmed&#x60; or &#x60;dismissed&#x60; it will no longer be updated so that the state is as it was when the review was first conducted. |  must be one of ["confirmed", "pending_review", "dismissed", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


