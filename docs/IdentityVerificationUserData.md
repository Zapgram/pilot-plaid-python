# IdentityVerificationUserData

The identity data that was either collected from the user or provided via API in order to perform an identity verification.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_of_birth** | **date, none_type** | A date in the format YYYY-MM-DD (RFC 3339 Section 5.6). | 
**ip_address** | **str, none_type** | An IPv4 or IPV6 address. | 
**email_address** | **str, none_type** | A valid email address. | 
**name** | [**IdentityVerificationResponseUserName**](IdentityVerificationResponseUserName.md) |  | 
**address** | [**IdentityVerificationUserAddress**](IdentityVerificationUserAddress.md) |  | 
**id_number** | [**UserIDNumber**](UserIDNumber.md) |  | 
**phone_number** | **str, none_type** | A phone number in E.164 format. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


