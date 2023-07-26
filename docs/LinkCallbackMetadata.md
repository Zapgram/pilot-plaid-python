# LinkCallbackMetadata

Information related to the callback from the hosted Link session.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_type** | [**LinkDeliveryWebhookCallbackType**](LinkDeliveryWebhookCallbackType.md) |  | [optional] 
**event_name** | [**LinkEventName**](LinkEventName.md) |  | [optional] 
**status** | **str** | Indicates where in the flow the Link user exited | [optional] 
**link_session_id** | **str** | A unique identifier associated with a user&#39;s actions and events through the Link flow. Include this identifier when opening a support ticket for faster turnaround. | [optional] 
**request_id** | **str** | The request ID for the last request made by Link. This can be shared with Plaid Support to expedite investigation. | [optional] 
**institution** | [**LinkDeliveryInstitution**](LinkDeliveryInstitution.md) |  | [optional] 
**accounts** | [**[LinkDeliveryAccount]**](LinkDeliveryAccount.md) | A list of accounts attached to the connected Item. If Account Select is enabled via the developer dashboard, accounts will only include selected accounts. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


