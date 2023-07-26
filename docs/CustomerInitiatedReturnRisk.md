# CustomerInitiatedReturnRisk

The object contains a risk score and a risk tier that evaluate the transaction return risk of an unauthorized debit. Common return codes in this category include: \"R05\", \"R07\", \"R10\", \"R11\", \"R29\". These returns typically have a return time frame of up to 60 calendar days. During this period, the customer of financial institutions can dispute a transaction as unauthorized.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | [**SignalScore**](SignalScore.md) |  | 
**risk_tier** | [**CustomerInitiatedRiskTier**](CustomerInitiatedRiskTier.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


