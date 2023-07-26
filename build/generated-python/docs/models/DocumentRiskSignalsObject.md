# plaid.model.document_risk_signals_object.DocumentRiskSignalsObject

Object containing fraud risk data for a set of income documents.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing fraud risk data for a set of income documents. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account_id** | None, str,  | NoneClass, str,  | ID of the payroll provider account. | 
**[single_document_risk_signals](#single_document_risk_signals)** | list, tuple,  | tuple,  | Array of document metadata and associated risk signals per document | 
**[multi_document_risk_signals](#multi_document_risk_signals)** | list, tuple,  | tuple,  | Array of risk signals computed from a set of uploaded documents and the associated documents&#x27; metadata | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# single_document_risk_signals

Array of document metadata and associated risk signals per document

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of document metadata and associated risk signals per document | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SingleDocumentRiskSignal**](SingleDocumentRiskSignal.md) | [**SingleDocumentRiskSignal**](SingleDocumentRiskSignal.md) | [**SingleDocumentRiskSignal**](SingleDocumentRiskSignal.md) |  | 

# multi_document_risk_signals

Array of risk signals computed from a set of uploaded documents and the associated documents' metadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of risk signals computed from a set of uploaded documents and the associated documents&#x27; metadata | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MultiDocumentRiskSignal**](MultiDocumentRiskSignal.md) | [**MultiDocumentRiskSignal**](MultiDocumentRiskSignal.md) | [**MultiDocumentRiskSignal**](MultiDocumentRiskSignal.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

