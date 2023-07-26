# plaid.model.numbers.Numbers

Account and bank identifier number data used to configure the test account. All values are optional.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Account and bank identifier number data used to configure the test account. All values are optional. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account** | str,  | str,  | Will be used for the account number. | [optional] 
**ach_routing** | str,  | str,  | Must be a valid ACH routing number. | [optional] 
**ach_wire_routing** | str,  | str,  | Must be a valid wire transfer routing number. | [optional] 
**eft_institution** | str,  | str,  | EFT institution number. Must be specified alongside &#x60;eft_branch&#x60;. | [optional] 
**eft_branch** | str,  | str,  | EFT branch number. Must be specified alongside &#x60;eft_institution&#x60;. | [optional] 
**international_bic** | str,  | str,  | Bank identifier code (BIC). Must be specified alongside &#x60;international_iban&#x60;. | [optional] 
**international_iban** | str,  | str,  | International bank account number (IBAN). If no account number is specified via &#x60;account&#x60;, will also be used as the account number by default. Must be specified alongside &#x60;international_bic&#x60;. | [optional] 
**bacs_sort_code** | str,  | str,  | BACS sort code | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

