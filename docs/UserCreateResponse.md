# UserCreateResponse

UserCreateResponse defines the response schema for `/user/create`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_token** | **str** | The user token associated with the User data is being requested for. | 
**user_id** | **str** | The Plaid &#x60;user_id&#x60; of the User associated with this webhook, warning, or error. | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


