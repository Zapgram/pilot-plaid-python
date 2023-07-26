# plaid.model.transaction_stream.TransactionStream

A grouping of related transactions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A grouping of related transactions | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**average_amount** | [**TransactionStreamAmount**](TransactionStreamAmount.md) | [**TransactionStreamAmount**](TransactionStreamAmount.md) |  | 
**is_active** | bool,  | BoolClass,  | Indicates whether the transaction stream is still live. | 
**description** | str,  | str,  | A description of the transaction stream. | 
**merchant_name** | None, str,  | NoneClass, str,  | The merchant associated with the transaction stream. | 
**last_date** | str, date,  | str,  | The posted date of the latest transaction in the stream. | value must conform to RFC-3339 full-date YYYY-MM-DD
**frequency** | [**RecurringTransactionFrequency**](RecurringTransactionFrequency.md) | [**RecurringTransactionFrequency**](RecurringTransactionFrequency.md) |  | 
**account_id** | str,  | str,  | The ID of the account to which the stream belongs | 
**category_id** | str,  | str,  | The ID of the category to which this transaction belongs. See [Categories](https://plaid.com/docs/api/products/transactions/#categoriesget).  All implementations are encouraged to use the new &#x60;personal_finance_category&#x60; instead of &#x60;category&#x60;. &#x60;personal_finance_category&#x60; provides more meaningful categorization and greater accuracy. | 
**stream_id** | str,  | str,  | A unique id for the stream | 
**[transaction_ids](#transaction_ids)** | list, tuple,  | tuple,  | An array of Plaid transaction IDs belonging to the stream, sorted by posted date. | 
**[category](#category)** | list, tuple,  | tuple,  | A hierarchical array of the categories to which this transaction belongs. See [Categories](https://plaid.com/docs/api/products/transactions/#categoriesget).  All implementations are encouraged to use the new &#x60;personal_finance_category&#x60; instead of &#x60;category&#x60;. &#x60;personal_finance_category&#x60; provides more meaningful categorization and greater accuracy. | 
**first_date** | str, date,  | str,  | The posted date of the earliest transaction in the stream. | value must conform to RFC-3339 full-date YYYY-MM-DD
**last_amount** | [**TransactionStreamAmount**](TransactionStreamAmount.md) | [**TransactionStreamAmount**](TransactionStreamAmount.md) |  | 
**status** | [**TransactionStreamStatus**](TransactionStreamStatus.md) | [**TransactionStreamStatus**](TransactionStreamStatus.md) |  | 
**personal_finance_category** | [**PersonalFinanceCategory**](PersonalFinanceCategory.md) | [**PersonalFinanceCategory**](PersonalFinanceCategory.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# category

A hierarchical array of the categories to which this transaction belongs. See [Categories](https://plaid.com/docs/api/products/transactions/#categoriesget).  All implementations are encouraged to use the new `personal_finance_category` instead of `category`. `personal_finance_category` provides more meaningful categorization and greater accuracy.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A hierarchical array of the categories to which this transaction belongs. See [Categories](https://plaid.com/docs/api/products/transactions/#categoriesget).  All implementations are encouraged to use the new &#x60;personal_finance_category&#x60; instead of &#x60;category&#x60;. &#x60;personal_finance_category&#x60; provides more meaningful categorization and greater accuracy. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# transaction_ids

An array of Plaid transaction IDs belonging to the stream, sorted by posted date.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of Plaid transaction IDs belonging to the stream, sorted by posted date. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

