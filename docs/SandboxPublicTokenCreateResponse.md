# SandboxPublicTokenCreateResponse

SandboxPublicTokenCreateResponse defines the response schema for `/sandbox/public_token/create`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_token** | **str** | A public token that can be exchanged for an access token using &#x60;/item/public_token/exchange&#x60; | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


