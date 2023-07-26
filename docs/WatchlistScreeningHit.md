# WatchlistScreeningHit

Data from a government watchlist or PEP list that has been attached to the screening.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the associated screening hit. | 
**review_status** | [**WatchlistScreeningHitStatus**](WatchlistScreeningHitStatus.md) |  | 
**first_active** | **datetime** | An ISO8601 formatted timestamp. | 
**inactive_since** | **datetime, none_type** | An ISO8601 formatted timestamp. | 
**historical_since** | **datetime, none_type** | An ISO8601 formatted timestamp. | 
**list_code** | [**IndividualWatchlistCode**](IndividualWatchlistCode.md) |  | 
**plaid_uid** | **str** | A universal identifier for a watchlist individual that is stable across searches and updates. | 
**source_uid** | [**SourceUID**](SourceUID.md) |  | 
**analysis** | [**ScreeningHitAnalysis**](ScreeningHitAnalysis.md) |  | [optional] 
**data** | [**ScreeningHitData**](ScreeningHitData.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


