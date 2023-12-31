# SandboxTransferSimulateRequest

Defines the request schema for `/sandbox/transfer/simulate`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_id** | **str** | Plaid’s unique identifier for a transfer. | 
**event_type** | **str** | The asynchronous event to be simulated. May be: &#x60;posted&#x60;, &#x60;settled&#x60;, &#x60;failed&#x60;, or &#x60;returned&#x60;.  An error will be returned if the event type is incompatible with the current transfer status. Compatible status --&gt; event type transitions include:  &#x60;pending&#x60; --&gt; &#x60;failed&#x60;  &#x60;pending&#x60; --&gt; &#x60;posted&#x60;  &#x60;posted&#x60; --&gt; &#x60;returned&#x60;  &#x60;posted&#x60; --&gt; &#x60;settled&#x60;  | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**test_clock_id** | **str, none_type** | Plaid’s unique identifier for a test clock. If provided, the event to be simulated is created at the &#x60;virtual_time&#x60; on the provided &#x60;test_clock&#x60;. | [optional] 
**failure_reason** | [**TransferFailure**](TransferFailure.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


