# IncomeVerificationCreateRequest

IncomeVerificationCreateRequest defines the request schema for `/income/verification/create`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook** | **str** | The URL endpoint to which Plaid should send webhooks related to the progress of the income verification process. | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**precheck_id** | **str** | The ID of a precheck created with &#x60;/income/verification/precheck&#x60;. Will be used to improve conversion of the income verification flow. | [optional] 
**options** | [**IncomeVerificationCreateRequestOptions**](IncomeVerificationCreateRequestOptions.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


