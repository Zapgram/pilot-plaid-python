# TransferRepayment

A repayment is created automatically after one or more guaranteed transactions receive a return. If there are multiple eligible returns in a day, they are batched together into a single repayment.  Repayments are sent over ACH, with funds typically available on the next banking day.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repayment_id** | **str** | Identifier of the repayment. | 
**created** | **datetime** | The datetime when the repayment occurred, in RFC 3339 format. | 
**amount** | **str** | Decimal amount of the repayment as it appears on your account ledger. | 
**iso_currency_code** | **str** | The currency of the repayment, e.g. \&quot;USD\&quot;. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


