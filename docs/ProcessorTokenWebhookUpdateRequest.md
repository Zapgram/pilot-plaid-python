# ProcessorTokenWebhookUpdateRequest

ProcessorTokenWebhookUpdateRequest defines the request schema for `/processor/token/webhook/update`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processor_token** | **str** | The processor token obtained from the Plaid integration partner. Processor tokens are in the format: &#x60;processor-&lt;environment&gt;-&lt;identifier&gt;&#x60; | 
**webhook** | **str, none_type** | The new webhook URL to associate with the processor token. To remove a webhook from a processor token, set to &#x60;null&#x60;. | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


