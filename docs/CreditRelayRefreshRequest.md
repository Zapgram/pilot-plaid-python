# CreditRelayRefreshRequest

CreditRelayRefreshRequest defines the request schema for `/credit/relay/refresh`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relay_token** | **str** | The &#x60;relay_token&#x60; granting access to the report you would like to refresh. | 
**report_type** | [**ReportType**](ReportType.md) |  | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**webhook** | **str, none_type** | The URL registered to receive webhooks when the report of a relay token has been refreshed. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


