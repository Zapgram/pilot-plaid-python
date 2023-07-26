# plaid.model.client_provided_transaction.ClientProvidedTransaction

A client-provided transaction for Plaid to enrich.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A client-provided transaction for Plaid to enrich. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The absolute value of the transaction (&gt;&#x3D; 0). When testing Enrich, note that &#x60;amount&#x60; data should be realistic. Unrealistic or inaccurate &#x60;amount&#x60; data may result in reduced quality output. | value must be a 64 bit float
**iso_currency_code** | str,  | str,  | The ISO-4217 currency code of the transaction e.g. USD. | 
**description** | str,  | str,  | The raw description of the transaction. If you have location data in available an unstructured format, it may be appended to the &#x60;description&#x60; field. | 
**id** | str,  | str,  | A unique ID for the transaction used to help you tie data back to your systems. | 
**direction** | [**EnrichTransactionDirection**](EnrichTransactionDirection.md) | [**EnrichTransactionDirection**](EnrichTransactionDirection.md) |  | 
**client_user_id** | str,  | str,  | A unique user id used to group transactions for a given user, as a unique identifier from your application. Personally identifiable information, such as an email address or phone number, should not be used in the client_user_id. | [optional] 
**client_account_id** | str,  | str,  | A unique account id used to group transactions for a given account, as a unique identifier from your application. Personally identifiable information, such as an email address or phone number, should not be used in the client_account_id. | [optional] 
**account_type** | str,  | str,  | The account type associated with the transaction. For a full list of valid types and subtypes, see the [Account schema](https://plaid.com/docs/api/accounts#account-type-schema). | [optional] 
**account_subtype** | str,  | str,  | The account subtype associated with the transaction. For a full list of valid types and subtypes, see the [Account schema](https://plaid.com/docs/api/accounts#account-type-schema). | [optional] 
**location** | [**ClientProvidedTransactionLocation**](ClientProvidedTransactionLocation.md) | [**ClientProvidedTransactionLocation**](ClientProvidedTransactionLocation.md) |  | [optional] 
**mcc** | str,  | str,  | Merchant category codes (MCCs) are four-digit numbers that describe a merchant&#x27;s primary business activities. | [optional] 
**date_posted** | str, date,  | str,  | The date the transaction posted, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

