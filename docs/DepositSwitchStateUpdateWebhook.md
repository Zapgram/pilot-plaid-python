# DepositSwitchStateUpdateWebhook

Fired when the status of a deposit switch request has changed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;\&quot;DEPOSIT_SWITCH\&quot;&#x60; | [optional] 
**webhook_code** | **str** | &#x60;\&quot;SWITCH_STATE_UPDATE\&quot;&#x60; | [optional] 
**state** | **str** | The state, or status, of the deposit switch.  &#x60;initialized&#x60;: The deposit switch has been initialized with the user entering the information required to submit the deposit switch request.  &#x60;processing&#x60;: The deposit switch request has been submitted and is being processed.  &#x60;completed&#x60;: The user&#39;s employer has fulfilled and completed the deposit switch request.  &#x60;error&#x60;: There was an error processing the deposit switch request.  For more information, see the [Deposit Switch API reference](/docs/deposit-switch/reference#deposit_switchget). | [optional] 
**deposit_switch_id** | **str** | The ID of the deposit switch. | [optional] 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


