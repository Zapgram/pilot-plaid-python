# ItemApplicationListUserAuth

User authentication parameters, for clients making a request without an `access_token`. This is only allowed for select clients and will not be supported in the future. Most clients should call /item/import to obtain an access token before making a request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str, none_type** | Account username. | [optional] 
**fi_username_hash** | **str, none_type** | Account username hashed by FI. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


