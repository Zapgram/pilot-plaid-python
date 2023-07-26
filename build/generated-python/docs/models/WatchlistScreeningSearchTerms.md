# plaid.model.watchlist_screening_search_terms.WatchlistScreeningSearchTerms

Search terms for creating an individual watchlist screening

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Search terms for creating an individual watchlist screening | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**country** | [**GenericCountryCodeNullable**](GenericCountryCodeNullable.md) | [**GenericCountryCodeNullable**](GenericCountryCodeNullable.md) |  | 
**watchlist_program_id** | str,  | str,  | ID of the associated program. | 
**document_number** | [**WatchlistScreeningDocumentValueNullable**](WatchlistScreeningDocumentValueNullable.md) | [**WatchlistScreeningDocumentValueNullable**](WatchlistScreeningDocumentValueNullable.md) |  | 
**date_of_birth** | [**ISO8601DateNullable**](ISO8601DateNullable.md) | [**ISO8601DateNullable**](ISO8601DateNullable.md) |  | 
**legal_name** | [**WatchlistScreeningIndividualName**](WatchlistScreeningIndividualName.md) | [**WatchlistScreeningIndividualName**](WatchlistScreeningIndividualName.md) |  | 
**version** | decimal.Decimal, int,  | decimal.Decimal,  | The current version of the search terms. Starts at &#x60;1&#x60; and increments with each edit to &#x60;search_terms&#x60;. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

