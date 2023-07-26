# TransactionsGetRequestOptions

An optional object to be used with the request. If specified, `options` must not be `null`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **[str]** | A list of &#x60;account_ids&#x60; to retrieve for the Item  Note: An error will be returned if a provided &#x60;account_id&#x60; is not associated with the Item. | [optional] 
**count** | **int** | The number of transactions to fetch. | [optional]  if omitted the server will use the default value of 100
**offset** | **int** | The number of transactions to skip. The default value is 0. | [optional]  if omitted the server will use the default value of 0
**include_original_description** | **bool, none_type** | Include the raw unparsed transaction description from the financial institution. This field is disabled by default. If you need this information in addition to the parsed data provided, contact your Plaid Account Manager, or submit a [Support request](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/product-functionality) . | [optional]  if omitted the server will use the default value of False
**include_personal_finance_category_beta** | **bool** | Please use [&#x60;include_personal_finance_category&#x60;](https://plaid.com/docs/api/products/transactions/#transactions-get-request-options-include-personal-finance-category) instead. | [optional]  if omitted the server will use the default value of False
**include_personal_finance_category** | **bool** | Include the [&#x60;personal_finance_category&#x60;](https://plaid.com/docs/api/products/transactions/#transactions-get-response-transactions-personal-finance-category) object in the response.  All implementations are encouraged to set this field to &#x60;true&#x60; and use the &#x60;personal_finance_category&#x60; instead of &#x60;category&#x60;. Personal finance categories are the preferred categorization system for transactions, providing higher accuracy and more meaningful categories.  See the [&#x60;taxonomy csv file&#x60;](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories.  Plaid is also introducing Category Rules - a new endpoint that will enable you to change the &#x60;personal_finance_category&#x60; for a transaction based on your users’ needs. When rules are set, the selected category will override the Plaid provided category. To learn more, send a note to transactions-feedback@plaid.com. | [optional]  if omitted the server will use the default value of False
**include_logo_and_counterparty_beta** | **bool** | Include counterparties and extran merchant fields in the transaction. This field is disabled by default. If you need this information in addition to the parsed data provided, contact your Plaid Account Manager. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


