# plaid.model.link_callback_metadata.LinkCallbackMetadata

Information related to the callback from the hosted Link session.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Information related to the callback from the hosted Link session. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**callback_type** | [**LinkDeliveryWebhookCallbackType**](LinkDeliveryWebhookCallbackType.md) | [**LinkDeliveryWebhookCallbackType**](LinkDeliveryWebhookCallbackType.md) |  | [optional] 
**event_name** | [**LinkEventName**](LinkEventName.md) | [**LinkEventName**](LinkEventName.md) |  | [optional] 
**status** | str,  | str,  | Indicates where in the flow the Link user exited | [optional] 
**link_session_id** | str,  | str,  | A unique identifier associated with a user&#x27;s actions and events through the Link flow. Include this identifier when opening a support ticket for faster turnaround. | [optional] 
**request_id** | str,  | str,  | The request ID for the last request made by Link. This can be shared with Plaid Support to expedite investigation. | [optional] 
**institution** | [**LinkDeliveryInstitution**](LinkDeliveryInstitution.md) | [**LinkDeliveryInstitution**](LinkDeliveryInstitution.md) |  | [optional] 
**[accounts](#accounts)** | list, tuple,  | tuple,  | A list of accounts attached to the connected Item. If Account Select is enabled via the developer dashboard, accounts will only include selected accounts. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# accounts

A list of accounts attached to the connected Item. If Account Select is enabled via the developer dashboard, accounts will only include selected accounts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of accounts attached to the connected Item. If Account Select is enabled via the developer dashboard, accounts will only include selected accounts. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**LinkDeliveryAccount**](LinkDeliveryAccount.md) | [**LinkDeliveryAccount**](LinkDeliveryAccount.md) | [**LinkDeliveryAccount**](LinkDeliveryAccount.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

