# plaid.model.deposit_switch_target_user.DepositSwitchTargetUser

The deposit switch target user

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The deposit switch target user | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**phone** | str,  | str,  | The phone number of the user. The endpoint can accept a variety of phone number formats, including E.164. | 
**given_name** | str,  | str,  | The given name (first name) of the user. | 
**family_name** | str,  | str,  | The family name (last name) of the user. | 
**email** | str,  | str,  | The email address of the user. | 
**address** | [**DepositSwitchAddressData**](DepositSwitchAddressData.md) | [**DepositSwitchAddressData**](DepositSwitchAddressData.md) |  | [optional] 
**tax_payer_id** | str,  | str,  | The taxpayer ID of the user, generally their SSN, EIN, or TIN. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

