# plaid.model.auth_get_response.AuthGetResponse

AuthGetResponse defines the response schema for `/auth/get`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | AuthGetResponse defines the response schema for &#x60;/auth/get&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**item** | [**Item**](Item.md) | [**Item**](Item.md) |  | 
**numbers** | [**AuthGetNumbers**](AuthGetNumbers.md) | [**AuthGetNumbers**](AuthGetNumbers.md) |  | 
**[accounts](#accounts)** | list, tuple,  | tuple,  | The &#x60;accounts&#x60; for which numbers are being retrieved. | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# accounts

The `accounts` for which numbers are being retrieved.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The &#x60;accounts&#x60; for which numbers are being retrieved. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AccountBase**](AccountBase.md) | [**AccountBase**](AccountBase.md) | [**AccountBase**](AccountBase.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
