# IncomeVerificationPrecheckResponse

IncomeVerificationPrecheckResponse defines the response schema for `/income/verification/precheck`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**precheck_id** | **str** | ID of the precheck. Provide this value when calling &#x60;/link/token/create&#x60; in order to optimize Link conversion. | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**confidence** | [**IncomeVerificationPrecheckConfidence**](IncomeVerificationPrecheckConfidence.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


