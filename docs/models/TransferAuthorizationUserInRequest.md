# plaid.model.transfer_authorization_user_in_request.TransferAuthorizationUserInRequest

The legal name and other information for the account holder.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The legal name and other information for the account holder. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**legal_name** | str,  | str,  | The user&#x27;s legal name. | 
**phone_number** | str,  | str,  | The user&#x27;s phone number. In order to qualify for a guaranteed transfer, at least one of &#x60;phone_number&#x60; or &#x60;email_address&#x60; must be provided. | [optional] 
**email_address** | str,  | str,  | The user&#x27;s email address. In order to qualify for a guaranteed transfer, at least one of &#x60;phone_number&#x60; or &#x60;email_address&#x60; must be provided. | [optional] 
**address** | [**TransferUserAddressInRequest**](TransferUserAddressInRequest.md) | [**TransferUserAddressInRequest**](TransferUserAddressInRequest.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
