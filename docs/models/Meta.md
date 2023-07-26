# plaid.model.meta.Meta

Allows specifying the metadata of the test account

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Allows specifying the metadata of the test account | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**official_name** | str,  | str,  | The account&#x27;s official name | 
**limit** | decimal.Decimal, int, float,  | decimal.Decimal,  | The account&#x27;s limit | value must be a 64 bit float
**name** | str,  | str,  | The account&#x27;s name | 
**mask** | str,  | str,  | The account&#x27;s mask. Should be an empty string or a string of 2-4 alphanumeric characters. This allows you to model a mask which does not match the account number (such as with a virtual account number). | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

