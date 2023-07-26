# plaid.model.watchlist_screening_entity_history_list_response.WatchlistScreeningEntityHistoryListResponse

Paginated list of entity watchlist screenings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Paginated list of entity watchlist screenings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**next_cursor** | [**Cursor**](Cursor.md) | [**Cursor**](Cursor.md) |  | 
**[entity_watchlist_screenings](#entity_watchlist_screenings)** | list, tuple,  | tuple,  | List of entity watchlist screening | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# entity_watchlist_screenings

List of entity watchlist screening

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of entity watchlist screening | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EntityWatchlistScreening**](EntityWatchlistScreening.md) | [**EntityWatchlistScreening**](EntityWatchlistScreening.md) | [**EntityWatchlistScreening**](EntityWatchlistScreening.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

