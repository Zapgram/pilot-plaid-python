# plaid.model.bank_transfer_user.BankTransferUser

The legal name and other information for the account holder.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The legal name and other information for the account holder. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**legal_name** | str,  | str,  | The account holder’s full legal name. If the transfer &#x60;ach_class&#x60; is &#x60;ccd&#x60;, this should be the business name of the account holder. | 
**email_address** | None, str,  | NoneClass, str,  | The account holder’s email. | [optional] 
**routing_number** | str,  | str,  | The account holder&#x27;s routing number. This field is only used in response data. Do not provide this field when making requests. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

