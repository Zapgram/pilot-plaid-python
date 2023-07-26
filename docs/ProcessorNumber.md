# ProcessorNumber

An object containing identifying numbers used for making electronic transfers to and from the `account`. The identifying number type (ACH, EFT, IBAN, or BACS) used will depend on the country of the account. An account may have more than one number type. If a particular identifying number type is not used by the `account` for which auth data has been requested, a null value will be returned.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ach** | [**NumbersACHNullable**](NumbersACHNullable.md) |  | [optional] 
**eft** | [**NumbersEFTNullable**](NumbersEFTNullable.md) |  | [optional] 
**international** | [**NumbersInternationalNullable**](NumbersInternationalNullable.md) |  | [optional] 
**bacs** | [**NumbersBACSNullable**](NumbersBACSNullable.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


