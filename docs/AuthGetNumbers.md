# AuthGetNumbers

An object containing identifying numbers used for making electronic transfers to and from the `accounts`. The identifying number type (ACH, EFT, IBAN, or BACS) used will depend on the country of the account. An account may have more than one number type. If a particular identifying number type is not used by any `accounts` for which data has been requested, the array for that type will be empty.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ach** | [**[NumbersACH]**](NumbersACH.md) | An array of ACH numbers identifying accounts. | 
**eft** | [**[NumbersEFT]**](NumbersEFT.md) | An array of EFT numbers identifying accounts. | 
**international** | [**[NumbersInternational]**](NumbersInternational.md) | An array of IBAN numbers identifying accounts. | 
**bacs** | [**[NumbersBACS]**](NumbersBACS.md) | An array of BACS numbers identifying accounts. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


