# plaid.model.numbers_acats.NumbersACATS

Identifying information for transferring holdings to an investments account via ACATS.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Identifying information for transferring holdings to an investments account via ACATS. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account_id** | str,  | str,  | The Plaid account ID associated with the account numbers | 
**[dtc_numbers](#dtc_numbers)** | list, tuple,  | tuple,  | Identifiers for the clearinghouses that are assocciated with the account in order of relevance. This array will be empty if we can&#x27;t provide any account level data. Institution level data can be retrieved from the institutions/get endpoints. | 
**account** | str,  | str,  | The full account number for the account | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# dtc_numbers

Identifiers for the clearinghouses that are assocciated with the account in order of relevance. This array will be empty if we can't provide any account level data. Institution level data can be retrieved from the institutions/get endpoints.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Identifiers for the clearinghouses that are assocciated with the account in order of relevance. This array will be empty if we can&#x27;t provide any account level data. Institution level data can be retrieved from the institutions/get endpoints. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

