# plaid.model.screening_hit_analysis.ScreeningHitAnalysis

Analysis information describing why a screening hit matched the provided user information

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Analysis information describing why a screening hit matched the provided user information | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**search_terms_version** | decimal.Decimal, int,  | decimal.Decimal,  | The version of the screening&#x27;s &#x60;search_terms&#x60; that were compared when the screening hit was added. screening hits are immutable once they have been reviewed. If changes are detected due to updates to the screening&#x27;s &#x60;search_terms&#x60;, the associated program, or the list&#x27;s source data prior to review, the screening hit will be updated to reflect those changes. | 
**dates_of_birth** | [**MatchSummaryCode**](MatchSummaryCode.md) | [**MatchSummaryCode**](MatchSummaryCode.md) |  | [optional] 
**documents** | [**MatchSummaryCode**](MatchSummaryCode.md) | [**MatchSummaryCode**](MatchSummaryCode.md) |  | [optional] 
**locations** | [**MatchSummaryCode**](MatchSummaryCode.md) | [**MatchSummaryCode**](MatchSummaryCode.md) |  | [optional] 
**names** | [**MatchSummaryCode**](MatchSummaryCode.md) | [**MatchSummaryCode**](MatchSummaryCode.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

