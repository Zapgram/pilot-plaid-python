# plaid.model.credit1099_recipient.Credit1099Recipient

An object representing a recipient used in both 1099-K and 1099-MISC tax documents.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing a recipient used in both 1099-K and 1099-MISC tax documents. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**address** | [**CreditPayStubAddress**](CreditPayStubAddress.md) | [**CreditPayStubAddress**](CreditPayStubAddress.md) |  | [optional] 
**name** | None, str,  | NoneClass, str,  | Name of recipient. | [optional] 
**tin** | None, str,  | NoneClass, str,  | Tax identification number of recipient. | [optional] 
**account_number** | None, str,  | NoneClass, str,  | Account number number of recipient. | [optional] 
**facta_filing_requirement** | None, str,  | NoneClass, str,  | Checked if FACTA is a filing requirement. | [optional] 
**second_tin_exists** | None, str,  | NoneClass, str,  | Checked if 2nd TIN exists. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

