# plaid.model.risk_check_identity_abuse_signals.RiskCheckIdentityAbuseSignals

Result summary object capturing abuse signals related to `identity abuse`, e.g. stolen and synthetic identity fraud.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Result summary object capturing abuse signals related to &#x60;identity abuse&#x60;, e.g. stolen and synthetic identity fraud. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**synthetic_identity** | [**RiskCheckSyntheticIdentity**](RiskCheckSyntheticIdentity.md) | [**RiskCheckSyntheticIdentity**](RiskCheckSyntheticIdentity.md) |  | 
**stolen_identity** | [**RiskCheckStolenIdentity**](RiskCheckStolenIdentity.md) | [**RiskCheckStolenIdentity**](RiskCheckStolenIdentity.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

