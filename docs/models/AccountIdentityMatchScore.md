# plaid.model.account_identity_match_score.AccountIdentityMatchScore

Identity match scores for an account

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Identity match scores for an account | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[AccountBase](AccountBase.md) | [**AccountBase**](AccountBase.md) | [**AccountBase**](AccountBase.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**legal_name** | [**NameMatchScore**](NameMatchScore.md) | [**NameMatchScore**](NameMatchScore.md) |  | [optional] 
**phone_number** | [**PhoneNumberMatchScore**](PhoneNumberMatchScore.md) | [**PhoneNumberMatchScore**](PhoneNumberMatchScore.md) |  | [optional] 
**email_address** | [**EmailAddressMatchScore**](EmailAddressMatchScore.md) | [**EmailAddressMatchScore**](EmailAddressMatchScore.md) |  | [optional] 
**address** | [**AddressMatchScore**](AddressMatchScore.md) | [**AddressMatchScore**](AddressMatchScore.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

