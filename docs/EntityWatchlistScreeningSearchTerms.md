# EntityWatchlistScreeningSearchTerms

Search terms associated with an entity used for searching against watchlists

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_watchlist_program_id** | **str** | ID of the associated entity program. | 
**legal_name** | [**EntityWatchlistScreeningName**](EntityWatchlistScreeningName.md) |  | 
**document_number** | [**WatchlistScreeningDocumentValueNullable**](WatchlistScreeningDocumentValueNullable.md) |  | 
**email_address** | **str, none_type** | A valid email address. | 
**country** | [**GenericCountryCodeNullable**](GenericCountryCodeNullable.md) |  | 
**phone_number** | **str, none_type** | A phone number in E.164 format. | 
**url** | **str, none_type** | An &#39;http&#39; or &#39;https&#39; URL (must begin with either of those). | 
**version** | **int** | The current version of the search terms. Starts at &#x60;1&#x60; and increments with each edit to &#x60;search_terms&#x60;. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


