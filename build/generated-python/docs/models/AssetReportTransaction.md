# plaid.model.asset_report_transaction.AssetReportTransaction

A transaction on the asset report

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A transaction on the asset report | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date** | str, date,  | str,  | For pending transactions, the date that the transaction occurred; for posted transactions, the date that the transaction posted. Both dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( &#x60;YYYY-MM-DD&#x60; ). | value must conform to RFC-3339 full-date YYYY-MM-DD
**transaction_id** | str,  | str,  | The unique ID of the transaction. Like all Plaid identifiers, the &#x60;transaction_id&#x60; is case sensitive. | 
**unofficial_currency_code** | None, str,  | NoneClass, str,  | The unofficial currency code associated with the transaction. Always &#x60;null&#x60; if &#x60;iso_currency_code&#x60; is non-&#x60;null&#x60;. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported &#x60;iso_currency_code&#x60;s. | 
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The settled value of the transaction, denominated in the transactions&#x27;s currency, as stated in &#x60;iso_currency_code&#x60; or &#x60;unofficial_currency_code&#x60;. Positive values when money moves out of the account; negative values when money moves in. For example, debit card purchases are positive; credit card payments, direct deposits, and refunds are negative. | value must be a 64 bit float
**account_id** | str,  | str,  | The ID of the account in which this transaction occurred. | 
**pending** | bool,  | BoolClass,  | When &#x60;true&#x60;, identifies the transaction as pending or unsettled. Pending transaction details (name, type, amount, category ID) may change before they are settled. | 
**iso_currency_code** | None, str,  | NoneClass, str,  | The ISO-4217 currency code of the transaction. Always &#x60;null&#x60; if &#x60;unofficial_currency_code&#x60; is non-null. | 
**original_description** | None, str,  | NoneClass, str,  | The string returned by the financial institution to describe the transaction. For transactions returned by &#x60;/transactions/get&#x60;, this field is in beta and will be omitted unless the client is both enrolled in the closed beta program and has set &#x60;options.include_original_description&#x60; to &#x60;true&#x60;. | 
**[category](#category)** | list, tuple, None,  | tuple, NoneClass,  | A hierarchical array of the categories to which this transaction belongs. For a full list of categories, see [&#x60;/categories/get&#x60;](https://plaid.com/docs/api/products/transactions/#categoriesget).  All Transactions implementations are recommended to use the new &#x60;personal_finance_category&#x60; instead of &#x60;category&#x60;. &#x60;personal_finance_category&#x60; provides more meaningful categorization and greater accuracy.  If the &#x60;transactions&#x60; object was returned by an Assets endpoint such as &#x60;/asset_report/get/&#x60; or &#x60;/asset_report/pdf/get&#x60;, this field will only appear in an Asset Report with Insights. | [optional] 
**category_id** | None, str,  | NoneClass, str,  | The ID of the category to which this transaction belongs. For a full list of categories, see [&#x60;/categories/get&#x60;](https://plaid.com/docs/api/products/transactions/#categoriesget).  All Transactions implementations are recommended to use the new &#x60;personal_finance_category&#x60; instead of &#x60;category_id&#x60;, as it provides greater accuracy and more meaningful categorization.  If the &#x60;transactions&#x60; object was returned by an Assets endpoint such as &#x60;/asset_report/get/&#x60; or &#x60;/asset_report/pdf/get&#x60;, this field will only appear in an Asset Report with Insights. | [optional] 
**credit_category** | [**CreditCategory**](CreditCategory.md) | [**CreditCategory**](CreditCategory.md) |  | [optional] 
**check_number** | None, str,  | NoneClass, str,  | The check number of the transaction. This field is only populated for check transactions. | [optional] 
**date_transacted** | None, str,  | NoneClass, str,  | The date on which the transaction took place, in IS0 8601 format. | [optional] 
**location** | [**Location**](Location.md) | [**Location**](Location.md) |  | [optional] 
**name** | str,  | str,  | The merchant name or transaction description.  If the &#x60;transactions&#x60; object was returned by a Transactions endpoint such as &#x60;/transactions/get&#x60;, this field will always appear. If the &#x60;transactions&#x60; object was returned by an Assets endpoint such as &#x60;/asset_report/get/&#x60; or &#x60;/asset_report/pdf/get&#x60;, this field will only appear in an Asset Report with Insights. | [optional] 
**merchant_name** | None, str,  | NoneClass, str,  | The merchant name, as enriched by Plaid from the &#x60;name&#x60; field. This is typically a more human-readable version of the merchant counterparty in the transaction. For some bank transactions (such as checks or account transfers) where there is no meaningful merchant name, this value will be &#x60;null&#x60;. | [optional] 
**payment_meta** | [**PaymentMeta**](PaymentMeta.md) | [**PaymentMeta**](PaymentMeta.md) |  | [optional] 
**pending_transaction_id** | None, str,  | NoneClass, str,  | The ID of a posted transaction&#x27;s associated pending transaction, where applicable. | [optional] 
**account_owner** | None, str,  | NoneClass, str,  | The name of the account owner. This field is not typically populated and only relevant when dealing with sub-accounts. | [optional] 
**transaction_type** | [**AssetReportTransactionType**](AssetReportTransactionType.md) | [**AssetReportTransactionType**](AssetReportTransactionType.md) |  | [optional] 
**income_source_id** | str,  | str,  | A unique identifier for an income source. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# category

A hierarchical array of the categories to which this transaction belongs. For a full list of categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).  All Transactions implementations are recommended to use the new `personal_finance_category` instead of `category`. `personal_finance_category` provides more meaningful categorization and greater accuracy.  If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | A hierarchical array of the categories to which this transaction belongs. For a full list of categories, see [&#x60;/categories/get&#x60;](https://plaid.com/docs/api/products/transactions/#categoriesget).  All Transactions implementations are recommended to use the new &#x60;personal_finance_category&#x60; instead of &#x60;category&#x60;. &#x60;personal_finance_category&#x60; provides more meaningful categorization and greater accuracy.  If the &#x60;transactions&#x60; object was returned by an Assets endpoint such as &#x60;/asset_report/get/&#x60; or &#x60;/asset_report/pdf/get&#x60;, this field will only appear in an Asset Report with Insights. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

