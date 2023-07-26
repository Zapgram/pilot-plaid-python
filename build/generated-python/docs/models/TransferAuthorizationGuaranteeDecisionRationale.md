# plaid.model.transfer_authorization_guarantee_decision_rationale.TransferAuthorizationGuaranteeDecisionRationale

The rationale for Plaid's decision to not guarantee a transfer. Will be `null` unless `guarantee_decision` is `NOT_GUARANTEED`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The rationale for Plaid&#x27;s decision to not guarantee a transfer. Will be &#x60;null&#x60; unless &#x60;guarantee_decision&#x60; is &#x60;NOT_GUARANTEED&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | [**TransferAuthorizationGuaranteeDecisionRationaleCode**](TransferAuthorizationGuaranteeDecisionRationaleCode.md) | [**TransferAuthorizationGuaranteeDecisionRationaleCode**](TransferAuthorizationGuaranteeDecisionRationaleCode.md) |  | 
**description** | str,  | str,  | A human-readable description of why the transfer cannot be guaranteed. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

