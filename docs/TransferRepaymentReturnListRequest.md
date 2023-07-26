# TransferRepaymentReturnListRequest

Defines the request schema for `/transfer/repayment/return/list`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repayment_id** | **str** | Identifier of the repayment to query. | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**count** | **int, none_type** | The maximum number of repayments to return. | [optional]  if omitted the server will use the default value of 25
**offset** | **int** | The number of repayments to skip before returning results. | [optional]  if omitted the server will use the default value of 0
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


