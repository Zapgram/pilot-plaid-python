# TransferRepaymentListRequest

Defines the request schema for `/transfer/repayment/list`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**start_date** | **datetime, none_type** | The start datetime of repayments to return (RFC 3339 format). | [optional] 
**end_date** | **datetime, none_type** | The end datetime of repayments to return (RFC 3339 format). | [optional] 
**count** | **int, none_type** | The maximum number of repayments to return. | [optional]  if omitted the server will use the default value of 25
**offset** | **int** | The number of repayments to skip before returning results. | [optional]  if omitted the server will use the default value of 0
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


