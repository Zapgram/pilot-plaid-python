# plaid.model.selfie_check_selfie.SelfieCheckSelfie

Catpures and analysis from a user's selfie.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Catpures and analysis from a user&#x27;s selfie. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**capture** | [**SelfieCapture**](SelfieCapture.md) | [**SelfieCapture**](SelfieCapture.md) |  | 
**analysis** | [**SelfieAnalysis**](SelfieAnalysis.md) | [**SelfieAnalysis**](SelfieAnalysis.md) |  | 
**attempt** | decimal.Decimal, int,  | decimal.Decimal,  | The &#x60;attempt&#x60; field begins with 1 and increments with each subsequent selfie upload. | 
**status** | [**SelfieStatus**](SelfieStatus.md) | [**SelfieStatus**](SelfieStatus.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

