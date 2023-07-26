# WalletCreateResponse

WalletCreateResponse defines the response schema for `/wallet/create`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | A unique ID identifying the e-wallet | 
**balance** | [**WalletBalance**](WalletBalance.md) |  | 
**numbers** | [**WalletNumbers**](WalletNumbers.md) |  | 
**status** | [**WalletStatus**](WalletStatus.md) |  | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**recipient_id** | **str** | The ID of the recipient that corresponds to the e-wallet account numbers | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


