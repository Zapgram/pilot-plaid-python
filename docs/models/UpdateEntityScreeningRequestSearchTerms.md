# plaid.model.update_entity_screening_request_search_terms.UpdateEntityScreeningRequestSearchTerms

Search terms for editing an entity watchlist screening

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Search terms for editing an entity watchlist screening | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**entity_watchlist_program_id** | str,  | str,  | ID of the associated entity program. | 
**legal_name** | [**EntityWatchlistScreeningName**](EntityWatchlistScreeningName.md) | [**EntityWatchlistScreeningName**](EntityWatchlistScreeningName.md) |  | [optional] 
**document_number** | [**WatchlistScreeningDocumentValue**](WatchlistScreeningDocumentValue.md) | [**WatchlistScreeningDocumentValue**](WatchlistScreeningDocumentValue.md) |  | [optional] 
**email_address** | str,  | str,  | A valid email address. | [optional] 
**country** | [**GenericCountryCode**](GenericCountryCode.md) | [**GenericCountryCode**](GenericCountryCode.md) |  | [optional] 
**phone_number** | str,  | str,  | A phone number in E.164 format. | [optional] 
**url** | str,  | str,  | An &#x27;http&#x27; or &#x27;https&#x27; URL (must begin with either of those). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

