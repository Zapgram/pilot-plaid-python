# PhoneNumberMatchScore

Score found by matching phone number provided by the API with the phone number on the account at the financial institution. 100 is a perfect match and 0 is a no match. If the account contains multiple owners, the maximum match score is filled.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **int, none_type** | Match score for normalized phone number. 100 is a perfect match, 99-70 is a partial match (matching the same phone number with extension against one without extension etc.), anything below 70 is considered a mismatch. Typically, the match threshold should be set to a score of 70 or higher. If the phone number is missing from either the API or financial institution, this is null. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


