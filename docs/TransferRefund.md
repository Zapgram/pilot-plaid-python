# TransferRefund

Represents a refund within the Transfers API.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Plaid’s unique identifier for a refund. | 
**transfer_id** | **str** | The ID of the transfer to refund. | 
**amount** | **str** | The amount of the refund (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**status** | [**TransferRefundStatus**](TransferRefundStatus.md) |  | 
**created** | **datetime** | The datetime when this refund was created. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60; | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


