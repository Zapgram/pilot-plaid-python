# LinkTokenCreateRequestUser

An object specifying information about the end user who will be linking their account.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_user_id** | **str** | A unique ID representing the end user. Typically this will be a user ID number from your application. Personally identifiable information, such as an email address or phone number, should not be used in the &#x60;client_user_id&#x60;. It is currently used as a means of searching logs for the given user in the Plaid Dashboard. | 
**legal_name** | **str** | The user&#39;s full legal name, used for [micro-deposit based verification flows](https://plaid.com/docs/auth/coverage/). For a small number of customers on legacy flows, providing this field is required to enable micro-deposit-based flows. For all other customers, this field is optional, but providing the user&#39;s name in this field when using micro-deposit-based verification will enable certain risk checks and can reduce micro-deposit fraud. | [optional] 
**name** | [**LinkTokenCreateRequestUserName**](LinkTokenCreateRequestUserName.md) |  | [optional] 
**phone_number** | **str** | The user&#39;s phone number in [E.164](https://en.wikipedia.org/wiki/E.164) format. This field is optional, but required to enable the [returning user experience](https://plaid.com/docs/link/returning-user). Can also be used to prefill Link fields when used with Identity Verification. | [optional] 
**phone_number_verified_time** | **datetime, none_type** | The date and time the phone number was verified in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDThh:mm:ssZ&#x60;). This was previously an optional field used in the [returning user experience](https://plaid.com/docs/link/returning-user). This field is no longer required to enable the returning user experience.   Only pass a verification time for a phone number that you have verified. If you have performed verification but don’t have the time, you may supply a signal value of the start of the UNIX epoch.   Example: &#x60;2020-01-01T00:00:00Z&#x60;  | [optional] 
**email_address** | **str** | The user&#39;s email address. This field is optional, but required to enable the [pre-authenticated returning user flow](https://plaid.com/docs/link/returning-user/#pre-authenticated-rux). Can also be used to prefill Link fields when used with Identity Verification. | [optional] 
**email_address_verified_time** | **datetime, none_type** | The date and time the email address was verified in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDThh:mm:ssZ&#x60;). This was previously an optional field used in the [returning user experience](https://plaid.com/docs/link/returning-user). This field is no longer required to enable the returning user experience.   Only pass a verification time for an email address that you have verified. If you have performed verification but don’t have the time, you may supply a signal value of the start of the UNIX epoch.   Example: &#x60;2020-01-01T00:00:00Z&#x60; | [optional] 
**ssn** | **str** | Deprecated and not currently used, use the &#x60;id_number&#x60; field instead. | [optional] 
**date_of_birth** | **date, none_type** | To be provided in the format \&quot;yyyy-mm-dd\&quot;. Can be used to prefill Link fields when used with Identity Verification. | [optional] 
**address** | [**LinkTokenCreateRequestUserAddress**](LinkTokenCreateRequestUserAddress.md) |  | [optional] 
**id_number** | [**LinkTokenCreateRequestUserIdNumber**](LinkTokenCreateRequestUserIdNumber.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


