# SelfieCheck

Additional information for the `selfie_check` step. This field will be `null` unless `steps.selfie_check` has reached a terminal state of either `success` or `failed`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**SelfieCheckStatus**](SelfieCheckStatus.md) |  | 
**selfies** | [**[SelfieCheckSelfie]**](SelfieCheckSelfie.md) | An array of selfies submitted to the &#x60;selfie_check&#x60; step. Each entry represents one user submission. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


