# plaid.model.credit1099_payer.Credit1099Payer

An object representing a payer used by 1099-MISC tax documents.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing a payer used by 1099-MISC tax documents. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**address** | [**CreditPayStubAddress**](CreditPayStubAddress.md) | [**CreditPayStubAddress**](CreditPayStubAddress.md) |  | [optional] 
**name** | None, str,  | NoneClass, str,  | Name of payer. | [optional] 
**tin** | None, str,  | NoneClass, str,  | Tax identification number of payer. | [optional] 
**telephone_number** | None, str,  | NoneClass, str,  | Telephone number of payer. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

