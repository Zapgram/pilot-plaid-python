# plaid.model.numbers_eft.NumbersEFT

Identifying information for transferring money to or from a Canadian bank account via EFT.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Identifying information for transferring money to or from a Canadian bank account via EFT. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**institution** | str,  | str,  | The EFT institution number for the account | 
**account_id** | str,  | str,  | The Plaid account ID associated with the account numbers | 
**branch** | str,  | str,  | The EFT branch number for the account | 
**account** | str,  | str,  | The EFT account number for the account | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

