# plaid.model.client_provided_enriched_transaction.ClientProvidedEnrichedTransaction

A client-provided transaction that Plaid has enriched.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A client-provided transaction that Plaid has enriched. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The absolute value of the transaction (&gt;&#x3D; 0) | value must be a 64 bit float
**iso_currency_code** | str,  | str,  | The ISO-4217 currency code of the transaction e.g. USD. | 
**description** | str,  | str,  | The raw description of the transaction. | 
**id** | str,  | str,  | The unique ID for the transaction as provided by you in the request. | 
**enrichments** | [**Enrichments**](Enrichments.md) | [**Enrichments**](Enrichments.md) |  | 
**client_user_id** | str,  | str,  | A unique user id used to group transactions for a given user, as a unique identifier from your application. Personally identifiable information, such as an email address or phone number, should not be used in the client_user_id. | [optional] 
**client_account_id** | str,  | str,  | A unique account id used to group transactions for a given account, as a unique identifier from your application. Personally identifiable information, such as an email address or phone number, should not be used in the client_account_id. | [optional] 
**account_type** | str,  | str,  | The account type associated with the transaction. For a full list of valid types and subtypes, see the [Account schema](https://plaid.com/docs/api/accounts#account-type-schema). | [optional] 
**account_subtype** | str,  | str,  | The account subtype associated with the transaction. For a full list of valid types and subtypes, see the [Account schema](https://plaid.com/docs/api/accounts#account-type-schema). | [optional] 
**direction** | [**EnrichTransactionDirection**](EnrichTransactionDirection.md) | [**EnrichTransactionDirection**](EnrichTransactionDirection.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

