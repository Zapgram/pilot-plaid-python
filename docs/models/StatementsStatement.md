# plaid.model.statements_statement.StatementsStatement

A statement's metadata associated with an account

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A statement&#x27;s metadata associated with an account | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**month** | decimal.Decimal, int,  | decimal.Decimal,  | Month of the year. Possible values: 1 through 12 (January through December). | 
**year** | decimal.Decimal, int,  | decimal.Decimal,  | Year. Possible values: 2010-{current_year}. | 
**statement_id** | str,  | str,  | Plaid&#x27;s unique identifier for the statement. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

