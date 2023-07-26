# DepositSwitchAltCreateRequest

DepositSwitchAltCreateRequest defines the request schema for `/deposit_switch/alt/create`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_account** | [**DepositSwitchTargetAccount**](DepositSwitchTargetAccount.md) |  | 
**target_user** | [**DepositSwitchTargetUser**](DepositSwitchTargetUser.md) |  | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**options** | [**DepositSwitchCreateRequestOptions**](DepositSwitchCreateRequestOptions.md) |  | [optional] 
**country_code** | **str, none_type** | ISO-3166-1 alpha-2 country code standard. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


