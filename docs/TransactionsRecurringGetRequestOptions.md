# TransactionsRecurringGetRequestOptions

An optional object to be used with the request. If specified, `options` must not be `null`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_personal_finance_category** | **bool** | Include the [&#x60;personal_finance_category&#x60;](https://plaid.com/docs/api/products/transactions/#transactions-get-response-transactions-personal-finance-category) object for each transaction stream in the response.  All implementations are encouraged to set this field to &#x60;true&#x60; and to use the &#x60;personal_finance_category&#x60; field instead of &#x60;category&#x60;. Personal finance categories are the preferred categorization system for transactions, providing higher accuracy and more meaningful categories.  See the [&#x60;taxonomy csv file&#x60;](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


