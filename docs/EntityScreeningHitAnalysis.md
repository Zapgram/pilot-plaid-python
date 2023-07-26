# EntityScreeningHitAnalysis

Analysis information describing why a screening hit matched the provided entity information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_terms_version** | **int** | The version of the entity screening&#39;s &#x60;search_terms&#x60; that were compared when the entity screening hit was added. entity screening hits are immutable once they have been reviewed. If changes are detected due to updates to the entity screening&#39;s &#x60;search_terms&#x60;, the associated entity program, or the list&#39;s source data prior to review, the entity screening hit will be updated to reflect those changes. | 
**documents** | [**MatchSummaryCode**](MatchSummaryCode.md) |  | [optional] 
**email_addresses** | [**MatchSummaryCode**](MatchSummaryCode.md) |  | [optional] 
**locations** | [**MatchSummaryCode**](MatchSummaryCode.md) |  | [optional] 
**names** | [**MatchSummaryCode**](MatchSummaryCode.md) |  | [optional] 
**phone_numbers** | [**MatchSummaryCode**](MatchSummaryCode.md) |  | [optional] 
**urls** | [**MatchSummaryCode**](MatchSummaryCode.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


