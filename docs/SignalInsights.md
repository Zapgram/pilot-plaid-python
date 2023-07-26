# SignalInsights

Signal insights including scores and attributes. This response is offered as an add-on to `/transfer/authorization/create`. To request access to these fields please contact your Plaid account manager.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scores** | [**SignalScores**](SignalScores.md) |  | [optional] 
**warnings** | [**[SignalWarning]**](SignalWarning.md) | If bank information was not available to be used in the Signal model, this array contains warnings describing why bank data is missing. If you want to receive an API error instead of Signal scores in the case of missing bank data, file a support ticket or contact your Plaid account manager. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


