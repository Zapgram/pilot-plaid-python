# DocumentRiskSignalsObject

Object containing fraud risk data for a set of income documents.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str, none_type** | ID of the payroll provider account. | 
**single_document_risk_signals** | [**[SingleDocumentRiskSignal]**](SingleDocumentRiskSignal.md) | Array of document metadata and associated risk signals per document | 
**multi_document_risk_signals** | [**[MultiDocumentRiskSignal]**](MultiDocumentRiskSignal.md) | Array of risk signals computed from a set of uploaded documents and the associated documents&#39; metadata | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


