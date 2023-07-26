# LinkOAuthCorrelationIdExchangeResponse

LinkOAuthCorrelationIdExchangeResponse defines the response schema for `/link/oauth/correlation_id/exchange`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_token** | **str** | The &#x60;link_token&#x60; associated to the given &#x60;link_correlation_id&#x60;, which can be used to re-initialize Link. | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


