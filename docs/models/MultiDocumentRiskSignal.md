# plaid.model.multi_document_risk_signal.MultiDocumentRiskSignal

Object containing risk signals and relevant metadata for a set of uploaded documents

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing risk signals and relevant metadata for a set of uploaded documents | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[document_references](#document_references)** | list, tuple,  | tuple,  | Array of objects containing attributes that could indicate if a document is fraudulent | 
**[risk_signals](#risk_signals)** | list, tuple,  | tuple,  | Array of attributes that indicate whether or not there is fraud risk with a set of documents | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# document_references

Array of objects containing attributes that could indicate if a document is fraudulent

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of objects containing attributes that could indicate if a document is fraudulent | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RiskSignalDocumentReference**](RiskSignalDocumentReference.md) | [**RiskSignalDocumentReference**](RiskSignalDocumentReference.md) | [**RiskSignalDocumentReference**](RiskSignalDocumentReference.md) |  | 

# risk_signals

Array of attributes that indicate whether or not there is fraud risk with a set of documents

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of attributes that indicate whether or not there is fraud risk with a set of documents | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DocumentRiskSignal**](DocumentRiskSignal.md) | [**DocumentRiskSignal**](DocumentRiskSignal.md) | [**DocumentRiskSignal**](DocumentRiskSignal.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

