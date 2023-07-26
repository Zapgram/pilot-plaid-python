# plaid.model.link_token_create_request_user.LinkTokenCreateRequestUser

An object specifying information about the end user who will be linking their account.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object specifying information about the end user who will be linking their account. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**client_user_id** | str,  | str,  | A unique ID representing the end user. Typically this will be a user ID number from your application. Personally identifiable information, such as an email address or phone number, should not be used in the &#x60;client_user_id&#x60;. It is currently used as a means of searching logs for the given user in the Plaid Dashboard. | 
**legal_name** | str,  | str,  | The user&#x27;s full legal name, used for [micro-deposit based verification flows](https://plaid.com/docs/auth/coverage/). For a small number of customers on legacy flows, providing this field is required to enable micro-deposit-based flows. For all other customers, this field is optional, but providing the user&#x27;s name in this field when using micro-deposit-based verification will enable certain risk checks and can reduce micro-deposit fraud. | [optional] 
**[name](#name)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**phone_number** | str,  | str,  | The user&#x27;s phone number in [E.164](https://en.wikipedia.org/wiki/E.164) format. This field is optional, but required to enable the [returning user experience](https://plaid.com/docs/link/returning-user). Can also be used to prefill Link fields when used with Identity Verification. | [optional] 
**phone_number_verified_time** | None, str, datetime,  | NoneClass, str,  | The date and time the phone number was verified in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDThh:mm:ssZ&#x60;). This was previously an optional field used in the [returning user experience](https://plaid.com/docs/link/returning-user). This field is no longer required to enable the returning user experience.   Only pass a verification time for a phone number that you have verified. If you have performed verification but don’t have the time, you may supply a signal value of the start of the UNIX epoch.   Example: &#x60;2020-01-01T00:00:00Z&#x60;  | [optional] value must conform to RFC-3339 date-time
**email_address** | str,  | str,  | The user&#x27;s email address. This field is optional, but required to enable the [pre-authenticated returning user flow](https://plaid.com/docs/link/returning-user/#pre-authenticated-rux). Can also be used to prefill Link fields when used with Identity Verification. | [optional] 
**email_address_verified_time** | None, str, datetime,  | NoneClass, str,  | The date and time the email address was verified in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDThh:mm:ssZ&#x60;). This was previously an optional field used in the [returning user experience](https://plaid.com/docs/link/returning-user). This field is no longer required to enable the returning user experience.   Only pass a verification time for an email address that you have verified. If you have performed verification but don’t have the time, you may supply a signal value of the start of the UNIX epoch.   Example: &#x60;2020-01-01T00:00:00Z&#x60; | [optional] value must conform to RFC-3339 date-time
**ssn** | str,  | str,  | Deprecated and not currently used, use the &#x60;id_number&#x60; field instead. | [optional] 
**date_of_birth** | None, str, date,  | NoneClass, str,  | To be provided in the format \&quot;yyyy-mm-dd\&quot;. Can be used to prefill Link fields when used with Identity Verification. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**[address](#address)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**[id_number](#id_number)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[IdentityVerificationRequestUserName](IdentityVerificationRequestUserName.md) | [**IdentityVerificationRequestUserName**](IdentityVerificationRequestUserName.md) | [**IdentityVerificationRequestUserName**](IdentityVerificationRequestUserName.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The user&#x27;s full name. Optional if using the [Identity Verification](https://plaid.com/docs/api/products/identity-verification) product; if not using Identity Verification, this field is not allowed. Users will not be asked for their name when this field is provided. | 

# all_of_1

The user's full name. Optional if using the [Identity Verification](https://plaid.com/docs/api/products/identity-verification) product; if not using Identity Verification, this field is not allowed. Users will not be asked for their name when this field is provided.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The user&#x27;s full name. Optional if using the [Identity Verification](https://plaid.com/docs/api/products/identity-verification) product; if not using Identity Verification, this field is not allowed. Users will not be asked for their name when this field is provided. | 

# address

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[UserAddress](UserAddress.md) | [**UserAddress**](UserAddress.md) | [**UserAddress**](UserAddress.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The user&#x27;s address. Used only for Identity Verification. If provided, the user will not be shown fields to enter their address in the Identity Verification flow. May be omitted, but if not omitted, all fields marked as required must be provided. | 

# all_of_1

The user's address. Used only for Identity Verification. If provided, the user will not be shown fields to enter their address in the Identity Verification flow. May be omitted, but if not omitted, all fields marked as required must be provided.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The user&#x27;s address. Used only for Identity Verification. If provided, the user will not be shown fields to enter their address in the Identity Verification flow. May be omitted, but if not omitted, all fields marked as required must be provided. | 

# id_number

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[UserIDNumber](UserIDNumber.md) | [**UserIDNumber**](UserIDNumber.md) | [**UserIDNumber**](UserIDNumber.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The user&#x27;s ID number. Used only for Identity Verification. If provided, the user will not be shown fields to enter their ID number in the Identity Verification flow. May be omitted, but if not omitted, all fields marked as required must be provided. | 

# all_of_1

The user's ID number. Used only for Identity Verification. If provided, the user will not be shown fields to enter their ID number in the Identity Verification flow. May be omitted, but if not omitted, all fields marked as required must be provided.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The user&#x27;s ID number. Used only for Identity Verification. If provided, the user will not be shown fields to enter their ID number in the Identity Verification flow. May be omitted, but if not omitted, all fields marked as required must be provided. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

