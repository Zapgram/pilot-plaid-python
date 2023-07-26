# plaid.model.entity_watchlist_screening_hit.EntityWatchlistScreeningHit

Data from a government watchlist that has been attached to the screening.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data from a government watchlist that has been attached to the screening. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**inactive_since** | [**TimestampNullable**](TimestampNullable.md) | [**TimestampNullable**](TimestampNullable.md) |  | 
**plaid_uid** | str,  | str,  | A universal identifier for a watchlist individual that is stable across searches and updates. | 
**source_uid** | [**SourceUID**](SourceUID.md) | [**SourceUID**](SourceUID.md) |  | 
**first_active** | str, datetime,  | str,  | An ISO8601 formatted timestamp. | value must conform to RFC-3339 date-time
**id** | str,  | str,  | ID of the associated entity screening hit. | 
**review_status** | [**WatchlistScreeningHitStatus**](WatchlistScreeningHitStatus.md) | [**WatchlistScreeningHitStatus**](WatchlistScreeningHitStatus.md) |  | 
**list_code** | [**EntityWatchlistCode**](EntityWatchlistCode.md) | [**EntityWatchlistCode**](EntityWatchlistCode.md) |  | 
**historical_since** | [**TimestampNullable**](TimestampNullable.md) | [**TimestampNullable**](TimestampNullable.md) |  | 
**analysis** | [**EntityScreeningHitAnalysis**](EntityScreeningHitAnalysis.md) | [**EntityScreeningHitAnalysis**](EntityScreeningHitAnalysis.md) |  | [optional] 
**data** | [**EntityScreeningHitData**](EntityScreeningHitData.md) | [**EntityScreeningHitData**](EntityScreeningHitData.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

