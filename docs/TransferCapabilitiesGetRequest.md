# TransferCapabilitiesGetRequest

Defines the request schema for `/transfer/capabilities/get`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**access_token** | **str** | The Plaid &#x60;access_token&#x60; for the account that will be debited or credited. Required if not using &#x60;payment_profile_token&#x60;. | [optional] 
**account_id** | **str** | The Plaid &#x60;account_id&#x60; corresponding to the end-user account that will be debited or credited. Required when creating a transfer using an &#x60;access_token&#x60;. | [optional] 
**payment_profile_token** | **str** | A payment profile token associated with the Payment Profile data that is being requested. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


