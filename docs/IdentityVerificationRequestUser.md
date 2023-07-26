# IdentityVerificationRequestUser

User information collected outside of Link, most likely via your own onboarding process.  Each of the following identity fields are optional:  `email_address`  `phone_number`  `date_of_birth`  `name`  `address`  `id_number`  Specifically, these fields are optional in that they can either be fully provided (satisfying every required field in their subschema) or omitted from the request entirely by not providing the key or value. Providing these fields via the API will result in Link skipping the data collection process for the associated user. All verification steps enabled in the associated Identity Verification Template will still be run. Verification steps will either be run immediately, or once the user completes the `accept_tos` step, depending on the value provided to the `gave_consent` field.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** | A valid email address. | [optional] 
**phone_number** | **str, none_type** | A phone number in E.164 format. | [optional] 
**date_of_birth** | **date** | A date in the format YYYY-MM-DD (RFC 3339 Section 5.6). | [optional] 
**name** | [**IdentityVerificationRequestUserName**](IdentityVerificationRequestUserName.md) |  | [optional] 
**address** | [**UserAddress**](UserAddress.md) |  | [optional] 
**id_number** | [**UserIDNumber**](UserIDNumber.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


