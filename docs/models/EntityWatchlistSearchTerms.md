# plaid.model.entity_watchlist_search_terms.EntityWatchlistSearchTerms

Search inputs for creating an entity watchlist screening

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Search inputs for creating an entity watchlist screening | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**entity_watchlist_program_id** | str,  | str,  | ID of the associated entity program. | 
**legal_name** | [**EntityWatchlistScreeningName**](EntityWatchlistScreeningName.md) | [**EntityWatchlistScreeningName**](EntityWatchlistScreeningName.md) |  | 
**document_number** | [**WatchlistScreeningDocumentValueNullable**](WatchlistScreeningDocumentValueNullable.md) | [**WatchlistScreeningDocumentValueNullable**](WatchlistScreeningDocumentValueNullable.md) |  | [optional] 
**email_address** | [**EmailAddressNullable**](EmailAddressNullable.md) | [**EmailAddressNullable**](EmailAddressNullable.md) |  | [optional] 
**country** | [**GenericCountryCodeNullable**](GenericCountryCodeNullable.md) | [**GenericCountryCodeNullable**](GenericCountryCodeNullable.md) |  | [optional] 
**phone_number** | [**WatchlistScreeningPhoneNumberNullable**](WatchlistScreeningPhoneNumberNullable.md) | [**WatchlistScreeningPhoneNumberNullable**](WatchlistScreeningPhoneNumberNullable.md) |  | [optional] 
**url** | [**URLNullable**](URLNullable.md) | [**URLNullable**](URLNullable.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

