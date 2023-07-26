# ClientProvidedTransaction

A client-provided transaction for Plaid to enrich.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID for the transaction used to help you tie data back to your systems. | 
**description** | **str** | The raw description of the transaction. If you have location data in available an unstructured format, it may be appended to the &#x60;description&#x60; field. | 
**amount** | **float** | The absolute value of the transaction (&gt;&#x3D; 0). When testing Enrich, note that &#x60;amount&#x60; data should be realistic. Unrealistic or inaccurate &#x60;amount&#x60; data may result in reduced quality output. | 
**direction** | [**EnrichTransactionDirection**](EnrichTransactionDirection.md) |  | 
**iso_currency_code** | **str** | The ISO-4217 currency code of the transaction e.g. USD. | 
**client_user_id** | **str** | A unique user id used to group transactions for a given user, as a unique identifier from your application. Personally identifiable information, such as an email address or phone number, should not be used in the client_user_id. | [optional] 
**client_account_id** | **str** | A unique account id used to group transactions for a given account, as a unique identifier from your application. Personally identifiable information, such as an email address or phone number, should not be used in the client_account_id. | [optional] 
**account_type** | **str** | The account type associated with the transaction. For a full list of valid types and subtypes, see the [Account schema](https://plaid.com/docs/api/accounts#account-type-schema). | [optional] 
**account_subtype** | **str** | The account subtype associated with the transaction. For a full list of valid types and subtypes, see the [Account schema](https://plaid.com/docs/api/accounts#account-type-schema). | [optional] 
**location** | [**ClientProvidedTransactionLocation**](ClientProvidedTransactionLocation.md) |  | [optional] 
**mcc** | **str** | Merchant category codes (MCCs) are four-digit numbers that describe a merchant&#39;s primary business activities. | [optional] 
**date_posted** | **date** | The date the transaction posted, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


