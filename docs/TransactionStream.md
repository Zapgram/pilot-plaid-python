# TransactionStream

A grouping of related transactions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the account to which the stream belongs | 
**stream_id** | **str** | A unique id for the stream | 
**category** | **[str]** | A hierarchical array of the categories to which this transaction belongs. See [Categories](https://plaid.com/docs/api/products/transactions/#categoriesget).  All implementations are encouraged to use the new &#x60;personal_finance_category&#x60; instead of &#x60;category&#x60;. &#x60;personal_finance_category&#x60; provides more meaningful categorization and greater accuracy. | 
**category_id** | **str** | The ID of the category to which this transaction belongs. See [Categories](https://plaid.com/docs/api/products/transactions/#categoriesget).  All implementations are encouraged to use the new &#x60;personal_finance_category&#x60; instead of &#x60;category&#x60;. &#x60;personal_finance_category&#x60; provides more meaningful categorization and greater accuracy. | 
**description** | **str** | A description of the transaction stream. | 
**merchant_name** | **str, none_type** | The merchant associated with the transaction stream. | 
**first_date** | **date** | The posted date of the earliest transaction in the stream. | 
**last_date** | **date** | The posted date of the latest transaction in the stream. | 
**frequency** | [**RecurringTransactionFrequency**](RecurringTransactionFrequency.md) |  | 
**transaction_ids** | **[str]** | An array of Plaid transaction IDs belonging to the stream, sorted by posted date. | 
**average_amount** | [**TransactionStreamAmount**](TransactionStreamAmount.md) |  | 
**last_amount** | [**TransactionStreamAmount**](TransactionStreamAmount.md) |  | 
**is_active** | **bool** | Indicates whether the transaction stream is still live. | 
**status** | [**TransactionStreamStatus**](TransactionStreamStatus.md) |  | 
**personal_finance_category** | [**PersonalFinanceCategory**](PersonalFinanceCategory.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


