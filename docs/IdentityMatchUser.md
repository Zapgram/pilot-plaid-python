# IdentityMatchUser

The user's legal name, phone number, email address and address used to perform fuzzy match. If Financial Account Matching is enabled in the Identity Verification product, leave this field empty to automatically match against PII collected from the Identity Verification checks.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_name** | **str, none_type** | The user&#39;s full legal name. | [optional] 
**phone_number** | **str, none_type** | The user&#39;s phone number, in E.164 format: +{countrycode}{number}. For example: \&quot;+14151234567\&quot;. Phone numbers provided in other formats will be parsed on a best-effort basis. | [optional] 
**email_address** | **str, none_type** | The user&#39;s email address. | [optional] 
**address** | [**AddressDataNullable**](AddressDataNullable.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


