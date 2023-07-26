# plaid.model.update_individual_screening_request_search_terms.UpdateIndividualScreeningRequestSearchTerms

Search terms for editing an individual watchlist screening

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Search terms for editing an individual watchlist screening | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**watchlist_program_id** | str,  | str,  | ID of the associated program. | [optional] 
**legal_name** | [**WatchlistScreeningIndividualName**](WatchlistScreeningIndividualName.md) | [**WatchlistScreeningIndividualName**](WatchlistScreeningIndividualName.md) |  | [optional] 
**date_of_birth** | str, date,  | str,  | A date in the format YYYY-MM-DD (RFC 3339 Section 5.6). | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**document_number** | [**WatchlistScreeningDocumentValue**](WatchlistScreeningDocumentValue.md) | [**WatchlistScreeningDocumentValue**](WatchlistScreeningDocumentValue.md) |  | [optional] 
**country** | [**GenericCountryCode**](GenericCountryCode.md) | [**GenericCountryCode**](GenericCountryCode.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

