# TransferRepaymentReturn

Represents a return on a Guaranteed ACH transfer that is included in the specified repayment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_id** | **str** | The unique identifier of the guaranteed transfer that was returned. | 
**event_id** | **int** | The unique identifier of the corresponding &#x60;returned&#x60; transfer event. | 
**amount** | **str** | The value of the returned transfer. | 
**iso_currency_code** | **str** | The currency of the repayment, e.g. \&quot;USD\&quot;. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


