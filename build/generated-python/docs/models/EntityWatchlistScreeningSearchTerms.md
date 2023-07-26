# plaid.model.entity_watchlist_screening_search_terms.EntityWatchlistScreeningSearchTerms

Search terms associated with an entity used for searching against watchlists

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Search terms associated with an entity used for searching against watchlists | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**country** | [**GenericCountryCodeNullable**](GenericCountryCodeNullable.md) | [**GenericCountryCodeNullable**](GenericCountryCodeNullable.md) |  | 
**document_number** | [**WatchlistScreeningDocumentValueNullable**](WatchlistScreeningDocumentValueNullable.md) | [**WatchlistScreeningDocumentValueNullable**](WatchlistScreeningDocumentValueNullable.md) |  | 
**email_address** | [**EmailAddressNullable**](EmailAddressNullable.md) | [**EmailAddressNullable**](EmailAddressNullable.md) |  | 
**entity_watchlist_program_id** | str,  | str,  | ID of the associated entity program. | 
**phone_number** | [**WatchlistScreeningPhoneNumberNullable**](WatchlistScreeningPhoneNumberNullable.md) | [**WatchlistScreeningPhoneNumberNullable**](WatchlistScreeningPhoneNumberNullable.md) |  | 
**legal_name** | [**EntityWatchlistScreeningName**](EntityWatchlistScreeningName.md) | [**EntityWatchlistScreeningName**](EntityWatchlistScreeningName.md) |  | 
**version** | decimal.Decimal, int,  | decimal.Decimal,  | The current version of the search terms. Starts at &#x60;1&#x60; and increments with each edit to &#x60;search_terms&#x60;. | 
**url** | [**URLNullable**](URLNullable.md) | [**URLNullable**](URLNullable.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

