# plaid.model.auth_get_request_options.AuthGetRequestOptions

An optional object to filter `/auth/get` results.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An optional object to filter &#x60;/auth/get&#x60; results. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[account_ids](#account_ids)** | list, tuple,  | tuple,  | A list of &#x60;account_ids&#x60; to retrieve for the Item. Note: An error will be returned if a provided &#x60;account_id&#x60; is not associated with the Item. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# account_ids

A list of `account_ids` to retrieve for the Item. Note: An error will be returned if a provided `account_id` is not associated with the Item.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of &#x60;account_ids&#x60; to retrieve for the Item. Note: An error will be returned if a provided &#x60;account_id&#x60; is not associated with the Item. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

