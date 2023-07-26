# DocumentRiskSignal

Details about a certain reason as to why a document could potentially be fraudulent.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str, none_type** | The result from the risk signal check. | 
**field** | **str, none_type** | The field which the risk signal was computed for | 
**has_fraud_risk** | **bool, none_type** | A flag used to quickly identify if the signal indicates that this field is authentic or fraudulent | 
**institution_metadata** | [**DocumentRiskSignalInstitutionMetadata**](DocumentRiskSignalInstitutionMetadata.md) |  | 
**expected_value** | **str, none_type** | The expected value of the field, as seen on the document | 
**actual_value** | **str, none_type** | The derived value obtained in the risk signal calculation process for this field | 
**signal_description** | **str, none_type** | A human-readable explanation providing more detail into the particular risk signal | 
**page_number** | **int, none_type** | The relevant page associated with the risk signal | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


