# plaid.model.name_match_score.NameMatchScore

Score found by matching name provided by the API with the name on the account at the financial institution. If the account contains multiple owners, the maximum match score is filled.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Score found by matching name provided by the API with the name on the account at the financial institution. If the account contains multiple owners, the maximum match score is filled. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**score** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Match score for name. 100 is a perfect score, 85-99 means a strong match, 84-70 is a partial match, any score less than 70 is a mismatch. Typically, the match threshold should be set to a score of 70 or higher. If the name is missing from either the API or financial institution, this is null. | [optional] 
**is_first_name_or_last_name_match** | None, bool,  | NoneClass, BoolClass,  | first or last name completely matched, likely a family member | [optional] 
**is_nickname_match** | None, bool,  | NoneClass, BoolClass,  | nickname matched, example Jennifer and Jenn. | [optional] 
**is_business_name_detected** | None, bool,  | NoneClass, BoolClass,  | Is &#x60;true&#x60; if the name on either of the names that was matched for the score contained strings indicative of a business name, such as \&quot;CORP\&quot;, \&quot;LLC\&quot;, \&quot;INC\&quot;, or \&quot;LTD\&quot;. A &#x60;true&#x60; result generally indicates the entity is a business. However, a &#x60;false&#x60; result does not mean the entity is not a business, as some businesses do not use these strings in the names used for their financial institution accounts. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

