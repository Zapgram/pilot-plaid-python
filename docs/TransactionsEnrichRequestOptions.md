# TransactionsEnrichRequestOptions

An optional object to be used with the request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_legacy_category** | **bool** | Include &#x60;legacy_category&#x60; and &#x60;legacy_category_id&#x60; in the response (in addition to the default &#x60;personal_finance_category&#x60;).  Categories are based on Plaid&#39;s legacy taxonomy. For a full list of legacy categories, see [&#x60;/categories/get&#x60;](https://plaid.com/docs/api/products/transactions/#categoriesget). | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


