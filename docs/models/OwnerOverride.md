# plaid.model.owner_override.OwnerOverride

Data about the owner or owners of an account. Any fields not specified will be filled in with default Sandbox information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data about the owner or owners of an account. Any fields not specified will be filled in with default Sandbox information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[emails](#emails)** | list, tuple,  | tuple,  | A list of email addresses associated with the account. | 
**[phone_numbers](#phone_numbers)** | list, tuple,  | tuple,  | A list of phone numbers associated with the account. | 
**[addresses](#addresses)** | list, tuple,  | tuple,  | Data about the various addresses associated with the account. | 
**[names](#names)** | list, tuple,  | tuple,  | A list of names associated with the account by the financial institution. These should always be the names of individuals, even for business accounts. Note that the same name data will be used for all accounts associated with an Item. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# names

A list of names associated with the account by the financial institution. These should always be the names of individuals, even for business accounts. Note that the same name data will be used for all accounts associated with an Item.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of names associated with the account by the financial institution. These should always be the names of individuals, even for business accounts. Note that the same name data will be used for all accounts associated with an Item. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# phone_numbers

A list of phone numbers associated with the account.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of phone numbers associated with the account. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PhoneNumber**](PhoneNumber.md) | [**PhoneNumber**](PhoneNumber.md) | [**PhoneNumber**](PhoneNumber.md) |  | 

# emails

A list of email addresses associated with the account.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of email addresses associated with the account. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Email**](Email.md) | [**Email**](Email.md) | [**Email**](Email.md) |  | 

# addresses

Data about the various addresses associated with the account.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Data about the various addresses associated with the account. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Address**](Address.md) | [**Address**](Address.md) | [**Address**](Address.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

