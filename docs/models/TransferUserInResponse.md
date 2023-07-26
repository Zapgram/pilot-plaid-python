# plaid.model.transfer_user_in_response.TransferUserInResponse

The legal name and other information for the account holder.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The legal name and other information for the account holder. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**address** | [**TransferUserAddressInResponse**](TransferUserAddressInResponse.md) | [**TransferUserAddressInResponse**](TransferUserAddressInResponse.md) |  | 
**email_address** | None, str,  | NoneClass, str,  | The user&#x27;s email address. | 
**phone_number** | None, str,  | NoneClass, str,  | The user&#x27;s phone number. | 
**legal_name** | str,  | str,  | The user&#x27;s legal name. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

