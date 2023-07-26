# plaid.model.document_risk_signal.DocumentRiskSignal

Details about a certain reason as to why a document could potentially be fraudulent.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Details about a certain reason as to why a document could potentially be fraudulent. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**page_number** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The relevant page associated with the risk signal | 
**field** | None, str,  | NoneClass, str,  | The field which the risk signal was computed for | 
**has_fraud_risk** | None, bool,  | NoneClass, BoolClass,  | A flag used to quickly identify if the signal indicates that this field is authentic or fraudulent | 
**actual_value** | None, str,  | NoneClass, str,  | The derived value obtained in the risk signal calculation process for this field | 
**signal_description** | None, str,  | NoneClass, str,  | A human-readable explanation providing more detail into the particular risk signal | 
**expected_value** | None, str,  | NoneClass, str,  | The expected value of the field, as seen on the document | 
**type** | None, str,  | NoneClass, str,  | The result from the risk signal check. | 
**institution_metadata** | [**DocumentRiskSignalInstitutionMetadata**](DocumentRiskSignalInstitutionMetadata.md) | [**DocumentRiskSignalInstitutionMetadata**](DocumentRiskSignalInstitutionMetadata.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

