# plaid.model.risk_check_details.RiskCheckDetails

Additional information for the `risk_check` step.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Additional information for the &#x60;risk_check&#x60; step. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[devices](#devices)** | list, tuple,  | tuple,  | Array of result summary objects specifying values for &#x60;device&#x60; attributes of risk check. | 
**phone** | [**RiskCheckPhone**](RiskCheckPhone.md) | [**RiskCheckPhone**](RiskCheckPhone.md) |  | 
**behavior** | [**RiskCheckBehavior**](RiskCheckBehavior.md) | [**RiskCheckBehavior**](RiskCheckBehavior.md) |  | 
**identity_abuse_signals** | [**RiskCheckIdentityAbuseSignals**](RiskCheckIdentityAbuseSignals.md) | [**RiskCheckIdentityAbuseSignals**](RiskCheckIdentityAbuseSignals.md) |  | 
**email** | [**RiskCheckEmail**](RiskCheckEmail.md) | [**RiskCheckEmail**](RiskCheckEmail.md) |  | 
**status** | [**IdentityVerificationStepStatus**](IdentityVerificationStepStatus.md) | [**IdentityVerificationStepStatus**](IdentityVerificationStepStatus.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# devices

Array of result summary objects specifying values for `device` attributes of risk check.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of result summary objects specifying values for &#x60;device&#x60; attributes of risk check. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RiskCheckDevice**](RiskCheckDevice.md) | [**RiskCheckDevice**](RiskCheckDevice.md) | [**RiskCheckDevice**](RiskCheckDevice.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

