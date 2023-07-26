# WatchlistScreeningSearchTerms

Search terms for creating an individual watchlist screening

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**watchlist_program_id** | **str** | ID of the associated program. | 
**legal_name** | [**WatchlistScreeningIndividualName**](WatchlistScreeningIndividualName.md) |  | 
**date_of_birth** | **date, none_type** | A date in the format YYYY-MM-DD (RFC 3339 Section 5.6). | 
**document_number** | [**WatchlistScreeningDocumentValueNullable**](WatchlistScreeningDocumentValueNullable.md) |  | 
**country** | [**GenericCountryCodeNullable**](GenericCountryCodeNullable.md) |  | 
**version** | **int** | The current version of the search terms. Starts at &#x60;1&#x60; and increments with each edit to &#x60;search_terms&#x60;. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


