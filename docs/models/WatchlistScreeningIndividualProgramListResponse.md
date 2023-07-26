# plaid.model.watchlist_screening_individual_program_list_response.WatchlistScreeningIndividualProgramListResponse

Paginated list of individual watchlist screening programs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Paginated list of individual watchlist screening programs | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**next_cursor** | [**Cursor**](Cursor.md) | [**Cursor**](Cursor.md) |  | 
**[watchlist_programs](#watchlist_programs)** | list, tuple,  | tuple,  | List of individual watchlist screening programs | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# watchlist_programs

List of individual watchlist screening programs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of individual watchlist screening programs | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IndividualWatchlistProgram**](IndividualWatchlistProgram.md) | [**IndividualWatchlistProgram**](IndividualWatchlistProgram.md) | [**IndividualWatchlistProgram**](IndividualWatchlistProgram.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

