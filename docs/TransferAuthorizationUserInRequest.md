# TransferAuthorizationUserInRequest

The legal name and other information for the account holder.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_name** | **str** | The user&#39;s legal name. | 
**phone_number** | **str** | The user&#39;s phone number. In order to qualify for a guaranteed transfer, at least one of &#x60;phone_number&#x60; or &#x60;email_address&#x60; must be provided. | [optional] 
**email_address** | **str** | The user&#39;s email address. In order to qualify for a guaranteed transfer, at least one of &#x60;phone_number&#x60; or &#x60;email_address&#x60; must be provided. | [optional] 
**address** | [**TransferUserAddressInRequest**](TransferUserAddressInRequest.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


