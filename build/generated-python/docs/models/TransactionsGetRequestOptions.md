# plaid.model.transactions_get_request_options.TransactionsGetRequestOptions

An optional object to be used with the request. If specified, `options` must not be `null`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An optional object to be used with the request. If specified, &#x60;options&#x60; must not be &#x60;null&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[account_ids](#account_ids)** | list, tuple,  | tuple,  | A list of &#x60;account_ids&#x60; to retrieve for the Item  Note: An error will be returned if a provided &#x60;account_id&#x60; is not associated with the Item. | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  | The number of transactions to fetch. | [optional] if omitted the server will use the default value of 100
**offset** | decimal.Decimal, int,  | decimal.Decimal,  | The number of transactions to skip. The default value is 0. | [optional] if omitted the server will use the default value of 0
**include_original_description** | None, bool,  | NoneClass, BoolClass,  | Include the raw unparsed transaction description from the financial institution. This field is disabled by default. If you need this information in addition to the parsed data provided, contact your Plaid Account Manager, or submit a [Support request](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/product-functionality) . | [optional] if omitted the server will use the default value of False
**include_personal_finance_category_beta** | bool,  | BoolClass,  | Please use [&#x60;include_personal_finance_category&#x60;](https://plaid.com/docs/api/products/transactions/#transactions-get-request-options-include-personal-finance-category) instead. | [optional] if omitted the server will use the default value of False
**include_personal_finance_category** | bool,  | BoolClass,  | Include the [&#x60;personal_finance_category&#x60;](https://plaid.com/docs/api/products/transactions/#transactions-get-response-transactions-personal-finance-category) object in the response.  All implementations are encouraged to set this field to &#x60;true&#x60; and use the &#x60;personal_finance_category&#x60; instead of &#x60;category&#x60;. Personal finance categories are the preferred categorization system for transactions, providing higher accuracy and more meaningful categories.  See the [&#x60;taxonomy csv file&#x60;](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories.  Plaid is also introducing Category Rules - a new endpoint that will enable you to change the &#x60;personal_finance_category&#x60; for a transaction based on your users’ needs. When rules are set, the selected category will override the Plaid provided category. To learn more, send a note to transactions-feedback@plaid.com. | [optional] if omitted the server will use the default value of False
**include_logo_and_counterparty_beta** | bool,  | BoolClass,  | Include counterparties and extran merchant fields in the transaction. This field is disabled by default. If you need this information in addition to the parsed data provided, contact your Plaid Account Manager. | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# account_ids

A list of `account_ids` to retrieve for the Item  Note: An error will be returned if a provided `account_id` is not associated with the Item.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of &#x60;account_ids&#x60; to retrieve for the Item  Note: An error will be returned if a provided &#x60;account_id&#x60; is not associated with the Item. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

