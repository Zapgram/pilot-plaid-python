# AddressMatchScore

Score found by matching address provided by the API with the address on the account at the financial institution. The score can range from 0 to 100 where 100 is a perfect match and 0 is a no match. If the account contains multiple owners, the maximum match score is filled.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **int, none_type** | Match score for address. 100 is a perfect match, 99-90 is a strong match, 89-80 is a partial match, anything below 80 is considered a weak match. Typically, the match threshold should be set to a score of 80 or higher. If the address is missing from either the API or financial institution, this is null. | [optional] 
**is_postal_code_match** | **bool, none_type** | postal code was provided for both and was a match | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


