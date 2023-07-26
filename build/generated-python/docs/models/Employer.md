# plaid.model.employer.Employer

Data about the employer.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data about the employer. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**address** | [**AddressDataNullable**](AddressDataNullable.md) | [**AddressDataNullable**](AddressDataNullable.md) |  | 
**confidence_score** | decimal.Decimal, int, float,  | decimal.Decimal,  | A number from 0 to 1 indicating Plaid&#x27;s level of confidence in the pairing between the employer and the institution (not yet implemented). | value must be a 64 bit float
**name** | str,  | str,  | The name of the employer | 
**employer_id** | str,  | str,  | Plaid&#x27;s unique identifier for the employer. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

