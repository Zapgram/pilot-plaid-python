# plaid.model.watchlist_screening_entity_list_request.WatchlistScreeningEntityListRequest

Request input for listing entity watchlist screenings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Request input for listing entity watchlist screenings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**entity_watchlist_program_id** | str,  | str,  | ID of the associated entity program. | 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**client_user_id** | [**ClientUserID**](ClientUserID.md) | [**ClientUserID**](ClientUserID.md) |  | [optional] 
**status** | [**WatchlistScreeningStatus**](WatchlistScreeningStatus.md) | [**WatchlistScreeningStatus**](WatchlistScreeningStatus.md) |  | [optional] 
**assignee** | str,  | str,  | ID of the associated user. | [optional] 
**cursor** | [**Cursor**](Cursor.md) | [**Cursor**](Cursor.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

