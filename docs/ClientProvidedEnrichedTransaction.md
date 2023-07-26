# ClientProvidedEnrichedTransaction

A client-provided transaction that Plaid has enriched.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID for the transaction as provided by you in the request. | 
**description** | **str** | The raw description of the transaction. | 
**amount** | **float** | The absolute value of the transaction (&gt;&#x3D; 0) | 
**iso_currency_code** | **str** | The ISO-4217 currency code of the transaction e.g. USD. | 
**enrichments** | [**Enrichments**](Enrichments.md) |  | 
**client_user_id** | **str** | A unique user id used to group transactions for a given user, as a unique identifier from your application. Personally identifiable information, such as an email address or phone number, should not be used in the client_user_id. | [optional] 
**client_account_id** | **str** | A unique account id used to group transactions for a given account, as a unique identifier from your application. Personally identifiable information, such as an email address or phone number, should not be used in the client_account_id. | [optional] 
**account_type** | **str** | The account type associated with the transaction. For a full list of valid types and subtypes, see the [Account schema](https://plaid.com/docs/api/accounts#account-type-schema). | [optional] 
**account_subtype** | **str** | The account subtype associated with the transaction. For a full list of valid types and subtypes, see the [Account schema](https://plaid.com/docs/api/accounts#account-type-schema). | [optional] 
**direction** | [**EnrichTransactionDirection**](EnrichTransactionDirection.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


