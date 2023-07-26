# plaid.model.sandbox_transfer_simulate_request.SandboxTransferSimulateRequest

Defines the request schema for `/sandbox/transfer/simulate`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines the request schema for &#x60;/sandbox/transfer/simulate&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**event_type** | str,  | str,  | The asynchronous event to be simulated. May be: &#x60;posted&#x60;, &#x60;settled&#x60;, &#x60;failed&#x60;, or &#x60;returned&#x60;.  An error will be returned if the event type is incompatible with the current transfer status. Compatible status --&gt; event type transitions include:  &#x60;pending&#x60; --&gt; &#x60;failed&#x60;  &#x60;pending&#x60; --&gt; &#x60;posted&#x60;  &#x60;posted&#x60; --&gt; &#x60;returned&#x60;  &#x60;posted&#x60; --&gt; &#x60;settled&#x60;  | 
**transfer_id** | str,  | str,  | Plaid’s unique identifier for a transfer. | 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**test_clock_id** | None, str,  | NoneClass, str,  | Plaid’s unique identifier for a test clock. If provided, the event to be simulated is created at the &#x60;virtual_time&#x60; on the provided &#x60;test_clock&#x60;. | [optional] 
**failure_reason** | [**TransferFailure**](TransferFailure.md) | [**TransferFailure**](TransferFailure.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

