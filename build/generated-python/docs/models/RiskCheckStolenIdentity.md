# plaid.model.risk_check_stolen_identity.RiskCheckStolenIdentity

Field containing the data used in determining the outcome of the stolen identity risk check.  Contains the following fields:  `score` - A score from 0 to 100 indicating the likelihood that the user is a stolen identity.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Field containing the data used in determining the outcome of the stolen identity risk check.  Contains the following fields:  &#x60;score&#x60; - A score from 0 to 100 indicating the likelihood that the user is a stolen identity. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**score** | decimal.Decimal, int,  | decimal.Decimal,  | A score from 0 to 100 indicating the likelihood that the user is a stolen identity. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
