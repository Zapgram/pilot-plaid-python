# Taxform

Data about an official document used to report the user's income to the IRS.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_type** | **str** | The type of tax document. Currently, the only supported value is &#x60;w2&#x60;. | 
**doc_id** | **str** | An identifier of the document referenced by the document metadata. | [optional] 
**w2** | [**W2**](W2.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


