# plaid.model.auth_get_numbers.AuthGetNumbers

An object containing identifying numbers used for making electronic transfers to and from the `accounts`. The identifying number type (ACH, EFT, IBAN, or BACS) used will depend on the country of the account. An account may have more than one number type. If a particular identifying number type is not used by any `accounts` for which data has been requested, the array for that type will be empty.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object containing identifying numbers used for making electronic transfers to and from the &#x60;accounts&#x60;. The identifying number type (ACH, EFT, IBAN, or BACS) used will depend on the country of the account. An account may have more than one number type. If a particular identifying number type is not used by any &#x60;accounts&#x60; for which data has been requested, the array for that type will be empty. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[bacs](#bacs)** | list, tuple,  | tuple,  | An array of BACS numbers identifying accounts. | 
**[eft](#eft)** | list, tuple,  | tuple,  | An array of EFT numbers identifying accounts. | 
**[ach](#ach)** | list, tuple,  | tuple,  | An array of ACH numbers identifying accounts. | 
**[international](#international)** | list, tuple,  | tuple,  | An array of IBAN numbers identifying accounts. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ach

An array of ACH numbers identifying accounts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of ACH numbers identifying accounts. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NumbersACH**](NumbersACH.md) | [**NumbersACH**](NumbersACH.md) | [**NumbersACH**](NumbersACH.md) |  | 

# eft

An array of EFT numbers identifying accounts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of EFT numbers identifying accounts. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NumbersEFT**](NumbersEFT.md) | [**NumbersEFT**](NumbersEFT.md) | [**NumbersEFT**](NumbersEFT.md) |  | 

# international

An array of IBAN numbers identifying accounts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of IBAN numbers identifying accounts. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NumbersInternational**](NumbersInternational.md) | [**NumbersInternational**](NumbersInternational.md) | [**NumbersInternational**](NumbersInternational.md) |  | 

# bacs

An array of BACS numbers identifying accounts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of BACS numbers identifying accounts. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NumbersBACS**](NumbersBACS.md) | [**NumbersBACS**](NumbersBACS.md) | [**NumbersBACS**](NumbersBACS.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

