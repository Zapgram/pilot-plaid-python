# AccountAccess

Allow or disallow product access by account. Unlisted (e.g. missing) accounts will be considered `new_accounts`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_id** | **str** | The unique account identifier for this account. This value must match that returned by the data access API for this account. | 
**authorized** | **bool, none_type** | Allow the application to see this account (and associated details, including balance) in the list of accounts  If unset, defaults to &#x60;true&#x60;. | [optional]  if omitted the server will use the default value of True
**account_product_access** | [**AccountProductAccessNullable**](AccountProductAccessNullable.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


