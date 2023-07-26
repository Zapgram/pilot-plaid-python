# plaid.model.transfer_authorization_decision_rationale.TransferAuthorizationDecisionRationale

The rationale for Plaid's decision regarding a proposed transfer. It is always set for `declined` decisions, and may or may not be null for `approved` decisions.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The rationale for Plaid&#x27;s decision regarding a proposed transfer. It is always set for &#x60;declined&#x60; decisions, and may or may not be null for &#x60;approved&#x60; decisions. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | [**TransferAuthorizationDecisionRationaleCode**](TransferAuthorizationDecisionRationaleCode.md) | [**TransferAuthorizationDecisionRationaleCode**](TransferAuthorizationDecisionRationaleCode.md) |  | 
**description** | str,  | str,  | A human-readable description of the code associated with a transfer approval or transfer decline. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

