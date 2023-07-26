# LinkTokenCreateResponse

LinkTokenCreateResponse defines the response schema for `/link/token/create`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_token** | **str** | A &#x60;link_token&#x60;, which can be supplied to Link in order to initialize it and receive a &#x60;public_token&#x60;, which can be exchanged for an &#x60;access_token&#x60;. | 
**expiration** | **datetime** | The expiration date for the &#x60;link_token&#x60;, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. A &#x60;link_token&#x60; created to generate a &#x60;public_token&#x60; that will be exchanged for a new &#x60;access_token&#x60; expires after 4 hours. A &#x60;link_token&#x60; created for an existing Item (such as when updating an existing &#x60;access_token&#x60; by launching Link in update mode) expires after 30 minutes. | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


