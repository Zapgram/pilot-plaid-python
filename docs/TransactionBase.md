# TransactionBase

A representation of a transaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the account in which this transaction occurred. | 
**amount** | **float** | The settled value of the transaction, denominated in the transactions&#39;s currency, as stated in &#x60;iso_currency_code&#x60; or &#x60;unofficial_currency_code&#x60;. Positive values when money moves out of the account; negative values when money moves in. For example, debit card purchases are positive; credit card payments, direct deposits, and refunds are negative. | 
**iso_currency_code** | **str, none_type** | The ISO-4217 currency code of the transaction. Always &#x60;null&#x60; if &#x60;unofficial_currency_code&#x60; is non-null. | 
**unofficial_currency_code** | **str, none_type** | The unofficial currency code associated with the transaction. Always &#x60;null&#x60; if &#x60;iso_currency_code&#x60; is non-&#x60;null&#x60;. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported &#x60;iso_currency_code&#x60;s. | 
**date** | **date** | For pending transactions, the date that the transaction occurred; for posted transactions, the date that the transaction posted. Both dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( &#x60;YYYY-MM-DD&#x60; ). To receive information about the date that a posted transaction was initiated, see the &#x60;authorized_date&#x60; field. | 
**pending** | **bool** | When &#x60;true&#x60;, identifies the transaction as pending or unsettled. Pending transaction details (name, type, amount, category ID) may change before they are settled. | 
**transaction_id** | **str** | The unique ID of the transaction. Like all Plaid identifiers, the &#x60;transaction_id&#x60; is case sensitive. | 
**category** | **[str], none_type** | A hierarchical array of the categories to which this transaction belongs. For a full list of categories, see [&#x60;/categories/get&#x60;](https://plaid.com/docs/api/products/transactions/#categoriesget).  All Transactions implementations are recommended to use the new &#x60;personal_finance_category&#x60; instead of &#x60;category&#x60;. &#x60;personal_finance_category&#x60; provides more meaningful categorization and greater accuracy.  If the &#x60;transactions&#x60; object was returned by an Assets endpoint such as &#x60;/asset_report/get/&#x60; or &#x60;/asset_report/pdf/get&#x60;, this field will only appear in an Asset Report with Insights. | [optional] 
**category_id** | **str, none_type** | The ID of the category to which this transaction belongs. For a full list of categories, see [&#x60;/categories/get&#x60;](https://plaid.com/docs/api/products/transactions/#categoriesget).  All Transactions implementations are recommended to use the new &#x60;personal_finance_category&#x60; instead of &#x60;category_id&#x60;, as it provides greater accuracy and more meaningful categorization.  If the &#x60;transactions&#x60; object was returned by an Assets endpoint such as &#x60;/asset_report/get/&#x60; or &#x60;/asset_report/pdf/get&#x60;, this field will only appear in an Asset Report with Insights. | [optional] 
**check_number** | **str, none_type** | The check number of the transaction. This field is only populated for check transactions. | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**name** | **str** | The merchant name or transaction description.  If the &#x60;transactions&#x60; object was returned by a Transactions endpoint such as &#x60;/transactions/sync&#x60; or &#x60;/transactions/get&#x60;, this field will always appear. If the &#x60;transactions&#x60; object was returned by an Assets endpoint such as &#x60;/asset_report/get/&#x60; or &#x60;/asset_report/pdf/get&#x60;, this field will only appear in an Asset Report with Insights. | [optional] 
**merchant_name** | **str, none_type** | The merchant name, as enriched by Plaid from the &#x60;name&#x60; field. This is typically a more human-readable version of the merchant counterparty in the transaction. For some bank transactions (such as checks or account transfers) where there is no meaningful merchant name, this value will be &#x60;null&#x60;. | [optional] 
**original_description** | **str, none_type** | The string returned by the financial institution to describe the transaction. For transactions returned by &#x60;/transactions/sync&#x60; or &#x60;/transactions/get&#x60;, this field is in beta and will be omitted unless the client is both enrolled in the closed beta program and has set &#x60;options.include_original_description&#x60; to &#x60;true&#x60;. | [optional] 
**payment_meta** | [**PaymentMeta**](PaymentMeta.md) |  | [optional] 
**pending_transaction_id** | **str, none_type** | The ID of a posted transaction&#39;s associated pending transaction, where applicable. | [optional] 
**account_owner** | **str, none_type** | The name of the account owner. This field is not typically populated and only relevant when dealing with sub-accounts. | [optional] 
**transaction_type** | **str** | Please use the &#x60;payment_channel&#x60; field, &#x60;transaction_type&#x60; will be deprecated in the future.  &#x60;digital:&#x60; transactions that took place online.  &#x60;place:&#x60; transactions that were made at a physical location.  &#x60;special:&#x60; transactions that relate to banks, e.g. fees or deposits.  &#x60;unresolved:&#x60; transactions that do not fit into the other three types.  | [optional] 
**logo_url** | **str, none_type** | The logo associated with the merchant, if available. Formatted as a 100x100 pixels PNG file path. | [optional] 
**website** | **str, none_type** | The website associated with the merchant, if available. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


