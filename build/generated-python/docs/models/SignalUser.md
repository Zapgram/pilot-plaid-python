# plaid.model.signal_user.SignalUser

Details about the end user initiating the transaction (i.e., the account holder).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Details about the end user initiating the transaction (i.e., the account holder). | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | [**SignalPersonName**](SignalPersonName.md) | [**SignalPersonName**](SignalPersonName.md) |  | [optional] 
**phone_number** | None, str,  | NoneClass, str,  | The user&#x27;s phone number, in E.164 format: +{countrycode}{number}. For example: \&quot;+14151234567\&quot; | [optional] 
**email_address** | None, str,  | NoneClass, str,  | The user&#x27;s email address. | [optional] 
**address** | [**SignalAddressData**](SignalAddressData.md) | [**SignalAddressData**](SignalAddressData.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

