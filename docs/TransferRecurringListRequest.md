# TransferRecurringListRequest

Defines the request schema for `/transfer/recurring/list`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**start_time** | **datetime, none_type** | The start datetime of recurring transfers to list. This should be in RFC 3339 format (i.e. &#x60;2019-12-06T22:35:49Z&#x60;) | [optional] 
**end_time** | **datetime, none_type** | The end datetime of recurring transfers to list. This should be in RFC 3339 format (i.e. &#x60;2019-12-06T22:35:49Z&#x60;) | [optional] 
**count** | **int** | The maximum number of recurring transfers to return. | [optional]  if omitted the server will use the default value of 25
**offset** | **int** | The number of recurring transfers to skip before returning results. | [optional]  if omitted the server will use the default value of 0
**funding_account_id** | **str, none_type** | Filter recurring transfers to only those with the specified &#x60;funding_account_id&#x60;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


