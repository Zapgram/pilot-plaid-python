# plaid.model.credit1099_filer.Credit1099Filer

An object representing a filer used by 1099-K tax documents.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing a filer used by 1099-K tax documents. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**address** | [**CreditPayStubAddress**](CreditPayStubAddress.md) | [**CreditPayStubAddress**](CreditPayStubAddress.md) |  | [optional] 
**name** | None, str,  | NoneClass, str,  | Name of filer. | [optional] 
**tin** | None, str,  | NoneClass, str,  | Tax identification number of filer. | [optional] 
**type** | None, str,  | NoneClass, str,  | One of the following values will be provided: Payment Settlement Entity (PSE), Electronic Payment Facilitator (EPF), Other Third Party | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

