# plaid.model.transfer_intent_get_failure_reason.TransferIntentGetFailureReason

The reason for a failed transfer intent. Returned only if the transfer intent status is `failed`. Null otherwise.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The reason for a failed transfer intent. Returned only if the transfer intent status is &#x60;failed&#x60;. Null otherwise. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error_type** | str,  | str,  | A broad categorization of the error. | [optional] 
**error_code** | str,  | str,  | A code representing the reason for a failed transfer intent (i.e., an API error or the authorization being declined). | [optional] 
**error_message** | str,  | str,  | A human-readable description of the code associated with a failed transfer intent. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

