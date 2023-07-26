# plaid.model.single_document_risk_signal.SingleDocumentRiskSignal

Object containing all risk signals and relevant metadata for a single document

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing all risk signals and relevant metadata for a single document | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**document_reference** | [**RiskSignalDocumentReference**](RiskSignalDocumentReference.md) | [**RiskSignalDocumentReference**](RiskSignalDocumentReference.md) |  | 
**risk_summary** | [**DocumentRiskSummary**](DocumentRiskSummary.md) | [**DocumentRiskSummary**](DocumentRiskSummary.md) |  | 
**[risk_signals](#risk_signals)** | list, tuple,  | tuple,  | Array of attributes that indicate whether or not there is fraud risk with a document | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# risk_signals

Array of attributes that indicate whether or not there is fraud risk with a document

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of attributes that indicate whether or not there is fraud risk with a document | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DocumentRiskSignal**](DocumentRiskSignal.md) | [**DocumentRiskSignal**](DocumentRiskSignal.md) | [**DocumentRiskSignal**](DocumentRiskSignal.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

