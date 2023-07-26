# plaid.model.deposit_switch_state_update_webhook.DepositSwitchStateUpdateWebhook

Fired when the status of a deposit switch request has changed.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Fired when the status of a deposit switch request has changed. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**webhook_type** | str,  | str,  | &#x60;\&quot;DEPOSIT_SWITCH\&quot;&#x60; | [optional] 
**webhook_code** | str,  | str,  | &#x60;\&quot;SWITCH_STATE_UPDATE\&quot;&#x60; | [optional] 
**state** | str,  | str,  | The state, or status, of the deposit switch.  &#x60;initialized&#x60;: The deposit switch has been initialized with the user entering the information required to submit the deposit switch request.  &#x60;processing&#x60;: The deposit switch request has been submitted and is being processed.  &#x60;completed&#x60;: The user&#x27;s employer has fulfilled and completed the deposit switch request.  &#x60;error&#x60;: There was an error processing the deposit switch request.  For more information, see the [Deposit Switch API reference](/docs/deposit-switch/reference#deposit_switchget). | [optional] 
**deposit_switch_id** | str,  | str,  | The ID of the deposit switch. | [optional] 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

