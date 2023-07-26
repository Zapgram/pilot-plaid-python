# LinkTokenGetResponse

LinkTokenGetResponse defines the response schema for `/link/token/get`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_token** | **str** | A &#x60;link_token&#x60;, which can be supplied to Link in order to initialize it and receive a &#x60;public_token&#x60;, which can be exchanged for an &#x60;access_token&#x60;. | 
**created_at** | **datetime, none_type** | The creation timestamp for the &#x60;link_token&#x60;, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. | 
**expiration** | **datetime, none_type** | The expiration timestamp for the &#x60;link_token&#x60;, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. | 
**metadata** | [**LinkTokenGetMetadataResponse**](LinkTokenGetMetadataResponse.md) |  | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


