# plaid.model.processor_number.ProcessorNumber

An object containing identifying numbers used for making electronic transfers to and from the `account`. The identifying number type (ACH, EFT, IBAN, or BACS) used will depend on the country of the account. An account may have more than one number type. If a particular identifying number type is not used by the `account` for which auth data has been requested, a null value will be returned.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object containing identifying numbers used for making electronic transfers to and from the &#x60;account&#x60;. The identifying number type (ACH, EFT, IBAN, or BACS) used will depend on the country of the account. An account may have more than one number type. If a particular identifying number type is not used by the &#x60;account&#x60; for which auth data has been requested, a null value will be returned. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ach** | [**NumbersACHNullable**](NumbersACHNullable.md) | [**NumbersACHNullable**](NumbersACHNullable.md) |  | [optional] 
**eft** | [**NumbersEFTNullable**](NumbersEFTNullable.md) | [**NumbersEFTNullable**](NumbersEFTNullable.md) |  | [optional] 
**international** | [**NumbersInternationalNullable**](NumbersInternationalNullable.md) | [**NumbersInternationalNullable**](NumbersInternationalNullable.md) |  | [optional] 
**bacs** | [**NumbersBACSNullable**](NumbersBACSNullable.md) | [**NumbersBACSNullable**](NumbersBACSNullable.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

