# plaid.model.processor_signal_evaluate_response.ProcessorSignalEvaluateResponse

ProcessorSignalEvaluateResponse defines the response schema for `/processor/signal/evaluate`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ProcessorSignalEvaluateResponse defines the response schema for &#x60;/processor/signal/evaluate&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**scores** | [**SignalScores**](SignalScores.md) | [**SignalScores**](SignalScores.md) |  | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**core_attributes** | [**SignalEvaluateCoreAttributes**](SignalEvaluateCoreAttributes.md) | [**SignalEvaluateCoreAttributes**](SignalEvaluateCoreAttributes.md) |  | [optional] 
**[warnings](#warnings)** | list, tuple,  | tuple,  | If bank information was not available to be used in the Signal model, this array contains warnings describing why bank data is missing. If you want to receive an API error instead of Signal scores in the case of missing bank data, file a support ticket or contact your Plaid account manager. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# warnings

If bank information was not available to be used in the Signal model, this array contains warnings describing why bank data is missing. If you want to receive an API error instead of Signal scores in the case of missing bank data, file a support ticket or contact your Plaid account manager.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | If bank information was not available to be used in the Signal model, this array contains warnings describing why bank data is missing. If you want to receive an API error instead of Signal scores in the case of missing bank data, file a support ticket or contact your Plaid account manager. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SignalWarning**](SignalWarning.md) | [**SignalWarning**](SignalWarning.md) | [**SignalWarning**](SignalWarning.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
