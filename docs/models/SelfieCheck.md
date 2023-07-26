# plaid.model.selfie_check.SelfieCheck

Additional information for the `selfie_check` step. This field will be `null` unless `steps.selfie_check` has reached a terminal state of either `success` or `failed`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Additional information for the &#x60;selfie_check&#x60; step. This field will be &#x60;null&#x60; unless &#x60;steps.selfie_check&#x60; has reached a terminal state of either &#x60;success&#x60; or &#x60;failed&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[selfies](#selfies)** | list, tuple,  | tuple,  | An array of selfies submitted to the &#x60;selfie_check&#x60; step. Each entry represents one user submission. | 
**status** | [**SelfieCheckStatus**](SelfieCheckStatus.md) | [**SelfieCheckStatus**](SelfieCheckStatus.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# selfies

An array of selfies submitted to the `selfie_check` step. Each entry represents one user submission.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of selfies submitted to the &#x60;selfie_check&#x60; step. Each entry represents one user submission. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SelfieCheckSelfie**](SelfieCheckSelfie.md) | [**SelfieCheckSelfie**](SelfieCheckSelfie.md) | [**SelfieCheckSelfie**](SelfieCheckSelfie.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

