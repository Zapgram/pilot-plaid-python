# EntityWatchlistScreeningHit

Data from a government watchlist that has been attached to the screening.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the associated entity screening hit. | 
**review_status** | [**WatchlistScreeningHitStatus**](WatchlistScreeningHitStatus.md) |  | 
**first_active** | **datetime** | An ISO8601 formatted timestamp. | 
**inactive_since** | **datetime, none_type** | An ISO8601 formatted timestamp. | 
**historical_since** | **datetime, none_type** | An ISO8601 formatted timestamp. | 
**list_code** | [**EntityWatchlistCode**](EntityWatchlistCode.md) |  | 
**plaid_uid** | **str** | A universal identifier for a watchlist individual that is stable across searches and updates. | 
**source_uid** | [**SourceUID**](SourceUID.md) |  | 
**analysis** | [**EntityScreeningHitAnalysis**](EntityScreeningHitAnalysis.md) |  | [optional] 
**data** | [**EntityScreeningHitData**](EntityScreeningHitData.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


