# TransactionsSyncRequestOptions

An optional object to be used with the request. If specified, `options` must not be `null`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_original_description** | **bool, none_type** | Include the raw unparsed transaction description from the financial institution. This field is disabled by default. If you need this information in addition to the parsed data provided, contact your Plaid Account Manager or submit a [Support request](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/product-functionality). | [optional]  if omitted the server will use the default value of False
**include_personal_finance_category** | **bool** | Include the [&#x60;personal_finance_category&#x60;](https://plaid.com/docs/api/products/transactions/#transactions-sync-response-added-personal-finance-category) object in the response.  All implementations are encouraged to use set this field to &#x60;true&#x60; and to use the &#x60;personal_finance_category&#x60; instead of &#x60;category&#x60; for more meaningful and accurate categorization.  See the [&#x60;taxonomy csv file&#x60;](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories.  We’re also introducing Category Rules - a new beta endpoint that will enable you to change the &#x60;personal_finance_category&#x60; for a transaction based on your users’ needs. When rules are set, the selected category will override the Plaid provided category. To learn more, send a note to transactions-feedback@plaid.com. | [optional]  if omitted the server will use the default value of False
**include_logo_and_counterparty_beta** | **bool** | Include counterparties and extra merchant fields in the transaction. This field is disabled by default. If you need this information in addition to the parsed data provided, contact your Plaid Account Manager. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


