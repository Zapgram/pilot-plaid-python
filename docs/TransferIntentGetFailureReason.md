# TransferIntentGetFailureReason

The reason for a failed transfer intent. Returned only if the transfer intent status is `failed`. Null otherwise.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_type** | **str** | A broad categorization of the error. | [optional] 
**error_code** | **str** | A code representing the reason for a failed transfer intent (i.e., an API error or the authorization being declined). | [optional] 
**error_message** | **str** | A human-readable description of the code associated with a failed transfer intent. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


