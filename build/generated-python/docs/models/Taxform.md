# plaid.model.taxform.Taxform

Data about an official document used to report the user's income to the IRS.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data about an official document used to report the user&#x27;s income to the IRS. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**document_type** | str,  | str,  | The type of tax document. Currently, the only supported value is &#x60;w2&#x60;. | 
**doc_id** | str,  | str,  | An identifier of the document referenced by the document metadata. | [optional] 
**w2** | [**W2**](W2.md) | [**W2**](W2.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

