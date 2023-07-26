# LinkDeliveryCreateResponse

LinkDeliveryCreateResponse defines the response schema for `/link_delivery/create`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_delivery_url** | **str** | The URL to the Hosted Link session, which will be delivered by the specified delivery method. | 
**link_delivery_session_id** | **str** | The ID for the Hosted Link session. Same as the &#x60;link_token&#x60; string excluding the \&quot;link-{env}-\&quot; prefix. | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


